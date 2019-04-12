from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Lunch, Appetizer, Beverages, Order, Menu, MenuReview


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


class ReviewMenuForm(forms.ModelForm):
    class Meta:
        model = MenuReview
        fields = ['review', 'lunch_stars', 'appetizer_stars']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']