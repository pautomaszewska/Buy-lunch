# Generated by Django 2.1.7 on 2019-03-31 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buy_lunch', '0005_auto_20190331_1307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appetizer',
            old_name='type',
            new_name='appetizer_type',
        ),
    ]
