from rest_framework import serializers
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""
    _id = serializers.CharField(source='_id', read_only=False)

    class Meta:
        model = User
        fields = ['_id', 'email', 'username', 'first_name', 'last_name', 'created_at', 'updated_at']


class TeamSerializer(serializers.ModelSerializer):
    """Serializer for Team model"""
    _id = serializers.CharField(source='_id', read_only=False)

    class Meta:
        model = Team
        fields = ['_id', 'name', 'description', 'created_at', 'updated_at']


class ActivitySerializer(serializers.ModelSerializer):
    """Serializer for Activity model"""
    _id = serializers.CharField(source='_id', read_only=False)
    user_id = serializers.CharField()

    class Meta:
        model = Activity
        fields = ['_id', 'user_id', 'activity_type', 'duration', 'calories_burned', 'distance', 'created_at', 'updated_at']


class LeaderboardSerializer(serializers.ModelSerializer):
    """Serializer for Leaderboard model"""
    _id = serializers.CharField(source='_id', read_only=False)
    user_id = serializers.CharField()
    team_id = serializers.CharField()

    class Meta:
        model = Leaderboard
        fields = ['_id', 'user_id', 'team_id', 'total_points', 'rank', 'created_at', 'updated_at']


class WorkoutSerializer(serializers.ModelSerializer):
    """Serializer for Workout model"""
    _id = serializers.CharField(source='_id', read_only=False)

    class Meta:
        model = Workout
        fields = ['_id', 'title', 'description', 'difficulty', 'duration', 'exercises', 'created_at', 'updated_at']
