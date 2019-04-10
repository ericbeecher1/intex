from django.db import models
from django.contrib.auth.models import AbstractUser
from perscriptions import models as pmod


class User(AbstractUser):
    Perscriber = models.ForeignKey(pmod.Prescriber, on_delete=models.CASCADE, null=True)
