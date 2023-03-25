import datetime
import discord
from src.exec import execute_code

class CodeModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Snowball code", style=discord.InputTextStyle.paragraph))

    async def callback(self, interaction: discord.Interaction):
        output, p = execute_code(self.children[0].value)
        if p != 0:
            await interaction.response.send_message("", embed=self._create_error_embed(output, interaction))
        else:
            await interaction.response.send_message("", embed=self._create_output_embed(output, interaction))

    def _create_error_embed(self, error: str, ctx: discord.Interaction):
        embed = discord.Embed(
            title="Compilation failed!",
            description="There has been an error while compiling your code.",
            color=discord.Colour.red(),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )

        # embed.set_author(name=f"{str(ctx.author)}'s code execution", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Error message", value=f"```rs\n{error}```", inline=False)
        embed.set_footer(text="Fix your code and try again!")

        return embed

    def _create_output_embed(self, output: str, ctx: discord.Interaction):
        embed = discord.Embed(colour=discord.Colour.dark_grey(), timestamp=datetime.datetime.now(datetime.timezone.utc))
        # embed.set_author(name=f"{str(ctx.author)}'s code execution", icon_url=ctx.author.avatar_url)

        if len(output) > 300 or output.count("\n") > 10:
            embed.description = f"Output too large - [Full output](TODO)"

            if output.count("\n") > 10:
                output = "\n".join(output.split("\n")[:10]) + "\n(...)"
            else:
                output = output[:300] + "\n(...)"

        embed.add_field(name="Output", value=f"```yaml\n{output}```", inline=False)
        return embed