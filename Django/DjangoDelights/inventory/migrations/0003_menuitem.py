# Generated by Django 4.2 on 2023-08-30 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_ingredient_ingredientunit'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menuitemName', models.CharField(max_length=50, verbose_name='Menu Item')),
                ('menuitemPrice', models.FloatField(default=20.0, verbose_name='Price')),
            ],
        ),
    ]