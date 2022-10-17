from django.db import models

class Pokemon(models.Model):
    title = models.CharField(verbose_name='название', max_length=200)
    title_en = models.CharField(verbose_name='название анг', max_length=200,
                                blank=True)
    title_jp = models.CharField(verbose_name='название яп', max_length=200,
                                blank=True)

    description = models.TextField(verbose_name='описание',
                                   blank=True)
    photo = models.ImageField(verbose_name='изображение', upload_to='pokemons')

    parent = models.ForeignKey('self', verbose_name='Эволюционирует из',
                               related_name="child_pokemon",
                               on_delete=models.CASCADE,
                               blank=True, null=True)


    def __str__(self):
        return f"{self.title}"


class PokemonEntity(models.Model):
    lat = models.FloatField(verbose_name='широта')
    lon = models.FloatField(verbose_name='долгота')

    appear_at = models.DateTimeField(verbose_name='появится', null=True)
    disappear_at = models.DateTimeField(verbose_name='скроектся', null=True)

    level = models.IntegerField(verbose_name='уровень')
    health = models.IntegerField(verbose_name='здоровье')
    strength = models.IntegerField(verbose_name='сила')
    defense = models.IntegerField(verbose_name='защита')
    stamina = models.IntegerField(verbose_name='выносливость')

    pokemon = models.ForeignKey(Pokemon, verbose_name='покемон',
                                related_name="pokemon_entity",
                                on_delete=models.CASCADE)
