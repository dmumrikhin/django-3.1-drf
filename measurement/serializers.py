from rest_framework import serializers

# TODO: опишите необходимые сериализаторы
from measurement.models import Measurement, Sensor

class SensorSerializer(serializers.ModelSerializer): #простой сериализатор 1
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class MeasurementSerializer(serializers.ModelSerializer): #встраиваемая часть сер.2
    class Meta:
        model = Measurement
        fields = ['temperature', 'time']

class SensorDetailSerializer(serializers.ModelSerializer): #основная часть сер.2
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']