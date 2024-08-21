import discord
from discord.ext import commands
import psutil

class RAM(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="ram", description="Zeigt die aktuelle RAM-Auslastung an.")
    async def ram_command(self, interaction: discord.Interaction):
        ram_usage = psutil.virtual_memory().percent
        embed = discord.Embed(title="RAM-Auslastung", description=f"Aktuelle RAM-Auslastung: {ram_usage}%", color=discord.Color.green())
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(RAM(bot))
