from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=70)
    address = models.CharField(max_length=50)
    phone = models.IntegerField()
    mail = models.EmailField()
    image = models.ImageField(blank=True, default='anonym.png')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


