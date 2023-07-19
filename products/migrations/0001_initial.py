# Generated by Django 4.2.3 on 2023-07-14 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Product Name')),
                ('description', models.CharField(max_length=50, verbose_name='Description')),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cost Price')),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Selling Price')),
                ('quantity', models.IntegerField(default=0)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendors.vendor')),
            ],
        ),
    ]