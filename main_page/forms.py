from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['evolution_type', 'apartment_price', 'price_per_square']
        labels = {
            'first_name': 'Имя',
            'email': 'Email',
            'phone_number': 'Номер телефона',
            'apartment_price': 'Автор',
            'floor': 'Этаж',
            'rooms_count': 'Кол-во комнат',
            'living_space': 'Площадь',
            'floor_count': 'Кол-во этажей',
            'metro': 'Метро',
            'district': 'Район',
            'year_of_construction': 'Год постройки'
        }
