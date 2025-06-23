import django_filters
from .models import Meal, Workout

class MealFilter(django_filters.FilterSet):
    recorded_at = django_filters.DateFilter(field_name='recorded_at', lookup_expr='date')
    user = django_filters.NumberFilter(field_name='user')
    class Meta:
        model = Meal
        fields = ['user', 'recorded_at']

class WorkoutFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(field_name='date', lookup_expr='date')
    user = django_filters.NumberFilter(field_name='user')
    class Meta:
        model = Workout
        fields = ['user', 'date']
