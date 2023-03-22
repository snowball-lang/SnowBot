import discord
from discord.ext import commands
from discord import Option

from src.exec import execute_code

class CommandGroup(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    @discord.slash_command(name="compile")
    async def compile_cmd(self, interaction: discord.Interaction, code: str):
        output, error = execute_code(code)
        if error:
            await interaction.response.send_message("Compilation failed: " + error.decode("utf-8"))
        else:
            await interaction.response.send_message("Compilation successful: " + output.decode("utf-8"))
