import os
from dotenv import load_dotenv

from .commands import CommandGroup
from .mobile import identify

import discord
from discord.gateway import DiscordWebSocket

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

def bot():
    DiscordWebSocket.identify = identify
    client = discord.Bot(activity=discord.Activity(type=discord.ActivityType.watching, name="all of your spagetti code"))

    @client.event
    async def on_ready():
        print("SnowBot ready to compile!")

    client.add_cog(CommandGroup(client))
    client.run(TOKEN)
