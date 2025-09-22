from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add_station, name='add_station'),
    path('delete/<int:station_id>/', views.delete_station, name='delete_station'),
]