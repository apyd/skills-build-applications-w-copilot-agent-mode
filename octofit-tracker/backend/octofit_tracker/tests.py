from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(
            email='test@example.com',
            username='testuser',
            first_name='Test',
            last_name='User',
            password='testpass123'
        )
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(
            name='Test Team',
            description='A test team.'
        )
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(
            user_id='dummyid',
            activity_type='Running',
            duration=30,
            calories_burned=300.0,
            distance=5.0
        )
        self.assertEqual(activity.activity_type, 'Running')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(
            user_id='dummyid',
            team_id='dummyteam',
            total_points=100,
            rank=1
        )
        self.assertEqual(leaderboard.rank, 1)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(
            title='Test Workout',
            description='A test workout.',
            difficulty='Easy',
            duration=20,
            exercises=[{'name': 'Pushups', 'reps': 10, 'sets': 2}]
        )
        self.assertEqual(workout.title, 'Test Workout')
