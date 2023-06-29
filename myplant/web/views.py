from django.shortcuts import render, redirect

from myplant.web.forms import ProfileCreateForm, PlantCreateForm, PlantEditForm, PlantDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from myplant.web.models import Profile, Plant


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
    if get_profile() is not None:
        return redirect('index')
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
    }
    return render(request, 'profile/create-profile.html', context)


def catalogue(request):
    profile = get_profile()
    plants = Plant.objects.all()
    context = {
        'profile': profile,
        'plants': plants,
    }
    return render(request, 'catalogue.html', context)


def plant_create(request):
    if request.method == 'GET':
        plant = PlantCreateForm()
    else:
        plant = PlantCreateForm(request.POST)
        if plant.is_valid():
            plant.save()
            return redirect('catalogue')
    context = {
        'plant': plant,
    }
    return render(request, 'plants/create-plant.html', context)


def plant_details(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    context = {
        'plant': plant,
    }
    return render(request, 'plants/plant-details.html', context)


def plant_edit(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = PlantEditForm(instance=plant)
    else:
        form = PlantEditForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant,
    }
    return render(request, 'plants/edit-plant.html', context)


def plant_delete(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = PlantDeleteForm(instance=plant)
    else:
        form = PlantDeleteForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant,
    }
    return render(request, 'plants/delete-plant.html', context)


def profile_details(request):
    profile = get_profile()
    plants_count = Plant.objects.count()
    if plants_count == 0:
        number_of_stars = 0
    elif plants_count == 1:
        number_of_stars = 1
    elif plants_count == 2:
        number_of_stars = 2
    else:
        number_of_stars = 3
    context = {
        'profile': profile,
        'number_of_stars': number_of_stars,
    }
    return render(request, 'profile/profile-details.html', context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile/edit-profile.html', context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'profile/delete-profile.html', context)