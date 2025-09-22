from django.contrib import admin
from .models import WeatherStation

@admin.register(WeatherStation)
class WeatherStationAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'location', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'user__username', 'location')