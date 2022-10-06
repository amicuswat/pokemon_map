from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='pokemons', blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

class PokemonEntity(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=True)
    appear_at = models.DateTimeField(null=True)
    disappear_at = models.DateTimeField(null=True)
