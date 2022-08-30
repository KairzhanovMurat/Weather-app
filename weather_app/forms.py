from django.forms import ModelForm,TextInput
from . import models

class CityForm(ModelForm):




    class Meta:
        model = models.City

        fields = ('city_name',)