import discord
from discord.ext import commands
from discord import Option

slash_categories = {
}

class CommandGroup(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    @discord.slash_command(name="compile")
    async def compile_cmd(self, interaction: discord.Interaction):
        await interaction.response.send_message('Hello')
