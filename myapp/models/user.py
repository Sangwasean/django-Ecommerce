from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from myapp.validator import validate_password


class User(models.Model):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(max_length=100, unique=True, validators=[username_validator])
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100, validators=[validate_password])
    shipping_address = models.CharField(max_length=255, blank=True, null=True)

    # to save the data
    def register(self):
        self.save()

    @staticmethod
    def get_user_by_email(email):
        try:
            return User.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if User.objects.filter(email=self.email):
            return True

        return False