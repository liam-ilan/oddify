# Oddify
[Add Oddify to your Discord Server](https://discord.com/api/oauth2/authorize?client_id=852342848174293022&permissions=268823632&scope=bot)

### A discord bot... but Oddish???
Oddify is a discord bot built for the sole of pasting Oddish's face onto random pokemon. It is made with [Pokemon Fusion](https://pokemon.alexonsager.net/), and [discord.py](https://discordpy.readthedocs.io/en/stable/).

![Oddnat](https://images.alexonsager.net/pokemon/fused/48/48.43.png) ![Oddwhirl](https://images.alexonsager.net/pokemon/fused/61/61.43.png) ![Oddto](https://images.alexonsager.net/pokemon/fused/132/132.43.png)

### How to use
First, [Invite Oddify](https://discord.com/api/oauth2/authorize?client_id=852342848174293022&permissions=268823632&scope=bot). Then just type `oddify <pokemon>` to get started!

### Development
Clone this repo
``` bash
git clone https://github.com/liam-ilan/oddify.git
```

Install the required pacakges with Poetry
``` bash
poetry install
```
Alternatively, a `requirements.txt` file is provided

Create a bot through the discord developer dashboard
Invite it through the link obtained under the OAuth2 tab

Create a `.env` file, and write the following
``` bash
TOKEN=<secret token>
```
Your secret token is your bot's token

Then run
``` bash
poetry run python main.py
```
to start the bot

### Hosting through Heroku
1. Set your buildpack to python
2. Push the bot to Heroku
3. Ping the site to keep the bot online (see `ping.py`)

### Credits
Bot created by [Liam Ilan](liamilan.com)
All fusions created by [Pokemon Fusion](https://pokemon.alexonsager.net/)

### Some fun pokemon... but odd
| ![Oddpod](https://images.alexonsager.net/pokemon/fused/11/11.43.png) | ![Oddster](https://images.alexonsager.net/pokemon/fused/91/91.43.png) |
| :------------------------------------------------------------------: | :-------------------------------------------------------------------: |
| > `oddify metapod`                                                   | > `oddify cloyster`                                                   |

| ![Oddgar](https://images.alexonsager.net/pokemon/fused/94/94.43.png) | ![Oddth](https://images.alexonsager.net/pokemon/fused/52/52.43.png) |
| :------------------------------------------------------------------: | :-----------------------------------------------------------------: |
| > `oddify gengar`                                                    | > `oddify meowth`                                                   |

| ![Oddmime](https://images.alexonsager.net/pokemon/fused/122/122.43.png) | ![Oddfing](https://images.alexonsager.net/pokemon/fused/109/109.43.png) |
| :---------------------------------------------------------------------: | :---------------------------------------------------------------------: |
| > `oddify mr. mime`                                                     | > `oddify koffing`                                                      |

| ![Oddlax](https://images.alexonsager.net/pokemon/fused/143/143.43.png)  | ![Oddlax](https://images.alexonsager.net/pokemon/fused/43/43.43.png)    |
| :---------------------------------------------------------------------: | :---------------------------------------------------------------------: |
| > `oddify snorlax`                                                      | > `oddify oddish` for just Oddish :)                                    |

All 151 (+1) first generation pokemon are supported through https://pokemon.alexonsager.net/.
