from django.core.exceptions import ValidationError


def validate_height(value):
    if value > 240:
        raise ValidationError('Height greater than 240', params={'value': value})
