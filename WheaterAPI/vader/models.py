from django.db import models

# Create your models here.

class WeatherData(models.Model):
    temperature = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"WeatherData(temperature={self.temperature}, pressure={self.pressure}, humidity={self.humidity}, recorded_at={self.recorded_at})"
    