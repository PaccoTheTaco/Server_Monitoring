import discord
from discord.ext import commands
import psutil
import datetime

class Who(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="who", description="Zeigt die aktuell angemeldeten Benutzer an.")
    async def who_command(self, interaction: discord.Interaction):
        users = psutil.users()
        if not users:
            embed = discord.Embed(title="Angemeldete Benutzer", description="Derzeit ist kein Benutzer angemeldet.", color=discord.Color.blue())
        else:
            embed = discord.Embed(title="Angemeldete Benutzer", color=discord.Color.blue())
            for user in users:
                if user.host:
                    masked_ip = '.'.join(user.host.split('.')[:1]) + ".x.x.x"
                else:
                    masked_ip = "Unbekannt"
                
                login_time = datetime.datetime.fromtimestamp(user.started).strftime('%d.%m.%Y %H:%M:%S')

                embed.add_field(
                    name=f"Benutzername: {user.name}",
                    value=f"Terminal: {user.terminal}, Host: {masked_ip}, Anmeldezeit: {login_time}",
                    inline=False
                )

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Who(bot))
