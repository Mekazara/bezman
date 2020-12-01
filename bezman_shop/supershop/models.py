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

    def __str__(self):
        return self.name + ' ' + self.product_model


class Orders(models.Model):
    statuses = (
        ('New order', 'New order'),
        ('Not delivered', 'Not delivered'),
        ('In process', 'In process'),
        ('Delivered', 'Delivered')
    )
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=statuses, default='New order')

    def __str__(self):
        return self.product.name + ' ' + self.status


