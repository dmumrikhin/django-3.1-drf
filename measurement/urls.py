from django.contrib import admin
from django.urls import path

from measurement.views import SensorUpdateSet, demo

# TODO: зарегистрируйте необходимые маршруты

from measurement.views import SensorViewSet, MeasuremenViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', demo),
    path('sensors/', SensorViewSet.as_view()),
    path('sensors/<pk>/', SensorUpdateSet.as_view()),
    path('measurements/', MeasuremenViewSet.as_view()),
]