import discord
from discord.ext import commands
import psutil

class RAM(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="ram", description="Zeigt die aktuelle RAM-Auslastung an.")
    async def ram_command(self, interaction: discord.Interaction):
        memory = psutil.virtual_memory()
        total_memory = memory.total
        used_memory = memory.used
        ram_usage = memory.percent

        if total_memory >= 2**30:
            total_memory_str = f"{total_memory / (2**30):.2f} GB"
            used_memory_str = f"{used_memory / (2**30):.2f} GB"
        else:
            total_memory_str = f"{total_memory / (2**20):.0f} MB"
            used_memory_str = f"{used_memory / (2**20):.0f} MB"

        embed = discord.Embed(title="RAM-Auslastung", color=discord.Color.green())
        embed.add_field(name="Maximale RAM-Kapazität", value=total_memory_str, inline=False)
        embed.add_field(name="Genutzter RAM", value=used_memory_str, inline=False)
        embed.add_field(name="Prozentuale Auslastung", value=f"{ram_usage}%", inline=False)

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(RAM(bot))
