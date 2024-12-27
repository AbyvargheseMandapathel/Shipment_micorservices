from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_first_category = models.BooleanField(default=False)
    is_second_category = models.BooleanField(default=False)
    is_third_category = models.BooleanField(default=False)
    is_fourth_category = models.BooleanField(default=False)

    def __str__(self):
        return self.username
