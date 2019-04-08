from django import forms
from django.forms import SelectDateWidget
from .widgets import AjaxInputWidget
from .models import City


class SearchTicket(forms.Form):
    city_of_departure = forms.CharField(label='Город отправления', widget=AjaxInputWidget(url='api/city_ajax', attrs={'class': 'inline right-margin'}))
    arrival_city = forms.ModelChoiceField(label='Город прибытия', queryset=City.objects.all())
    date = forms.DateField(label='Дата', widget=SelectDateWidget())
