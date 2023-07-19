# Generated by Django 4.2.3 on 2023-07-14 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Vendor Name')),
                ('email', models.CharField(max_length=25, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=10, unique=True, verbose_name='Phone Number')),
                ('address', models.CharField(max_length=25, verbose_name='Address')),
            ],
        ),
    ]
