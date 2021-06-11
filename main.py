import os
import discord
from pokemon import pokemon
from dotenv import load_dotenv
from keepalive import keep_alive, app
load_dotenv()

class Oddify():
  client = discord.Client()
  token = os.environ["TOKEN"]
  channel = None

  def __init__(self):
    @self.client.event
    async def on_ready():
      print("Discord Bot Ready!")

    # respond
    async def respond(message):

      # pull argument from message
      argument = message.content.split(" ", 1)[1]

      # create embed to package response
      result = discord.Embed()

      try:
        # find index of pokemon
        pokemonIndex = pokemon.index(argument.lower())

      except:
        if argument.lower() == "help":
          # help command
          result.color = discord.Colour.blue()
          result.title = "Help"
          result.add_field(name = "Want to Oddify?", value = "Just type oddify `Pokemon` to Oddify???")
        else:
          # send error if invalid
          result.title = "Error: Pokemon Not Found???"
          result.color = discord.Colour.red()

      else:
        # get content for image
        # url in format url<pokedex num>/<pokedex num>.43.png
        # 43 is oddish's pokedex number
        img = "https://images.alexonsager.net/pokemon/fused/" + str(pokemonIndex) + "/" + str(pokemonIndex) + ".43.png"
        result.set_image(url = img)
        result.color = discord.Colour.green()

        # title
        result.title = "Odd " + pokemon[pokemonIndex].capitalize() + "???"

      await self.channel.send(embed=result)

    @self.client.event
    async def on_message(message):

      # ignore messages sent by self
      if message.author == self.client.user:
        return

      # set channel to respond to
      self.channel = self.client.get_channel(message.channel.id)

      # evaluate commands
      if message.content.startswith("oddify "):
        await respond(message)
    
    self.client.run(self.token)

if __name__ == '__main__':
  keep_alive()
  print("hi")
  oddify = Oddify()