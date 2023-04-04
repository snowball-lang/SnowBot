import datetime
import re
import discord
from discord.ext import commands
from discord import Option
from src.exec import execute_code

class CommandGroup(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(description="Compile snowball code")
    async def compile(self, ctx, *, code = None):
        async with ctx.typing():
            if code is None:
                await ctx.reply("", embed=self._create_how_to_pass_embed())
                return

            code = self.strip_source_code(code)

            p, output = execute_code(code)
            if p != 0:
                await ctx.reply("", embed=self._create_error_embed(output, ctx))
            else:
                await ctx.reply("", embed=self._create_output_embed(output, ctx))

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

    def _create_how_to_pass_embed(self):
        """
        Creates a Discord embed guide for passing code.
        Includes the 3 methods of passing source code.
        """
        embed = discord.Embed(title=f"How to pass snowball source code?", color=discord.Colour.from_rgb(255,255,255))

        embed.add_field(
            name="Method 1 (Plain)",
            value=(f"<@1088132784431829072> compile \n" "code"),
            inline=False,
        )
        embed.add_field(
            name="Method 2 (Code block)",
            value=(f"<@1088132784431829072> compile \n" "\`\`\`code\`\`\`"),
            inline=False,
        )
        embed.add_field(
            name="Method 3 (Syntax Highlighting)",
            value=(f"<@1088132784431829072> compile \n" f"\`\`\`rs\n" "code\`\`\`"),
            inline=False,
        )
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

    @staticmethod
    def strip_source_code(code: str) -> str:
        """
        Strips the source code from a Discord message.
        
        It strips:
            code wrapped in backticks ` (one line code)
            code wrapped in triple backtick ``` (multiline code)
            code wrapped in triple backticks and
                 language keyword ```python (syntax highlighting)
        """
        code = code.strip("`")
        if re.match(r"\w*\n", code):
            code = "\n".join(code.split("\n")[1:])
        return code

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(CommandGroup(bot)) # add the cog to the bot
