# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Measurement, Sensor
from measurement.serializers import SensorSerializer
from measurement.serializers import MeasurementSerializer, SensorDetailSerializer


# class SensorViewSet(RetrieveAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorSerializer

@api_view(['GET'])
def demo(request):
    data = {'message': 'Hello!'}
    return Response(data)

class SensorViewSet(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class MeasuremenViewSet(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = SensorDetailSerializer

 

