import discord
from discord.ext import commands
import psutil
import datetime

class Uptime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="uptime", description="Zeigt die Uptime des Servers an.")
    async def uptime_command(self, interaction: discord.Interaction):
        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
        uptime_duration = datetime.datetime.now() - boot_time
        days, seconds = uptime_duration.days, uptime_duration.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60

        embed = discord.Embed(title="Server Uptime", color=discord.Color.blue())
        embed.add_field(name="Seit", value=boot_time.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
        embed.add_field(name="Laufzeit", value=f"{days} Tage, {hours} Stunden, {minutes} Minuten, {seconds} Sekunden", inline=False)

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Uptime(bot))
