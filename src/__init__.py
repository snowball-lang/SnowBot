import os
import discord
from dotenv import load_dotenv
from .commands import CommandGroup

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

def bot():

    client = discord.Bot()

    @client.event
    async def on_ready():
        print("SnowBot ready to compile!")

    client.add_cog(CommandGroup(client))
    client.run(TOKEN)
