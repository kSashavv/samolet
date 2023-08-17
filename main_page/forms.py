from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone_number', 'email', 'first_name', 'floor', 'floor_count', 'year_of_construction', 'rooms_count',
                  'living_space', 'metro', 'district']
        exclude = ['evolution_type', 'apartment_price', 'price_per_square']
        widgets = {
            'email': forms.TextInput(attrs={'type': 'email', 'placeholder': 'Email', }),
            'phone_number': forms.TextInput(
                attrs={'type': 'tel', 'placeholder': 'Номер телефона', 'pattern': '^\+7\d{10}$'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'floor': forms.TextInput(attrs={'type': 'number', 'placeholder': 'Этаж'}),
            'floor_count': forms.TextInput(attrs={'type': 'number', 'placeholder': 'Кол-во Этажей'}),
            'year_of_construction': forms.TextInput(attrs={'type': 'number', 'placeholder': 'Год постройки'}),
            'rooms_count': forms.TextInput(attrs={'placeholder': 'Кол-во комнат', 'type': 'number'}),
            'living_space': forms.TextInput(attrs={'type': 'number', 'placeholder': 'Площадь'}),
            'metro': forms.TextInput(attrs={'placeholder': 'Метро'}),
            'district': forms.TextInput(attrs={'placeholder': 'Район'}),

        }
        labels = {
            'first_name': '',
            'email': '',
            'phone_number': 'Номер телефона',
            'floor': '',
            'floor_count': '',
            'rooms_count': '',
            'living_space': '',
            'year_of_construction': '',
            'metro': '',
            'district': '',
        }
