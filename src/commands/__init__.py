import discord
from discord.ext import commands
from discord import Option

class CommandGroup(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    @discord.slash_command(name="compile")
    async def compile_cmd(self, interaction: discord.Interaction, code: str):
        await interaction.response.send_message('Hello')
