from rest_framework import serializers

from teams.models import Team, Task
from user.serializers import UserSerializer


class TeamSerializer(serializers.ModelSerializer):
    tasks = serializers.IntegerField(read_only=True, source="tasks.count")
    people = serializers.IntegerField(read_only=True, source="users.count")

    class Meta:
        model = Team
        fields = ["id", "name", "date_of_establishment", "tasks", "people"]


class TeamRetrieveSerializer(TeamSerializer):
    tasks = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="title",
    )
    people = serializers.SerializerMethodField()

    def get_people(self, team: Team):
        return [f"{user.first_name} {user.last_name}" for user in team.users.all()]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "completed", "assigned_to", "teams"]


class TaskListSerializer(TaskSerializer):
    assigned_to = serializers.SerializerMethodField()
    teams = serializers.SlugRelatedField(
        read_only=True,
        slug_field="name",
    )

    class Meta:
        model = Task
        fields = ["id", "title", "completed", "assigned_to", "teams"]

    def get_assigned_to(self, task: Task):
        if task.assigned_to:
            return f"{task.assigned_to.first_name} {task.assigned_to.last_name}"
        return None
