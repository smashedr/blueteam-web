import datetime
import logging
import requests
from celery.decorators import task
from django.conf import settings
from django.utils.timezone import now
from .models import TwitchToken, BlueProfile

logger = logging.getLogger('celery')


@task(name='check_twitch_live')
def check_twitch_live():
    logger.info('check_twitch_live: executed')
    access_token = get_twitch_token()
    logger.info(access_token)

    blue = BlueProfile.objects.all()
    twitch_usernames = [u.twitch_username for u in blue if u.twitch_username]

    url = 'https://api.twitch.tv/helix/streams'
    params = {'user_login': twitch_usernames}
    headers = {
        'Client-ID': settings.TWITCH_CLIENT_ID,
        'Authorization': 'Bearer {}'.format(access_token),
    }
    r = requests.get(url, params, headers=headers)
    if not r.ok:
        r.raise_for_status()

    data = r.json()['data']
    live_users = [u['user_name'].lower() for u in data]
    for u in blue:
        if u.twitch_username.lower() in live_users:
            u.live_on_twitch = True
        else:
            u.live_on_twitch = False
        u.save()
    return 'Finished'


def get_twitch_token():
    twitch_token = TwitchToken.objects.get_or_create(id=1)[0]
    if twitch_token:
        if twitch_token.access_token and twitch_token.access_token:
            if twitch_token.expiration_date > now():
                return twitch_token.access_token

    url = 'https://id.twitch.tv/oauth2/token'
    data = {
        'client_id': settings.TWITCH_CLIENT_ID,
        'client_secret': settings.TWITCH_CLIENT_SECRET,
        'grant_type': 'client_credentials',
    }
    r = requests.post(url, data)
    logger.info(r.status_code)
    if not r.ok:
        r.raise_for_status()

    token_info = r.json()
    exp_date = now() + datetime.timedelta(0, token_info['expires_in'] - 300)
    twitch_token.access_token = token_info['access_token']
    twitch_token.expiration_date = exp_date
    twitch_token.save()
    return twitch_token.access_token
