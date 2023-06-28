from django.shortcuts import render

from myplant.web.models import Profile


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        nav_bar_visible = True
    else:
        nav_bar_visible = False

    context = {
        'nav_bar_visible': nav_bar_visible,
    }
    return render(request, 'home-page.html', context)


def profile_create(request):
    return render(request, 'profile/create-profile.html')


def catalogue(request):
    return render(request, 'catalogue.html')


def plant_create(request):
    return render(request, 'plants/create-plant.html')


def plant_details(request, pk):
    return render(request, 'plants/plant-details.html')


def plant_edit(request, pk):
    return render(request, 'plants/edit-plant.html')


def plant_delete(request, pk):
    return render(request, 'plants/delete-plant.html')


def profile_details(request):
    return render(request, 'profile/profile-details.html')


def profile_edit(request):
    return render(request, 'profile/edit-profile.html')


def profile_delete(request):
    return render(request, 'profile/delete-profile.html')