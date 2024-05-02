from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

def validate_password(value):
    if len(value) < 8:
        raise ValidationError(
            _("The password must be at least 8 characters long."),
            code='password_too_short',
        )
    if not any(char.isdigit() for char in value):
        raise ValidationError(
            _("The password must contain at least one digit."),
            code='password_no_digit',
        )
    if not any(char.isalnum() for char in value):
        raise ValidationError(
            _("The password must contain at least one alphanumeric character."),
            code='password_no_alphanumeric',
        )
