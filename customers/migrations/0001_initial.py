# Generated by Django 4.2.3 on 2023-07-13 11:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=25, verbose_name='First Name')),
                ('lname', models.CharField(max_length=25, verbose_name='Last Name')),
                ('phone_number', models.CharField(max_length=10, unique=True, verbose_name='Phone Number')),
                ('loyalty_points', models.IntegerField(default=0, verbose_name='Loyalty Points')),
                ('door_no', models.CharField(max_length=10, verbose_name='Door Number')),
                ('street', models.CharField(max_length=25, verbose_name='Street')),
                ('city', models.CharField(max_length=25, verbose_name='City')),
                ('state', models.CharField(max_length=25, verbose_name='State')),
                ('country', models.CharField(max_length=25, verbose_name='Country')),
                ('pincode', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^[0-9]{6}$', 'Invalid postal code')], verbose_name='Pincode')),
            ],
        ),
    ]