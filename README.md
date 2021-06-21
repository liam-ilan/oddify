# Oddify
[Add Oddify to your Discord Server](https://discord.com/api/oauth2/authorize?client_id=852342848174293022&permissions=268823632&scope=bot)

### A discord bot... but Oddish???
Oddify is a discord bot built for the sole of pasting Oddish's face onto random pokemon (and flags). It is made with [Pokemon Fusion](https://pokemon.alexonsager.net/), [Flagpedia](https://flagpedia.net/), and [discord.py](https://discordpy.readthedocs.io/en/stable/).

| ![Oddnat](./img/oddnat.png) | ![Oddto](./img/oddto.png) | ![Oddwhirl](./img/oddwhirl.png) |
| :-------------------------: | :-----------------------: | :-----------------------------: |
| <img src="./img/canada.png" alt="canada" width="240"/> | <img src="./img/uk.png" alt="uk" width="240"/> | <img src="./img/tuvalu.png" alt="tuvalu" width="240"/> |


### How to use
First, [Invite Oddify](https://discord.com/api/oauth2/authorize?client_id=852342848174293022&permissions=268823632&scope=bot). Then just type `oddify help` to get started!

### Some fun pokemon... but odd
| ![Oddpod](./img/oddpod.png) | ![Oddster](./img/oddster.png) |
| :-------------------------: | :---------------------------: |
| > `oddify metapod`          | > `oddify cloyster`           |

| ![Oddgar](./img/oddgar.png) | ![Oddth](./img/oddth.png) |
| :-------------------------: | :-----------------------: |
| > `oddify gengar`           | > `oddify meowth`         |

| ![Oddmime](./img/oddmime.png) | ![Oddfing](./img/oddfing.png) |
| :---------------------------: | :---------------------------: |
| > `oddify mr. mime`           | > `oddify koffing`            |

| ![Oddlax](./img/oddlax.png) | ![Oddish](./img/oddish.png) |
| :-------------------------: | :-------------------------: |
| > `oddify snorlax`          | > `oddify oddish`           |

### Flags
| <img src="./img/france.png" alt="france" width="240"/> | <img src="./img/unitedstates.png" alt="US" width="240"/> |
| :----------------------------------------------------: | :------------------------------------------------------: |
| > `oddify france`                                      | > `oddify us`                                            |

All 151 (+1) first generation pokemon are supported through https://pokemon.alexonsager.net/.
Flags from [Flagpedia](https://flagpedia.net/), names from [pycountry](https://pypi.org/project/pycountry/).

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
1. Set your buildpack to Python
2. Build `requirements.txt` with `poetry export -f requirements.txt --output requirements.txt`, since Heroku's Python buildpack uses pip to install packages.
3. Push the bot to Heroku
4. Ping the site to keep the bot online (see `ping.py`)

### Credits
Bot created by [Liam Ilan](https://www.liamilan.com/), all fusions created by [Pokemon Fusion](https://pokemon.alexonsager.net/)