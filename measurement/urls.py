from django.contrib import admin
from django.urls import path

from measurement.views import demo

# TODO: зарегистрируйте необходимые маршруты

from measurement.views import SensorViewSet, MeasuremenViewSet

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('demo/', demo),
    path('api/sensors/', SensorViewSet.as_view()),
    path('api/sensors/measurements/', MeasuremenViewSet.as_view()),
]