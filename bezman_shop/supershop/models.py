from django.db import models


class Product(models.Model):
    types = (('classic', 'classic'),
             ('sport', 'sport'),
             ('dm', 'demi-season'),
             ('winter', 'winter'),
             )
    genders = (('female', 'female'),
              ('male', 'male'),
              ('uni', 'uni'),
              )
    sizes = (('small', 'child'),
             ('medium', 'medium'),
             ('large', 'large'),
             ('XL', 'XL'))
    name = models.CharField(max_length=40)
    product_type = models.CharField(max_length=40, choices=types)
    gender = models.CharField(max_length=20, choices=genders)
    product_model = models.CharField(max_length=20)
    price = models.IntegerField()
    manufactured = models.CharField(max_length=50)
    size = models.CharField(max_length=20, choices=sizes)
    image = models.ImageField(blank=True, default='default.png')

