# Generated by Django 3.1.14 on 2022-10-16 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0015_auto_20221016_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='defense',
            field=models.IntegerField(verbose_name='защита'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(verbose_name='здоровье'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(verbose_name='уровень'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(verbose_name='выносливость'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='strength',
            field=models.IntegerField(verbose_name='сила'),
        ),
    ]
