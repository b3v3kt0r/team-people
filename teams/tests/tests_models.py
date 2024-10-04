from django.test import TestCase
from django.contrib.auth import get_user_model
from teams.models import Team, Task
from datetime import date

User = get_user_model()


class TeamModelTest(TestCase):

    def setUp(self):
        self.team = Team.objects.create(
            name="Development",
            date_of_establishment=date(2020, 1, 1)
        )

    def test_team_creation(self):
        """Test that a team can be successfully created"""
        self.assertEqual(self.team.name, "Development")
        self.assertEqual(self.team.date_of_establishment, date(2020, 1, 1))

    def test_team_str(self):
        """Test the __str__ method of the team model"""
        self.assertEqual(str(self.team), "Development")


class TaskModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="testuser@example.com",
            password="password123",
            first_name="John",
            last_name="Doe"
        )
        self.team = Team.objects.create(
            name="Development",
            date_of_establishment=date(2020, 1, 1)
        )
        self.task = Task.objects.create(
            title="Complete API",
            assigned_to=self.user,
            teams=self.team,
            completed=False
        )

    def test_task_creation(self):
        """Test that a task can be successfully created"""
        self.assertEqual(self.task.title, "Complete API")
        self.assertFalse(self.task.completed)
        self.assertEqual(self.task.assigned_to, self.user)
        self.assertEqual(self.task.teams, self.team)
