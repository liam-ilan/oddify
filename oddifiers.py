from PIL import Image
import requests
import pycountry
from pokemon import pokemons

# gets url, returns PIL image
def oddifyImage(url):
  front = Image.open("./assets/face.png").resize((480, 480)).convert("RGBA")

  imageData = requests.get(url, stream=True).raw
  back = Image.open(imageData).resize((480, 480)).convert("RGBA")

  back.paste(front, (0, 0), front)

  return back

# gets country
# returns PIL image
def oddifyCountry(country):
  countryName = country.lower()

  countryData = pycountry.countries.lookup(countryName)
  countryCode = countryData.alpha_2.lower()

  return oddifyImage("https://flagpedia.net/data/flags/emoji/twitter/256x256/" + countryCode + ".png")

# gets pokemon
# returns {url, name}
def oddifyPokemon(pokemon):
  pokemonIndex = pokemons.index(pokemon.lower())
  url = "https://images.alexonsager.net/pokemon/fused/" + str(pokemonIndex) + "/" + str(pokemonIndex) + ".43.png"
  return {"url": url, "name": pokemons[pokemonIndex]}