from django.urls import path, include
from rest_framework import routers

from teams.views import TeamViewSet, TaskViewSet

app_name = "teams_tasks"

router = routers.DefaultRouter()
router.register("teams", TeamViewSet)
router.register("tasks", TaskViewSet)

urlpatterns = [path("", include(router.urls))]
