from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from ..models import StepRecord
from ..serializers import StepRecordSerializer

class StepRecordDetailView(RetrieveUpdateDestroyAPIView):
    queryset = StepRecord.objects.all()
    serializer_class = StepRecordSerializer
    permission_classes = [IsAuthenticated]

class StepRecordListCreateView(ListCreateAPIView):
    queryset = StepRecord.objects.all()
    serializer_class = StepRecordSerializer
    permission_classes = [IsAuthenticated]

class StepRecordSearchView(ListAPIView):
    queryset = StepRecord.objects.all()
    serializer_class = StepRecordSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['date', 'steps']
