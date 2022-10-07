from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, blank=True, null=True)
    title_jp = models.CharField(max_length=200, blank=True, null=True)

    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='pokemons', blank=True, null=True)

    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

class PokemonEntity(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()

    appear_at = models.DateTimeField(null=True)
    disappear_at = models.DateTimeField(null=True)

    level = models.IntegerField(default=0)
    health = models.IntegerField(default=100)
    strength = models.IntegerField(default=1)
    defense = models.IntegerField(default=1)
    stamina = models.IntegerField(default=1)

    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=True)


