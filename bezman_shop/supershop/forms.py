from django.forms import ModelForm
from .models import *

class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'
        exclude = ['status', 'customer_order',]

