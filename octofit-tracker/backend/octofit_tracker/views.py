from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.serializers import (
    UserSerializer, TeamSerializer, ActivitySerializer,
    LeaderboardSerializer, WorkoutSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet for User model"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """ViewSet for Team model"""
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """ViewSet for Activity model"""
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class LeaderboardViewSet(viewsets.ModelViewSet):
    """ViewSet for Leaderboard model"""
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    """ViewSet for Workout model"""
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


@api_view(['GET'])
def api_root(request):
    """API root endpoint"""
    return Response({
        'message': 'Welcome to OctoFit Tracker API',
        'endpoints': {
            'users': request.build_absolute_uri('/api/users/'),
            'teams': request.build_absolute_uri('/api/teams/'),
            'activities': request.build_absolute_uri('/api/activities/'),
            'leaderboard': request.build_absolute_uri('/api/leaderboard/'),
            'workouts': request.build_absolute_uri('/api/workouts/'),
        }
    })
