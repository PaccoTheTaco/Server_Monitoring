import discord
from discord.ext import commands
import psutil

class DiskUsage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="diskusage", description="Zeigt die Festplattennutzung des Servers an.")
    async def diskusage_command(self, interaction: discord.Interaction):
        partitions = psutil.disk_partitions()
        embed = discord.Embed(title="Festplattennutzung", color=discord.Color.dark_blue())

        for partition in partitions:
            usage = psutil.disk_usage(partition.mountpoint)
            embed.add_field(
                name=f"Partition {partition.device}",
                value=f"Größe: {usage.total // (2**30)} GB\n"
                      f"Benutzt: {usage.used // (2**30)} GB ({usage.percent}%)\n"
                      f"Frei: {usage.free // (2**30)} GB",
                inline=False
            )

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(DiskUsage(bot))
