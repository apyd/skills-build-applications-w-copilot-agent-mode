from django.db import models
from django.contrib.auth.models import AbstractUser
from bson import ObjectId


class User(models.Model):
    """User model for OctoFit Tracker"""
    _id = models.CharField(max_length=24, primary_key=True, default=lambda: str(ObjectId()))
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username


class Team(models.Model):
    """Team model for OctoFit Tracker"""
    _id = models.CharField(max_length=24, primary_key=True, default=lambda: str(ObjectId()))
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class Activity(models.Model):
    """Activity model for OctoFit Tracker"""
    _id = models.CharField(max_length=24, primary_key=True, default=lambda: str(ObjectId()))
    user_id = models.CharField(max_length=24)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    calories_burned = models.FloatField()
    distance = models.FloatField()  # in km
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'activities'

    def __str__(self):
        return f"{self.activity_type} - {self.user_id}"


class Leaderboard(models.Model):
    """Leaderboard model for OctoFit Tracker"""
    _id = models.CharField(max_length=24, primary_key=True, default=lambda: str(ObjectId()))
    user_id = models.CharField(max_length=24)
    team_id = models.CharField(max_length=24)
    total_points = models.IntegerField()
    rank = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'leaderboard'

    def __str__(self):
        return f"{self.user_id} - Rank: {self.rank}"


class Workout(models.Model):
    """Workout model for OctoFit Tracker"""
    _id = models.CharField(max_length=24, primary_key=True, default=lambda: str(ObjectId()))
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=20)
    duration = models.IntegerField()  # in minutes
    exercises = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return self.title
