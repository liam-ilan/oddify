import os
import threading
import discord
import pycountry
from ping import app
import oddifiers

from dotenv import load_dotenv
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
      argument = message.content.split(" ", 1)[1].lower()

      # create embed to package response
      result = discord.Embed()

      # image for oddifying countries
      localImage = None

      try:
        # test if pokemon can be oddified
        oddifiedUrl = oddifiers.oddifyPokemon(argument)

      except:
        # if not oddifying pokemon, test if oddifying country
        try:
          pycountry.countries.lookup(argument.lower())

        except:
          if argument.lower() == "help":

            # setup embed
            result.color = discord.Colour.blue()
            result.title = "Help?"

            result.add_field(
              name = "🦄   Oddifying a Pokemon?", 
              value = "Just type `oddify <Pokemon>` to Oddify???"
            )

            result.add_field(
              name = "🌎   Oddifying a Country?",
              value = "Just type `oddify <Country>` or `oddify <Country Code>` to Oddify???"
            )
          else:

            # error
            # setup embed
            result.color = discord.Colour.red()
            result.title = "Who's that pokemon???"

        else:
          # oddify
          oddifiedCountry = oddifiers.oddifyCountry(argument.lower())

          # save image
          oddifiedCountry["img"].save("flag.png")
          localImage = discord.File("flag.png")

          # setup embed
          img = "attachment://flag.png"
          result.set_image(url = img)
          result.title = "Odd " + oddifiedCountry["name"] + "???"
          result.color = discord.Colour.green()

      else:
        # get data for image
        data = oddifiers.oddifyPokemon(argument)
        
        # set up embed
        result.set_image(url = data["url"])
        result.color = discord.Colour.green()
        result.title = "Odd " + data["name"] + "???"

      # send out
      if localImage != None:
        await self.channel.send(embed=result, file=localImage)
      else:
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
  pingThread = threading.Thread(target=app.run, kwargs={"host": "0.0.0.0"}, daemon=True)
  pingThread.start()
  oddify = Oddify()

