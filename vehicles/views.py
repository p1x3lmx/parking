from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Vehicle
from .forms import VehicleForm


def index(request):
    return render(request, 'vehicles/index.html')


def register_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicles:list_vehicles')
    else:
        form = VehicleForm()
    return render(request, 'vehicles/register_vehicle.html', {'form': form})


def list_vehicles(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles/list_vehicles.html', {'vehicles': vehicles})


def vehicle_details(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    form = VehicleForm(instance=vehicle)
    return render(request, 'vehicles/vehicle_details.html', {'form': form, 'vehicle': vehicle})


def edit_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicles:list_vehicles')
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'vehicles/edit_vehicle.html', {'form': form, 'vehicle': vehicle})


def view_vehicle_details(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    return render(request, 'vehicles/vehicle_details.html', {'vehicle': vehicle})
