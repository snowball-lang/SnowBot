import discord
from discord.ext import commands
from discord import Option

from src.modals.code import CodeModal

class CommandGroup(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    @discord.slash_command(name="compile", description="Compile snowball code")
    async def compile_cmd(self, interaction: discord.Interaction):
        modal = CodeModal(title="Compile snowball code")
        await interaction.send_modal(modal)
