from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from ..models import PredictionHistory
from ..serializers import PredictionHistorySerializer

class PredictionHistoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = PredictionHistory.objects.all()
    serializer_class = PredictionHistorySerializer
    permission_classes = [IsAuthenticated]

class PredictionHistoryListCreateView(ListCreateAPIView):
    queryset = PredictionHistory.objects.all()
    serializer_class = PredictionHistorySerializer
    permission_classes = [IsAuthenticated]

class PredictionHistorySearchView(ListAPIView):
    queryset = PredictionHistory.objects.all()
    serializer_class = PredictionHistorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['predicted_value', 'actual_value', 'date', 'error_margin']

