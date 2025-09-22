from django import forms
from .models import WeatherStation

class WeatherStationForm(forms.ModelForm):
    class Meta:
        model = WeatherStation
        fields = ['name', 'location', 'api_key']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Estación Central'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Madrid, España'
            }),
            'api_key': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa la clave API de tu estación'
            }),
        }