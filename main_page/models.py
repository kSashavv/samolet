from django.db import models


class User(models.Model):
    EVOLUTION_TYPE = (
        ('like', 'Цена понравилась'),
        ('dislike', 'Цена не понравилась'),
    )

    first_name = models.CharField(max_length=100,)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    apartment_price = models.CharField(max_length=100, null=True)
    price_per_square = models.CharField(max_length=100, null=True)
    floor = models.CharField(max_length=3, null=True)
    rooms_count = models.CharField(max_length=100, null=True)
    living_space = models.CharField(max_length=100, null=True)
    floor_count = models.CharField(max_length=3, null=True)
    metro = models.CharField(max_length=100, null=True)
    district = models.CharField(max_length=100, null=True)
    evolution_type = models.CharField(max_length=20, choices=EVOLUTION_TYPE, null=True)
    year_of_construction = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.first_name} '


class District(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'
