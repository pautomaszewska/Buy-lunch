from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date
from django.db.models import Sum


from .models import Lunch, Appetizer, Beverages, Order, Points
from .forms import AddLunchForm, AddAppetizerForm, AddBeverageForm, AddLunchDate, AddAppetizerDate


class ShowMenu(View):
    def get(self, request):
        lunches = Lunch.objects.filter(lunchdate__date=date.today()).order_by('type')
        appetizers = Appetizer.objects.filter(appetizerdate__date=date.today())
        today = date.today()
        return render(request, 'index.html', {'lunches': lunches,
                                              'appetizers': appetizers,
                                              'today': today})


class AddLunch(View):
    def get(self, request):
        form = AddLunchForm()
        return render(request, 'add_lunch.html', {'form': form})

    def post(self, request):
        form = AddLunchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')


class AddAppetizer(View):
    def get(self, request):
        form = AddAppetizerForm()
        return render(request, 'add_appetizer.html', {'form': form})

    def post(self, request):
        form = AddAppetizerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')


class AddBeverage(View):
    def get(self, request):
        form = AddBeverageForm()
        return render(request, 'add_beverage.html', {'form': form})

    def post(self, request):
        form = AddBeverageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')


class ShowLunches(View):
    def get(self, request):
        lunches = Lunch.objects.all()
        return render(request, 'show_lunches.html', {'lunches': lunches})


class ShowLAppetizers(View):
    def get(self, request):
        appetizers = Appetizer.objects.all()
        return render(request, 'show_appetizers.html', {'appetizers': appetizers})


class ShowBeverages(View):
    def get(self, request):
        beverages = Beverages.objects.all()
        return render(request, 'show_beverages.html', {'beverages': beverages})


class SetLunchDate(View):
    def get(self, request):
        form = AddLunchDate()
        return render(request, 'set_lunch_date.html', {'form': form})

    def post(self, request):
        form = AddLunchDate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')


class SetAppetizerDate(View):
    def get(self, request):
        form = AddAppetizerDate()
        return render(request, 'set_appetizer_date.html', {'form': form})

    def post(self, request):
        form = AddAppetizerDate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')


class MakeOrder(View):
    def get(self, request):
        lunch_meat = Lunch.objects.get(lunchdate__date=date.today(), type=1)
        lunch_vegetarian = Lunch.objects.get(lunchdate__date=date.today(), type=2)
        lunch_vegan = Lunch.objects.get(lunchdate__date=date.today(), type=3)

        appetizer_soup = Appetizer.objects.get(appetizerdate__date=date.today(), type=1)
        appetizer_salad = Appetizer.objects.get(appetizerdate__date=date.today(), type=2)

        beverages = Beverages.objects.all()

        count_points = Points.objects.filter(user=request.user).aggregate(Sum('amount'))
        all_points = count_points['amount__sum']

        return render(request, 'make_order.html', {'lunch_meat': lunch_meat,
                                                   'lunch_vegetarian': lunch_vegetarian,
                                                   'lunch_vegan': lunch_vegan,
                                                   'appetizer_soup': appetizer_soup,
                                                   'appetizer_salad': appetizer_salad,
                                                   'beverages': beverages,
                                                   'all_points': all_points})

    def post(self, request):
        lunch_selected = request.POST.get('lunch')
        lunch = Lunch.objects.get(id=lunch_selected)

        appetizer_selected = request.POST.get('appetizer')
        appetizer = Appetizer.objects.get(id=appetizer_selected)

        beverage_selected = request.POST.get('beverage')
        beverage = Beverages.objects.get(id=beverage_selected)

        final_price = lunch.price + appetizer.price + beverage.price

        points_collected = int(final_price/10)

        all_points = Points.objects.filter(user=request.user).aggregate()

        if final_price > 10:
            user_points = Points.objects.create(user=self.request.user, amount=points_collected)

        order = Order.objects.create(lunch=lunch,
                                     appetizer=appetizer,
                                     beverage=beverage,
                                     final_price=final_price,
                                     points=user_points,
                                     points_collected=points_collected,
                                     user=self.request.user,
                                     )
        order.save()
        return HttpResponse('zamówienie złożone')




