# Generated by Django 2.1.7 on 2019-04-01 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buy_lunch', '0012_auto_20190401_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lunchreview',
            name='lunch',
        ),
        migrations.AddField(
            model_name='lunchreview',
            name='lunch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='buy_lunch.Lunch'),
            preserve_default=False,
        ),
    ]