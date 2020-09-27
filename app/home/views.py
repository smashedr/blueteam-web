import logging
from pprint import pformat
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.shortcuts import render
from .forms import ProfileForm
from .models import BlueProfile, BlueNews

logger = logging.getLogger('app')


def is_blue_member(user):
    return user.blue_team_member


def is_blue_officer(user):
    return user.blue_team_officer


def home_view(request):
    # View: /
    if request.user.is_authenticated:
        blue_profile = BlueProfile.objects.filter(
            discord_id=request.user.discord_id
        ).first()
    else:
        blue_profile = {}

    blue_news = BlueNews.objects.all().order_by('-pk')[:2]
    data = {'blue_profile': blue_profile, 'blue_news': blue_news}
    return render(request, 'home.html', data)


def news_view(request):
    # View: /roster/
    blue_news = BlueNews.objects.all().order_by('-pk')[:50]
    return render(request, 'news.html', {'blue_news': blue_news})


def roster_view(request):
    # View: /roster/
    guild_roster = BlueProfile.objects.all().order_by('-pk')
    return render(request, 'roster.html', {'guild_roster': guild_roster})


@login_required
@user_passes_test(is_blue_member, login_url='/')
def profile_view(request):
    # View: /profile/
    if not request.method == 'POST':
        if request.user.is_authenticated:
            blue_profile = BlueProfile.objects.filter(
                discord_id=request.user.discord_id
            ).first()
            blue_profile = {} if not blue_profile else blue_profile
            data = {'blue_profile': blue_profile}
            return render(request, 'profile.html', data)
        else:
            return render(request, 'profile.html')

    else:
        logger.debug(pformat(request.POST))  # LOCAL DEBUGGING ONLY
        form = ProfileForm(request.POST)
        if form.is_valid():
            blue_profile = BlueProfile(
                discord_id=request.user.discord_id,
                main_char=form.cleaned_data['main_char'],
                main_class=form.cleaned_data['main_class'],
                main_role=form.cleaned_data['main_role'],
                user_description=form.cleaned_data['user_description'],
                show_in_roster=form.cleaned_data['show_in_roster'],
            )
            blue_profile.save()
            return JsonResponse({'message': 'ok'}, status=200)
        else:
            return JsonResponse(form.errors, status=400)
