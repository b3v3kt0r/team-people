from django.test import TestCase
from teams.models import Team, Task
from user.models import User
from teams.serializers import (
    TaskSerializer,
    TaskListSerializer
)
from datetime import date


class TeamSerializerTest(TestCase):

    def setUp(self):
        self.team = Team.objects.create(
            name="Development",
            date_of_establishment=date(2020, 1, 1)
        )
        self.user = User.objects.create_user(
            email="testuser@example.com",
            password="password123",
            first_name="John",
            last_name="Doe"
        )
        self.task = Task.objects.create(
            title="Complete API",
            assigned_to=self.user,
            teams=self.team,
            completed=False
        )


class TaskSerializerTest(TestCase):

    def setUp(self):
        self.team = Team.objects.create(
            name="Development",
            date_of_establishment=date(2020, 1, 1)
        )
        self.user = User.objects.create_user(
            email="testuser@example.com",
            password="password123",
            first_name="John",
            last_name="Doe"
        )
        self.task = Task.objects.create(
            title="Complete API",
            assigned_to=self.user,
            teams=self.team,
            completed=False
        )

    def test_task_serializer(self):
        """Test TaskSerializer fields"""
        serializer = TaskSerializer(self.task)
        expected_data = {
            "id": self.task.id,
            "title": "Complete API",
            "completed": False,
            "assigned_to": self.user.id,
            "teams": self.team.id
        }
        self.assertEqual(serializer.data, expected_data)

    def test_task_list_serializer(self):
        """Test TaskListSerializer fields"""
        serializer = TaskListSerializer(self.task)
        expected_data = {
            "id": self.task.id,
            "title": "Complete API",
            "completed": False,
            "assigned_to": "John Doe",  # Full name of user
            "teams": "Development"  # Team name
        }
        self.assertEqual(serializer.data, expected_data)
