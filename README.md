# MemlogBot

***Update: [discord.py is no longer maintained](https://gist.github.com/Rapptz/4a2f62751b9600a31a0d3c78100287f1), this repository has been archived.***

A [discord.py](https://github.com/Rapptz/discord.py) bot that keeps track of ever-changing members, names, discriminators and roles for all your guilds/servers! Once running, the bot checks all guilds for changes every few minutes. All data is stored in [memlog.json](data/memlog.json) and the a crude summary of changes are appended to [changelog.txt](data/changelog.txt).

## Setup

1. Discord:
    1. You must have a [discord bot application](https://discord.com/developers/applications) set up

    2. Make sure your bot has [server members intent](https://discordpy.readthedocs.io/en/latest/intents.html?highlight=intents#privileged-intents) enabled

    2. Invite the bot to your guild(s)

2. Local:
    1. [Python 3.7.4](https://www.python.org/downloads/) or greater must be installed

    2. Clone this repository
        ```
        git clone https://github.com/Infinitifall/MemlogBot.git
        cd MemlogBot
        ```
    
    3. (Optional) Creating a [virtual environment](https://docs.python.org/3/tutorial/venv.html) is recommended
    
    4. Install all packages listed in [requirements.txt](requirements.txt)
        ```
        pip install -r requirements.txt
        ```

    5. In [bot_globals.py](data/bot_globals.py), update the following:
        - `bot_token` with your bot’s secret token (string)
    
    6. Finally, you dont want to accidentally git push sensitive data! ([*what is this?*](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---no-skip-worktree))
        ```
        git update-index --skip-worktree data/bot_globals.py
        git update-index --skip-worktree data/changelog.txt
        git update-index --skip-worktree data/memlog.json
        ```



## Run
Navigate to the main directory and run the [bot.py](bot.py) file
```
python bot.py
```
