import os
import discord
import pycountry
import oddifiers

from dotenv import load_dotenv
load_dotenv()

class Oddify():
  token = os.environ["TOKEN"]
  channel = None

  def __init__(self):

    # to get member objects from get_user() client requires special intents
    intents = discord.Intents.default()
    intents.members = True

    self.client = discord.Client(intents=intents)


    @self.client.event
    async def on_ready():
      print("Discord Bot Ready!")

    # respond
    async def respond(message):

      # server count
      serverCount = len(self.client.guilds)

      # member count
      # set counts unique elements (members)
      # note: inneficent implementation, will need to be replaced with higher usage
      memberList = set()

      for server in self.client.guilds:
        for user in server.members: 
          memberList.add(user)

      memberCount = len(memberList)

      # set activity
      await self.client.change_presence(
        activity = discord.Activity(
          type = discord.ActivityType.watching, 
          name = "oddify help, in " + str(serverCount) + " servers with " + str(memberCount) + " members"
        )
      )

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
          # if not contry, test if oddifying person

          try:
            # get id
            user_id = argument.lower()

            # mentions are in format <@!id>
            # trim away <@! and >, and convert to int
            user_id = int(user_id[3:len(user_id) - 1])
            
            # test if user exists
            user = self.client.get_user(user_id)

            # test if valid
            url, name = user.avatar_url, user.name  

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

              result.add_field(
                name = "🧑‍🦲   Oddifying a person?",
                value = "Just type `oddify @<person>` to Oddify???"
              )

            else:
              # error
              result.color = discord.Colour.red()
              result.title = "Who's that pokemon???"

          else:         
            # get id
            user_id = argument.lower()

            # mentions are in format <@!id>
            # trim away <@! and >, anc convert to int
            user_id = int(user_id[3:len(user_id) - 1])

            # get user and oddify
            user = self.client.get_user(user_id)
            oddifiedUser = oddifiers.oddifyUser(user)
            
            # save image
            oddifiedUser["img"].save("profile.png")
            localImage = discord.File("profile.png")

            # setup embed
            img = "attachment://profile.png"
            result.set_image(url = img)
            result.title = name = "Odd " + oddifiedUser["name"] + "???"
            result.color = discord.Colour.green()

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
  oddify = Oddify()
