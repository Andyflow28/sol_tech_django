# dashboard/models.py
from django.db import models
from django.contrib.auth.models import User

class WeatherStation(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre de la estación")
    location = models.CharField(max_length=200, verbose_name="Ubicación")
    api_key = models.CharField(max_length=100, unique=True, verbose_name="Clave API")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stations")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name