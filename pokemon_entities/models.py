from django.db import models

class Pokemon(models.Model):
    title = models.CharField(verbose_name='название', max_length=200)
    title_en = models.CharField(verbose_name='название анг', max_length=200,
                                blank=True, null=True)
    title_jp = models.CharField(verbose_name='название яп', max_length=200,
                                blank=True, null=True)

    description = models.TextField(verbose_name='описание',
                                   blank=True, null=True)
    photo = models.ImageField(verbose_name='изображение', upload_to='pokemons',
                              blank=True, null=True)

    parent = models.ForeignKey('self', verbose_name='Эволюционирует из',
                               on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

class PokemonEntity(models.Model):
    lat = models.FloatField(verbose_name='широта')
    lon = models.FloatField(verbose_name='долгота')

    appear_at = models.DateTimeField(verbose_name='появится', null=True)
    disappear_at = models.DateTimeField(verbose_name='скроектся', null=True)

    level = models.IntegerField(verbose_name='уровень', default=0)
    health = models.IntegerField(verbose_name='здоровье', default=100)
    strength = models.IntegerField(verbose_name='сила', default=1)
    defense = models.IntegerField(verbose_name='защита', default=1)
    stamina = models.IntegerField(verbose_name='выносливость', default=1)

    pokemon = models.ForeignKey(Pokemon, verbose_name='покемон',
                                on_delete=models.CASCADE)


