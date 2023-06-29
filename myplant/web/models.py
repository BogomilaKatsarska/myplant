from django.core.validators import MinLengthValidator
from django.db import models

from myplant.web.validators import validate_capitalized, validate_contains_only_letters


class Profile(models.Model):
    MAX_USERNAME_LEN = 10
    MAX_FIRST_NAME_LEN = 20
    MAX_LAST_NAME_LEN = 20
    MIN_USERNAME_LEN = 2

    username = models.CharField(
        max_length=MAX_USERNAME_LEN,
        validators=(
            MinLengthValidator(MIN_USERNAME_LEN),
        ),
        null=False,
        blank=False,
    )
    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LEN,
        null=False,
        blank=False,
        validators=(
            validate_capitalized,
        ),
    )
    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LEN,
        validators=(
            validate_capitalized,
        ),
        null=False,
        blank=False,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.username


class Plant(models.Model):
    OUTDOOR_PLANTS = 'Outdoor Plants'
    INDOOR_PLANTS = 'Indoor Plants'

    PLANTS = (
        (OUTDOOR_PLANTS, OUTDOOR_PLANTS),
        (INDOOR_PLANTS, INDOOR_PLANTS),
    )
    MAX_PLANT_TYPE_LEN = 14
    MAX_PLANT_NAME_LEN = 20
    MIN_PLANT_NAME_LEN = 2
    plant_type = models.CharField(
        max_length=MAX_PLANT_TYPE_LEN,
        null=False,
        blank=False,
        choices=PLANTS,
        verbose_name='Type',
    )
    name = models.CharField(
        max_length=MAX_PLANT_NAME_LEN,
        validators=(
            MinLengthValidator(MIN_PLANT_NAME_LEN),
            validate_contains_only_letters,
        ),
        null=False,
        blank=False,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name
