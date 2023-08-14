from django.shortcuts import render
from .forms import *
import main_page.logic as logic
from main_page.m1_model import load_model
import pandas as pd


def main_page(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        floor = request.POST.get('floor')
        rooms_count = request.POST.get('rooms_count')
        living_space = request.POST.get('living_space')
        floor_count = request.POST.get('floor_count')
        metro = logic.underground_decoder(request.POST.get('metro'))
        district = logic.district_decoder(request.POST.get('district'))
        year_of_construction = request.POST.get('year_of_construction')
        if form.is_valid():

            data = {
                'floor': floor,
                'floors_count': floor_count,
                'rooms_count': rooms_count,
                'total_meters': living_space,
                'year_of_construction': year_of_construction,
                'district': district,
                'underground': metro
            }

            data = pd.DataFrame(data, index=[0])
            model = load_model()
            score = model.predict(data)
            temp = logic.get_integer_part(score[0])  # стоимость за кв м^2
            full_price = temp * float(living_space)
            full_price = int(full_price)
            str_score = logic.division_into_parts(temp)
            str_full_price = logic.division_into_parts(full_price)

            user_instance = form.save(commit=False)  # Create a User instance but don't save it yet
            user_instance.apartment_price = full_price
            user_instance.price_per_square = temp
            user_instance.save()

            context = {
                'score': str_score,
                'full_price': str_full_price,
                'error': True,
                'form': form
            }
            return render(request, 'main_page.html', context)

    else:
        form = UserForm()

        context = {
            'error': False,
            'error_text': 'Вы ввели номер телефона или почту не правильно',
            'form': form
        }

        return render(request, 'main_page.html', context)