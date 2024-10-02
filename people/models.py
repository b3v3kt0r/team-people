from django.contrib.auth.models import AbstractUser
from django.db import models

from teams.models import Team


class Person(AbstractUser):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
