from django.conf import settings
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    date_of_establishment = models.DateField()

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tasks")
    teams = models.ManyToManyField(Team, related_name="tasks")
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}. Responsible: {self.assigned_to.name}. Completed: {self.completed}"
