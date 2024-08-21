import discord
from discord.ext import commands
import psutil

class CPU(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="cpu", description="Zeigt die aktuelle CPU-Auslastung an.")
    async def cpu_command(self, interaction: discord.Interaction):
        cpu_usage = psutil.cpu_percent(interval=1)
        embed = discord.Embed(title="CPU-Auslastung", description=f"Aktuelle CPU-Auslastung: {cpu_usage}%", color=discord.Color.red())
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(CPU(bot))
