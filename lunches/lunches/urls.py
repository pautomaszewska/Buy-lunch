"""lunches URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from .settings import MEDIA_ROOT, MEDIA_URL


from buy_lunch.views import ShowMenu, AddLunch, AddAppetizer, AddBeverage, ShowLunches, ShowLAppetizers, ShowBeverages,\
    SetLunchDate, SetAppetizerDate, MakeOrder, UserOrders, LunchCalendar, SetMenu, ReviewLunch

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

    path('', ShowMenu.as_view(), name='index'),
    path('add-lunch/', AddLunch.as_view(), name='add-lunch'),
    path('add-appetizer/', AddAppetizer.as_view(), name='add-appetizer'),
    path('add-beverage/', AddBeverage.as_view(), name='add-beverage'),
    path('lunches/', ShowLunches.as_view(), name='lunches'),
    path('appetizers/', ShowLAppetizers.as_view(), name='appetizers'),
    path('beverages/', ShowBeverages.as_view(), name='beverages'),
    path('set-lunch-date/', SetLunchDate.as_view(), name='set-lunch-date'),
    path('set-appetizer-date/', SetAppetizerDate.as_view(), name='set-appetizer-date'),
    path('make-order/', MakeOrder.as_view(), name='make-order'),
    path('user-orders/', UserOrders.as_view(), name='user-orders'),
    path('lunch-calendar/', LunchCalendar.as_view(), name='lunch-calendar'),
    path('set-menu/', SetMenu.as_view(), name='set-menu'),
    path('lunch-review/<int:lunch_id>', ReviewLunch.as_view(), name='lunch-review'),



    ] + static(MEDIA_URL, document_root=MEDIA_ROOT)
