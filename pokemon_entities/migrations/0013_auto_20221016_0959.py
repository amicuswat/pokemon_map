# Generated by Django 3.1.14 on 2022-10-16 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0012_auto_20221007_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='photo',
            field=models.ImageField(upload_to='pokemons', verbose_name='изображение'),
        ),
    ]
