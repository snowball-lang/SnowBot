import os
from dotenv import load_dotenv

from .commands import CommandGroup
from .mobile import identify

import discord
from discord.gateway import DiscordWebSocket

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

def bot():

    if not os.path.exists("./code"):
        os.mkdir("code")
        
    DiscordWebSocket.identify = identify
    client = discord.ext.commands.Bot(activity=discord.Activity(type=discord.ActivityType.watching, name="all of your spagetti code"))

    @client.event
    async def on_ready():
        print("SnowBot ready to compile!")

    client.load_extension('src.commands.__init__')
    client.run(TOKEN)
