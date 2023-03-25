import discord
from src.exec import execute_code

class CodeModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Snowball code", style=discord.InputTextStyle.paragraph))

    async def callback(self, interaction: discord.Interaction):
        output, error = execute_code(self.children[0].value)
        if error:
            await interaction.response.send_message("Compilation failed: " + error.decode("utf-8"))
        else:
            await interaction.response.send_message("Compilation successful: " + output.decode("utf-8"))
