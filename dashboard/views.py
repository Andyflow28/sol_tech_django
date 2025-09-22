from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import WeatherStation
from .forms import WeatherStationForm  # Solo importar WeatherStationForm

@login_required
def dashboard(request):
    stations = WeatherStation.objects.filter(user=request.user, is_active=True)
    return render(request, 'dashboard/dashboard.html', {'stations': stations})

@login_required
def add_station(request):
    if request.method == 'POST':
        form = WeatherStationForm(request.POST)
        if form.is_valid():
            station = form.save(commit=False)
            station.user = request.user
            station.save()
            return redirect('dashboard')
    else:
        form = WeatherStationForm()
    return render(request, 'dashboard/add_station.html', {'form': form})

@login_required
def delete_station(request, station_id):
    station = get_object_or_404(WeatherStation, id=station_id, user=request.user)
    if request.method == 'POST':
        station.is_active = False
        station.save()
        return redirect('dashboard')
    return render(request, 'dashboard/delete_station.html', {'station': station})