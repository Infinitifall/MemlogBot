# MemlogBot
A [discord.py](https://github.com/Rapptz/discord.py) bot that keeps track of ever-changing members, names, discriminators and roles for all your guilds/servers!

Once running, the bot checks all guilds for changes every few minutes. All data is stored in [memlog.json](data/memlog.json) and the a crude summary of changes are appended to [changelog.txt](data/changelog.txt).

## Setup

1. Discord:
    1. You must have a [discord bot application](https://discord.com/developers/applications) set up

    2. Make sure your bot has [server members intent](https://discordpy.readthedocs.io/en/latest/intents.html?highlight=intents#privileged-intents) enabled

    2. Invite the bot to your guild(s)

2. Local:
    1. [Python 3.7.4](https://www.python.org/downloads/) or greater must be installed

    2. Clone this repository
        ```
        git clone git@github.com:Infinitifall/MemlogBot.git
        cd MemlogBot
        ```
    
    3. (Optional) Creating a [virtual environment](https://docs.python.org/3/tutorial/venv.html) is recommended
    
    4. Install all packages listed in [requirements.txt](requirements.txt)
        ```
        pip install -r requirements.txt
        ```

    5. In [bot_globals.py](bot_globals.py), update the following:
        - `bot_token` with your bot’s secret token (string)



## Running the bot
1. Run the [bot.py](bot.py) file from the main directory, `python bot.py`.
