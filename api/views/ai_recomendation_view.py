from ..models import AIRecommendation
from ..serializers import AIRecommendationSerializer

from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class AIRecommendationDetailView(RetrieveUpdateDestroyAPIView):
    queryset = AIRecommendation.objects.all()
    serializer_class = AIRecommendationSerializer
    permission_classes = [IsAuthenticated]

class AIRecommendationListCreateView(ListCreateAPIView):
    queryset = AIRecommendation.objects.all()
    serializer_class = AIRecommendationSerializer
    permission_classes = [IsAuthenticated]

class AIRecommendationSearchView(ListAPIView):
    queryset = AIRecommendation.objects.all()
    serializer_class = AIRecommendationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['recommendation_type', 'recommendation_text', 'generated_at']
