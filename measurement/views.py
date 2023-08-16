# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from measurement.models import Measurement, Sensor
from measurement.serializers import SensorSerializer
from measurement.serializers import MeasurementSerializer, SensorDetailSerializer

class SensorViewSet(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorUpdateSet(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class MeasuremenViewSet(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

 

