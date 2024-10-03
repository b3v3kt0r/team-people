from django.shortcuts import render
from rest_framework import viewsets

from teams.models import Team, Task
from teams.serializers import TeamSerializer, TaskSerializer, TaskListSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return TaskListSerializer
        else:
            return TaskSerializer
