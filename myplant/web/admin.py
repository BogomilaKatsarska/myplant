from django.contrib import admin
from myplant.web.models import Plant, Profile


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
