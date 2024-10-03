from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from teams.filters import TeamFilter
from teams.models import Team, Task
from teams.serializers import (
    TeamSerializer,
    TaskSerializer,
    TaskListSerializer
)


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TeamFilter


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return TaskListSerializer
        else:
            return TaskSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ["list", "retrieve"]:
            return self.queryset.select_related()
        return queryset
