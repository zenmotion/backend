from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from ..models import HealthReport
from ..serializers import HealthReportSerializer

class HealthReportDetailView(RetrieveUpdateDestroyAPIView):
    queryset = HealthReport.objects.all()
    serializer_class = HealthReportSerializer
    permission_classes = [AllowAny]

class HealthReportListCreateView(ListCreateAPIView):
    queryset = HealthReport.objects.all()
    serializer_class = HealthReportSerializer
    permission_classes = [AllowAny]

class HealthReportSearchView(ListAPIView):
    queryset = HealthReport.objects.all()
    serializer_class = HealthReportSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['summary', 'generated_at']
