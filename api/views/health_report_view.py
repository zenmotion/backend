from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from ..models import HealthReport
from ..serializers import HealthReportSerializer

class HealthReportDetailView(RetrieveUpdateDestroyAPIView):
    queryset = HealthReport.objects.all()
    serializer_class = HealthReportSerializer
    permission_classes = [IsAuthenticated]

class HealthReportListCreateView(ListCreateAPIView):
    queryset = HealthReport.objects.all()
    serializer_class = HealthReportSerializer
    permission_classes = [IsAuthenticated]

class HealthReportSearchView(ListAPIView):
    queryset = HealthReport.objects.all()
    serializer_class = HealthReportSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['summary', 'generated_at']
