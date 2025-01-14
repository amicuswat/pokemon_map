import folium

from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime
from .models import PokemonEntity, Pokemon

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    entities = PokemonEntity.objects.filter(appear_at__lte=localtime(),
                                            disappear_at__gte=localtime())
    pokemons = Pokemon.objects.all()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for entity in entities:
        add_pokemon(
            folium_map, entity.lat,
            entity.lon,
            request.build_absolute_uri(entity.pokemon.photo.url),
        )

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.pk,
            'img_url': request.build_absolute_uri(pokemon.photo.url),
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)

    entities = pokemon.entities.filter(appear_at__lte=localtime(),
                                            disappear_at__gte=localtime())

    try:
        child_pokemon = pokemon.child_pokemons.get()
    except Pokemon.DoesNotExist:
        child_pokemon = None

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for entity in entities:
        add_pokemon(
            folium_map,
            entity.lat,
            entity.lon,
            request.build_absolute_uri(entity.pokemon.photo.url)
        )

    pokemon_serialized = {
        'title_ru': pokemon.title,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'description': pokemon.description,
        'img_url': request.build_absolute_uri(pokemon.photo.url),
    }

    if pokemon.parent:
        previous_evolution = {
            'img_url': request.build_absolute_uri(pokemon.parent.photo.url),
            'title_ru': pokemon.parent.title,
            'pokemon_id': pokemon.parent.id
        }

        pokemon_serialized['previous_evolution'] = previous_evolution

    if child_pokemon:
        next_evolution = {
            'img_url': request.build_absolute_uri(child_pokemon.photo.url),
            'title_ru': child_pokemon.title,
            'pokemon_id': child_pokemon.id
        }

        pokemon_serialized['next_evolution'] = next_evolution

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_serialized
    })
