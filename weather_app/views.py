from django.shortcuts import render
from django.urls import reverse
import requests
from django.http import HttpResponseRedirect
from .forms import CityForm
from .models import City
from django.views.generic import ListView
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    city = City.objects.last()
    api_key = '6127731de6e35544bc6cacbc72858c77'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city.city_name}&appid={api_key}&units=metric'
    response = requests.get(url).json()
    context = {'temperature': response['main']['temp'],
               'icon': response['weather'][0]['icon'],
               'city_name': city.city_name,
               'form': form}

    return render(request,'weather_app/index.html',context=context)

class History(ListView):
    model = City
    template_name = 'weather_app/history.html'

def delete(request,id):
    city = City.objects.get(id=id)
    city.delete()
    return HttpResponseRedirect(reverse('weather_app:history'))



