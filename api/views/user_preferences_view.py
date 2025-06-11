from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from ..models import UserPreferences
from ..serializers import UserPreferencesSerializer

class UserPreferencesDetailView(RetrieveUpdateDestroyAPIView):
    queryset = UserPreferences.objects.all()
    serializer_class = UserPreferencesSerializer
    permission_classes = [AllowAny]

class UserPreferencesListCreateView(ListCreateAPIView):
    queryset = UserPreferences.objects.all()
    serializer_class = UserPreferencesSerializer
    permission_classes = [AllowAny]

class UserPreferencesSearchView(ListAPIView):
    queryset = UserPreferences.objects.all()
    serializer_class = UserPreferencesSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['preferred_goal_type', 'preferred_meal_type', 'notifications_enabled']
