from django.shortcuts import render
from .forms import *
from main_page.models import User
import main_page.logic as logic
from main_page.m1_model import load_model
import pandas as pd


def main_page(request):
    form = UserForm

    context = {
        'error': False,
        'error_text': 'Вы ввели данные не прваильно',
        'score': False,
        'form': form
    }

    return render(request, 'main_page.html', context)


def calculate(request):
    if request.method == 'POST':
        form = UserForm
        floor = request.POST.get('floor')
        rooms_count = request.POST.get('rooms_count')
        living_space = request.POST.get('living_space')
        floor_count = request.POST.get('floor_count')
        metro = logic.underground_decoder(request.POST.get('metro'))
        district = logic.district_decoder(request.POST.get('district'))
        year_of_construction = request.POST.get('year_of_construction')
        if form.is_valid():
            form.save()
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
            User.objects.create(apartment_price=full_price,
                                price_per_square =temp
            )
            context = {
                'score': str_score,
                'full_price': str_full_price,
                'error': True
            }
            return render(request, 'main_page.html', context)

    else:
        form = UserForm
        context = {
            'error': False,
            'error_text': 'Вы ввели номер телефона или почту не правильно',
            'form': form
        }
        return render(request, 'main_page.html', context)










    # if request.method == 'POST':
    #     mail = request.POST.get('mail')
    #     phone_number = request.POST.get('phone_number')
    #     name = request.POST.get('name')
    #     floor = request.POST.get('floor')
    #     rooms_count = request.POST.get('rooms_count')
    #     living_space = request.POST.get('living_space')
    #     floor_count = request.POST.get('floor_count')
    #     metro = logic.underground_decoder(request.POST.get('metro'))
    #     district = logic.district_decoder(request.POST.get('district'))
    #     year_of_construction = request.POST.get('year_of_construction')
    #     if logic.ads_number(floor) and logic.ads_number(rooms_count) and logic.ads_number(
    #             living_space) and logic.ads_number(floor_count) and logic.ads_number(year_of_construction):
    #         if metro and district:
    #             if logic.is_number_valid(phone_number) and logic.is_mail_valid(mail):
    #                 User.objects.create(first_name=name,
    #                                     email=mail,
    #                                     phone_number=phone_number,
    #                                     floor=floor,
    #                                     rooms_count=rooms_count,
    #                                     living_space=living_space,
    #                                     floor_count=floor_count,
    #                                     metro=metro,
    #                                     district=district,
    #                                     year_of_construction=year_of_construction)
    #                 data = {
    #                     'floor': floor,
    #                     'floors_count': floor_count,
    #                     'rooms_count': rooms_count,
    #                     'total_meters': living_space,
    #                     'year_of_construction': year_of_construction,
    #                     'district': district,
    #                     'underground': metro
    #                 }
    #                 data = pd.DataFrame(data, index=[0])
    #                 model = load_model()
    #                 score = model.predict(data)
    #                 temp = logic.get_integer_part(score[0])  # стоимость
    #                 print(type(temp))
    #                 full_price = temp * float(living_space)
    #                 full_price = int(full_price)
    #                 str_score = logic.division_into_parts(temp)
    #                 str_full_price = logic.division_into_parts(full_price)
    #                 return render(request, 'main_page.html',
    #                               {'score': str_score, 'full_price': str_full_price, 'error': True})
    #             else:
    #                 return render(request, 'main_page.html',
    #                               {'error': False, 'error_text': 'Вы ввели номер телефона или почту не правильно'})
    #
    #         return render(request, 'main_page.html',
    #                       {'error': False, 'error_text': 'Вы ввели метро или район не прваильно'})
    #
    #     return render(request, 'main_page.html',
    #                   {'error': False, 'error_text': 'Вы ввели параметры квартиры не правильно'})
    #
    # return render(request, 'main_page.html', {'error': False})
