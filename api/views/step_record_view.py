from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from ..models import StepRecord
from ..serializers import StepRecordSerializer

class StepRecordDetailView(RetrieveUpdateDestroyAPIView):
    queryset = StepRecord.objects.all()
    serializer_class = StepRecordSerializer
    permission_classes = [AllowAny]

class StepRecordListCreateView(ListCreateAPIView):
    queryset = StepRecord.objects.all()
    serializer_class = StepRecordSerializer
    permission_classes = [AllowAny]

class StepRecordSearchView(ListAPIView):
    queryset = StepRecord.objects.all()
    serializer_class = StepRecordSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['date', 'steps']
