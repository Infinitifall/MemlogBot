import discord
import asyncio

from src.memlog import memlog
from data.bot_globals import bot_token

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("logged in as {} {} ({})".format(client.user.name, client.user.discriminator, client.user.id))
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Warden duty!"))
    print("bot is now ready")

    while(True):
        print("starting memlog")
        for guild in client.guilds:
            memlog(guild)
        print("done with memlog")
        # sleep for 10 minutes
        await asyncio.sleep(60*10)

if (__name__ == "__main__"):
    client.run(bot_token)
