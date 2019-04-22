from django.test import TestCase
from faker import Faker
from random import randint
from django.contrib.auth.models import User
from buy_lunch.models import Lunch, Appetizer, Beverages, Menu, MenuReview


class LunchTestCase(TestCase):
    def setUp(self):
        self.faker = Faker("pl_PL")
        for _ in range(5):
            Lunch.objects.create(lunch_name=self.faker.name(),
                                 lunch_type=randint(1, 3),
                                 lunch_price=randint(10, 20))

        for _ in range(5):
            Appetizer.objects.create(appetizer_name=self.faker.name(),
                                     appetizer_type=randint(1, 2),
                                     appetizer_price=randint(10, 20))

        for _ in range(5):
            Beverages.objects.create(beverage_name=self.faker.name(),
                                     beverage_price=randint(10, 20))

        lunch_meat = Lunch.objects.create(lunch_name=self.faker.name(),
                                          lunch_type=1,
                                          lunch_price=20)

        lunch_vegetarian = Lunch.objects.create(lunch_name=self.faker.name(),
                                                lunch_type=2,
                                                lunch_price=19)

        lunch_vegan = Lunch.objects.create(lunch_name=self.faker.name(),
                                           lunch_type=3,
                                           lunch_price=18)

        salad = Appetizer.objects.create(appetizer_name=self.faker.name(),
                                         appetizer_type=1,
                                         appetizer_price=10)

        soup = Appetizer.objects.create(appetizer_name=self.faker.name(),
                                        appetizer_type=2,
                                        appetizer_price=15)
        for _ in range(5):
            Menu.objects.create(date='2019-11-07 20:30:00',
                                lunch_meat=lunch_meat,
                                lunch_vegetarian=lunch_vegetarian,
                                lunch_vegan=lunch_vegan,
                                soup=soup,
                                salad=salad)

        self.user = User()
        self.username = 'testuser'
        self.email = 'test@test.com'
        self.password = '12345'
        self.user = User.objects.create_superuser(username=self.username, email=self.email, password=self.password)
        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)

    def test_get_lunch_list(self):
        response = self.client.get('/lunches/')
        self.assertEqual(response.status_code, 200)

    def test_get_appetizer_list(self):
        response = self.client.get('/appetizers/')
        self.assertEqual(response.status_code, 200)

    def test_get_beverage_list(self):
        response = self.client.get('/beverages/')
        self.assertEqual(response.status_code, 200)

    def test_post_lunch(self):
        lunch_before = Lunch.objects.count()
        new_lunch = {
            'lunch_name': '{}'.format(self.faker.name()),
            'lunch_type': '{}'.format(randint(1, 3)),
            'lunch_price': '{}'.format(randint(10, 20))
        }

        response = self.client.post('/add-lunch/', new_lunch)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Lunch.objects.count(), lunch_before + 1)

    def test_post_appetizer(self):
        appetizer_before = Appetizer.objects.count()
        new_appetizer = {
            'appetizer_name': '{}'.format(self.faker.name()),
            'appetizer_type': '{}'.format(randint(1, 2)),
            'appetizer_price': '{}'.format(randint(8, 15))
        }

        response = self.client.post('/add-appetizer/', new_appetizer)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Appetizer.objects.count(), appetizer_before + 1)

    def test_post_beverage(self):
        beverage_before = Beverages.objects.count()
        new_beverage = {
            'beverage_name': '{}'.format(self.faker.name()),
            'beverage_price': '{}'.format(randint(5, 10))
        }

        response = self.client.post('/add-beverage/', new_beverage)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Beverages.objects.count(), beverage_before + 1)

    def test_get_users_list(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)

    def test_get_user_details(self):
        response = self.client.get('/user-details/1')
        self.assertEqual(response.status_code, 200)

    def test_get_ranking(self):
        response = self.client.get('/ranking/')
        self.assertEqual(response.status_code, 200)

    def test_get_order_history(self):
        response = self.client.get('/all-orders/')
        self.assertEqual(response.status_code, 200)


