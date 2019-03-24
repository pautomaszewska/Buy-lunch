from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Lunch, Appetizer, Beverages, Order, LunchDate, AppetizerDate


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


class AddLunchDate(forms.ModelForm):
    class Meta:
        model = LunchDate
        fields = '__all__'
        widgets = {'date': forms.DateInput(attrs={'type': 'date'}),
                   'lunch': forms.SelectMultiple}


class AddAppetizerDate(forms.ModelForm):
    class Meta:
        model = AppetizerDate
        fields = '__all__'
        widgets = {'date': forms.DateInput(attrs={'type': 'date'}),
                   'appetizer': forms.SelectMultiple}
