import logging
from home.forms import ProfileForm
from home.models import BlueProfile
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from pprint import pformat

logger = logging.getLogger('app')


def home_view(request):
    #  View: /
    return render(request, 'home.html')


def roster_view(request):
    #  View: /
    guild_roster = BlueProfile.objects.all()
    return render(request, 'roster.html', {'guild_roster': guild_roster})


@login_required
def profile_view(request):
    #  View: /
    if not request.method == 'POST':
        if request.user.is_authenticated:
            logger.debug(request.user.profile.discord_id)
            blue_profile = BlueProfile.objects.filter(discord_id=request.user.profile.discord_id).first()
            if blue_profile:
                logger.debug('YES PROFILE FOUND')
            else:
                logger.debug('NO PROFILE FOUND')
                blue_profile = {}
            return render(request, 'profile.html', {'blue_profile': blue_profile})
        else:
            return render(request, 'profile.html')

    else:
        logger.debug(pformat(request.POST))  # DEBUGGING ONLY
        form = ProfileForm(request.POST)
        if not form.is_valid():
            return JsonResponse(form.errors, status=400)
        else:
            blue_profile = BlueProfile(
                discord_id=request.user.profile.discord_id,
                main_char=form.cleaned_data['main_char'],
                main_class=form.cleaned_data['main_class'],
                main_role=form.cleaned_data['main_role'],
                user_description=form.cleaned_data['user_description'],
                show_in_roster=form.cleaned_data['show_in_roster'],
            )
            blue_profile.save()
            return JsonResponse({'message': 'ok'}, status=200)


@login_required
@require_http_methods(['POST'])
def create_cm(request):
    """
    View: /profile/update/
    """
    logger.debug(pformat(request.POST))  # DEBUGGING ONLY
    form = ProfileForm(request.POST)
    if not form.is_valid():
        return JsonResponse(form.errors, status=400)
    else:
        pass
