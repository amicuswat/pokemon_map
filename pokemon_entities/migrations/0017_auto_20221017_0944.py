# Generated by Django 3.1.14 on 2022-10-17 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0016_auto_20221016_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_pokemon', to='pokemon_entities.pokemon', verbose_name='Эволюционирует из'),
        ),
    ]
