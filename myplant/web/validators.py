from django.core.exceptions import ValidationError


def validate_capitalized(value):
    if value != value.capitalize():
        raise ValidationError('Your name must start with a capital letter!')


def validate_contains_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Plant name should contain only letters!')