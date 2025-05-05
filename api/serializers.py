from rest_framework import serializers
from .models import (
    User, Workout, AIRecommendation, Meal, Goal, HealthReport,
    StepRecord, Notification, UserPreferences, PredictionHistory
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['created_at']


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'
        read_only_fields = ['date']


class AIRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIRecommendation
        fields = '__all__'
        read_only_fields = ['generated_at']


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'
        read_only_fields = ['recorded_at']


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'


class HealthReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthReport
        fields = '__all__'
        read_only_fields = ['generated_at']


class StepRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepRecord
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
        read_only_fields = ['created_at']


class UserPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPreferences
        fields = '__all__'


class PredictionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionHistory
        fields = '__all__'
        read_only_fields = ['predicted_at']
