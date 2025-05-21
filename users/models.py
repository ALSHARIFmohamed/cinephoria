from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_client = models.BooleanField(default=False)
    is_staff_member = models.BooleanField(default=False)  # pour distinguer les employés
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username

    