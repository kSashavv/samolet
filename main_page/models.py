from django.core.validators import RegexValidator
from django.db import models


class User(models.Model):
    EVOLUTION_TYPE = (
        ('like', 'Цена понравилась'),
        ('dislike', 'Цена не понравилась'),
    )

    first_name = models.CharField(max_length=100,)
    email = models.EmailField()
    phone_regex = RegexValidator(
        regex=r'^\+7\d{10}$',
        message="Номер телефона должен быть в формате: '+799999999'."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=12)
    apartment_price = models.CharField(max_length=100)
    price_per_square = models.CharField(max_length=100)
    floor = models.CharField(max_length=3)
    rooms_count = models.CharField(max_length=100)
    living_space = models.CharField(max_length=100)
    floor_count = models.CharField(max_length=3)
    metro = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    year_of_construction = models.CharField(max_length=4)

    def __str__(self):
        return f'{self.first_name} '


class District(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'
