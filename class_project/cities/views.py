from django.shortcuts import render, get_object_or_404, redirect
from .models import City
from .CityForms import CityForm

def home(request):
    cities = City.objects.all()
    return render(request, 'Cities.html', context={'cities': cities})

def city(request, pk):
    city = get_object_or_404(City, pk=pk)
    return render(request, 'city.html', context={'city': city})

def create_city(request):
    if request.method == 'POST':
        cityform = CityForm(request.POST)
        if cityform.is_valid():
            cityform.save()
            return redirect('home')
    return render(request, 'create_city.html', context={'form': CityForm})

def update_city(request, pk):
    city = get_object_or_404(City, pk=pk)
    if request.method == 'POST':
        cityform = CityForm(request.POST, instance=city)
        if cityform.is_valid():
            cityform.save()
            return redirect('home')
    return render(request, 'update_city.html', context={'form': CityForm(instance=city)})

def delete_city(request, pk):
    city = get_object_or_404(City, pk=pk)
    city.delete()
    return redirect('home')