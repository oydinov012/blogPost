from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15)
    photo = models.ImageField(default='media/profil.png',upload_to='profil_pic/')


    def __str__(self):
        return f"{self.username} {self.first_name}"