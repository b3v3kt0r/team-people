from django.shortcuts import render
from rest_framework import viewsets

from teams.models import Team, Task
from teams.serializers import TeamSerializer, TaskSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

