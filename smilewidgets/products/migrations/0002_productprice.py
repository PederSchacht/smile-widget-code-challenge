# Generated by Django 2.0.7 on 2018-10-04 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name that describes the price change', max_length=35)),
                ('price', models.PositiveIntegerField(help_text='New price of product in cents')),
                ('date_start', models.DateField(help_text='Start date of price change')),
                ('date_end', models.DateField(blank=True, help_text='End date of price change', null=True)),
                ('product', models.ForeignKey(help_text='Product effected by a price change', on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]
