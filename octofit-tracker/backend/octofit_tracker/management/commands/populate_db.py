from django.core.management.base import BaseCommand
from django.utils import timezone
from bson import ObjectId
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        """Populate the database with superhero test data"""
        self.stdout.write(self.style.SUCCESS('Starting database population...'))

        # Delete existing data
        self.stdout.write('Deleting existing data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            _id=str(ObjectId()),
            name='Team Marvel',
            description='Avengers and Marvel superheroes'
        )
        team_dc = Team.objects.create(
            _id=str(ObjectId()),
            name='Team DC',
            description='Justice League and DC superheroes'
        )

        # Create users (superheroes)
        self.stdout.write('Creating users...')
        users_data = [
            {
                'email': 'batman@dc.com',
                'username': 'batman',
                'first_name': 'Bruce',
                'last_name': 'Wayne',
                'team': team_dc,
            },
            {
                'email': 'superman@dc.com',
                'username': 'superman',
                'first_name': 'Clark',
                'last_name': 'Kent',
                'team': team_dc,
            },
            {
                'email': 'wonderwoman@dc.com',
                'username': 'wonderwoman',
                'first_name': 'Diana',
                'last_name': 'Prince',
                'team': team_dc,
            },
            {
                'email': 'ironman@marvel.com',
                'username': 'ironman',
                'first_name': 'Tony',
                'last_name': 'Stark',
                'team': team_marvel,
            },
            {
                'email': 'captainamerica@marvel.com',
                'username': 'captainamerica',
                'first_name': 'Steve',
                'last_name': 'Rogers',
                'team': team_marvel,
            },
            {
                'email': 'thor@marvel.com',
                'username': 'thor',
                'first_name': 'Thor',
                'last_name': 'Odinson',
                'team': team_marvel,
            },
        ]

        users = []
        for user_data in users_data:
            team = user_data.pop('team')
            user = User.objects.create(
                _id=str(ObjectId()),
                password='hashed_password_123',
                **user_data
            )
            users.append((user, team))
            self.stdout.write(f'  Created user: {user.username}')

        # Create activities
        self.stdout.write('Creating activities...')
        for user, team in users:
            Activity.objects.create(
                _id=str(ObjectId()),
                user_id=user._id,
                activity_type='Running',
                duration=45,
                calories_burned=500.0,
                distance=7.5
            )
            Activity.objects.create(
                _id=str(ObjectId()),
                user_id=user._id,
                activity_type='Gym',
                duration=60,
                calories_burned=600.0,
                distance=0.0
            )

        # Create leaderboard entries
        self.stdout.write('Creating leaderboard entries...')
        rank = 1
        for user, team in users:
            Leaderboard.objects.create(
                _id=str(ObjectId()),
                user_id=user._id,
                team_id=team._id,
                total_points=1000 - (rank * 50),
                rank=rank
            )
            rank += 1

        # Create workouts
        self.stdout.write('Creating workouts...')
        workouts_data = [
            {
                'title': 'Superhero Strength Training',
                'description': 'An intense workout to build superhero strength',
                'difficulty': 'Hard',
                'duration': 90,
                'exercises': [
                    {'name': 'Bench Press', 'reps': 10, 'sets': 4},
                    {'name': 'Squats', 'reps': 12, 'sets': 4},
                    {'name': 'Deadlifts', 'reps': 8, 'sets': 3},
                ],
            },
            {
                'title': 'Cardio Power Session',
                'description': 'Get your heart pumping like a superhero',
                'difficulty': 'Medium',
                'duration': 45,
                'exercises': [
                    {'name': 'Treadmill Run', 'duration': 20, 'intensity': 'High'},
                    {'name': 'Jump Rope', 'duration': 10, 'sets': 3},
                    {'name': 'Burpees', 'reps': 20, 'sets': 3},
                ],
            },
            {
                'title': 'Flexibility and Core',
                'description': 'Improve flexibility and core strength',
                'difficulty': 'Easy',
                'duration': 30,
                'exercises': [
                    {'name': 'Yoga Stretches', 'duration': 15},
                    {'name': 'Plank', 'duration': 5, 'sets': 3},
                    {'name': 'Core Rotations', 'reps': 20, 'sets': 2},
                ],
            },
        ]

        for workout_data in workouts_data:
            Workout.objects.create(
                _id=str(ObjectId()),
                **workout_data
            )
            self.stdout.write(f'  Created workout: {workout_data["title"]}')

        self.stdout.write(self.style.SUCCESS('Database population completed successfully!'))
