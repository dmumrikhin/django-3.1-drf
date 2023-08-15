from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=30)#, verbose_name='Название')
    description = models.CharField(max_length=255)#, verbose_name='Описание')

    # class Meta:
    #     verbose_name = 'Датчик'
    #     verbose_name_plural = 'Датчики'

    # def __str__(self):
    #     return self.name
    
class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=3, decimal_places=2, 
                                      verbose_name='Температура')
    time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'

    def __str__(self):
        return self.name
