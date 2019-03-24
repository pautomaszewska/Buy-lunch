from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User


LUNCH_TYPE = ((1, 'mięsny'),
              (2, 'wegetariański'),
              (3, 'wegański'))

APPETIZER_TYPE = ((1, 'sałatka'),
                  (2, 'zupa'))


class Lunch(models.Model):
    name = models.CharField(max_length=300)
    type = models.IntegerField(choices=LUNCH_TYPE)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    # date = models.ManyToManyField('LunchDate')

    def __str__(self):
        return self.name


class Appetizer(models.Model):
    name = models.CharField(max_length=300)
    type = models.IntegerField(choices=APPETIZER_TYPE)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    # date = models.ManyToManyField('AppetizerDate')

    def __str__(self):
        return self.name


class Beverages(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return self.name


class Order(models.Model):
    lunch = models.ForeignKey(Lunch, on_delete=models.CASCADE)
    appetizer = models.ForeignKey(Appetizer, on_delete=models.CASCADE, null=True)
    beverage = models.ForeignKey(Beverages, on_delete=models.CASCADE, null=True)
    final_price = models.DecimalField(decimal_places=2, max_digits=4)
    points = models.ForeignKey('Points', null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discount = models.IntegerField(default=0)
    points_collected = models.IntegerField(default=0)

    def __str__(self):
        return 'Zamówienie: {}, {}, {}'.format(self.lunch, self.appetizer, self.beverage)


class Points(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)


class LunchDate(models.Model):
    date = models.DateTimeField(default=datetime.today)
    lunch = models.ManyToManyField(Lunch)


class AppetizerDate(models.Model):
    date = models.DateTimeField(default=datetime.today)
    appetizer = models.ManyToManyField(Appetizer)
