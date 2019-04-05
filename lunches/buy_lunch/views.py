from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required

from datetime import date
from django.db.models import Sum


from .models import Lunch, Appetizer, Beverages, Order, Points, Menu, LunchReview, MenuReview
from .forms import AddLunchForm, AddAppetizerForm, AddBeverageForm, MenuForm, ReviewMenuForm,UserRegisterForm


class ShowMenu(View):
    def get(self, request):
        today = date.today()
        try:
            menu = Menu.objects.get(date=today)
        except Menu.DoesNotExist:
            menu = None
        return render(request, 'index.html', {'menu': menu,
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


class MakeOrder(View):
    def get(self, request):
        today = date.today()
        lunch_meat = Lunch.objects.get(lunch_type=1, lunch_meat__date=today)
        lunch_vegetarian = Lunch.objects.get(lunch_type=2, lunch_vegetarian__date=today)
        lunch_vegan = Lunch.objects.get(lunch_type=3, lunch_vegan__date=today)

        salad = Appetizer.objects.get(appetizer_type=1, salad__date=today)
        soup = Appetizer.objects.get(appetizer_type=2, soup__date=today)

        beverages = Beverages.objects.all()

        count_points = Points.objects.filter(user=request.user).aggregate(Sum('amount'))
        all_points = count_points['amount__sum']

        return render(request, 'make_order.html', {'lunch_meat': lunch_meat,
                                                   'lunch_vegetarian': lunch_vegetarian,
                                                   'lunch_vegan': lunch_vegan,
                                                   'salad': salad,
                                                   'soup': soup,
                                                   'beverages': beverages,
                                                   'all_points': all_points})

    def post(self, request):
        lunch_selected = request.POST.get('lunch')
        lunch = Lunch.objects.get(id=lunch_selected)

        appetizer_selected = request.POST.get('appetizer')
        appetizer = Appetizer.objects.get(id=appetizer_selected)

        beverage_selected = request.POST.get('beverage')
        beverage = Beverages.objects.get(id=beverage_selected)

        final_price = lunch.lunch_price + appetizer.appetizer_price + beverage.beverage_price

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
        return redirect('user-orders')


class UserOrders(View):
    def get(self, request):
        orders = Order.objects.filter(user=request.user).order_by('-date')

        return render(request, 'user_orders.html', {'orders': orders})


class LunchCalendar(View):
    def get(self, request):
        menu = Menu.objects.all()
        return render(request, 'calendar.html', {'menu': menu})


class SetMenu(View):
    def get(self, request):
        form = MenuForm()
        return render(request, 'set_menu.html', {'form': form})

    def post(self, request):
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')


class EditMenu(View):
    def get(self, request, menu_id):
        menu = Menu.objects.get(id=menu_id)
        form = MenuForm(instance=menu)
        return render(request, 'edit_menu.html', {'form': form, 'menu': menu})

    def post(self, request, menu_id):
        menu = Menu.objects.get(id=menu_id)
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('index')


class ReviewOrder(View):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        form = ReviewMenuForm()
        return render(request, 'lunch_review.html', {'form': form, 'order': order})

    def post(self, request, order_id):
        order = Order.objects.get(id=order_id)
        form = ReviewMenuForm(request.POST)
        if form.is_valid():
            review = MenuReview.objects.create(user=request.user,
                                               menu=order,
                                               review=form.cleaned_data.get('review'),
                                               lunch_stars=form.cleaned_data.get('lunch_stars'),
                                               appetizer_stars=form.cleaned_data.get('appetizer_stars'))
            review.save()
            return redirect('user-orders')


class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            return redirect('login')


class AllOrders(View):
    def get(self, request):
        orders = Order.objects.all()
        return render(request, 'all_orders.html', {'orders': orders})


class DishRanking(View):
    def get(self, request):
        # reviews = MenuReview.objects.all()
        lunches = Lunch.objects.all().distinct()
        # appetizers = Appetizer.objects.all()
        return render(request, 'ranking.html', {'lunches': lunches})

# 'reviews': reviews