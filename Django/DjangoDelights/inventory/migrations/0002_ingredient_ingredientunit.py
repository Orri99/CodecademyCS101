# Generated by Django 4.2 on 2023-08-28 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='ingredientUnit',
            field=models.CharField(default='?', max_length=10, verbose_name='Unit'),
        ),
    ]
