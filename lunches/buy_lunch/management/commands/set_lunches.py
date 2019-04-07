import datetime
from django.core.management.base import BaseCommand

from buy_lunch.models import Menu, Lunch, Appetizer


class Command(BaseCommand):
    help = 'Sets menu for the whole year'

    def handle(self, *args, **options):

        today = datetime.date.today()
        number = 101
        for date in range(number):
            d = today + datetime.timedelta(days=date)
            if d.weekday() in range(5):
                lunch_meat = Lunch.objects.filter(lunch_type=1).order_by('?').first()
                lunch_vegetarian = Lunch.objects.filter(lunch_type=2).order_by('?').first()
                lunch_vegan = Lunch.objects.filter(lunch_type=3).order_by('?').first()
                salad = Appetizer.objects.filter(appetizer_type=1).order_by('?').first()
                soup = Appetizer.objects.filter(appetizer_type=2).order_by('?').first()

                menu = Menu.objects.create(lunch_meat=lunch_meat,
                                           lunch_vegetarian=lunch_vegetarian,
                                           lunch_vegan=lunch_vegan,
                                           salad=salad,
                                           soup=soup,
                                           date=d)
                menu.save()




