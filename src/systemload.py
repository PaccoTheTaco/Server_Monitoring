import discord
from discord.ext import commands
import platform
import os

class SystemLoad(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="systemload", description="Zeigt die aktuelle Systemauslastung an (nur Debian/Unix).")
    async def systemload_command(self, interaction: discord.Interaction):
        if platform.system() in ["Linux", "Darwin"]:
            load1, load5, load15 = os.getloadavg()
            embed = discord.Embed(title="Systemauslastung", color=discord.Color.blue())
            embed.add_field(name="1 Minute", value=f"{load1:.4f}", inline=False)
            embed.add_field(name="5 Minuten", value=f"{load5:.4f}", inline=False)
            embed.add_field(name="15 Minuten", value=f"{load15:.4f}", inline=False)
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message(
                "Dieser Befehl ist nur auf Debian/Unix-basierten Systemen verfügbar."
            )

async def setup(bot):
    await bot.add_cog(SystemLoad(bot))
