from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Lunch, Appetizer, Beverages, Order, Menu
from datetime import date


class AddLunchForm(forms.ModelForm):
    class Meta:
        model = Lunch
        fields = '__all__'
        widgets = {'date': forms.DateInput(attrs={'type': 'date'})}


class AddAppetizerForm(forms.ModelForm):
    class Meta:
        model = Appetizer
        exclude = ['date']


class AddBeverageForm(forms.ModelForm):
    class Meta:
        model = Beverages
        fields = '__all__'


# class AddLunchDate(forms.ModelForm):
#     class Meta:
#         model = LunchDate
#         fields = '__all__'
#         widgets = {'date': forms.DateInput(attrs={'type': 'date'}),
#                    'lunch': forms.SelectMultiple}
#
#
# class AddAppetizerDate(forms.ModelForm):
#     class Meta:
#         model = AppetizerDate
#         fields = '__all__'
#         widgets = {'date': forms.DateInput(attrs={'type': 'date'}),
#                    'appetizer': forms.SelectMultiple}


class MenuForm(forms.ModelForm):
    date = forms.DateField(label='Data', widget=forms.DateInput(attrs={'type': 'date'}))
    lunch_meat = forms.ModelChoiceField(label='Lunch mięsny', queryset=Lunch.objects.filter(lunch_type='1'))
    lunch_vegetarian = forms.ModelChoiceField(label='Lunch wegetariański', queryset=Lunch.objects.filter(lunch_type='2'))
    lunch_vegan = forms.ModelChoiceField(label='Lunch wegański', queryset=Lunch.objects.filter(lunch_type='3'))
    salad = forms.ModelChoiceField(label='Sałatka', queryset=Appetizer.objects.filter(appetizer_type='1'))
    soup = forms.ModelChoiceField(label='Zupa', queryset=Appetizer.objects.filter(appetizer_type='2'))

    class Meta:
        model = Menu
        fields = ['date', 'lunch_meat', 'lunch_vegetarian', 'lunch_vegan', 'salad', 'soup']


# class OrderForm(forms.ModelForm):
#     today = date.today()
#     lunch = forms.ModelChoiceField(queryset=Lunch.objects.filter(order__date=today))
#
#     class Meta:
#         model = Order
#         fields = '__all__'





