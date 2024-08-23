import discord
from discord.ext import commands
import psutil

class ProcessesView(discord.ui.View):
    def __init__(self, processes, timeout=60):
        super().__init__(timeout=timeout)
        self.processes = processes
        self.current_page = 0
        self.per_page = 10

    def get_embed(self):
        start = self.current_page * self.per_page
        end = start + self.per_page
        current_processes = self.processes[start:end]

        embed = discord.Embed(title="Laufende Prozesse", color=discord.Color.purple())
        for i, (name, cpu) in enumerate(current_processes, start=start + 1):
            embed.add_field(name=f"{i}. {name}", value=f"CPU-Auslastung: {cpu}%", inline=False)
        embed.set_footer(text=f"Seite {self.current_page + 1}/{(len(self.processes) - 1) // self.per_page + 1}")
        return embed

    @discord.ui.button(label="Zurück", style=discord.ButtonStyle.secondary)
    async def previous_page(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.current_page > 0:
            self.current_page -= 1
            await interaction.response.edit_message(embed=self.get_embed(), view=self)

    @discord.ui.button(label="Weiter", style=discord.ButtonStyle.secondary)
    async def next_page(self, interaction: discord.Interaction, button: discord.ui.Button):
        if (self.current_page + 1) * self.per_page < len(self.processes):
            self.current_page += 1
            await interaction.response.edit_message(embed=self.get_embed(), view=self)

class Processes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="processes", description="Zeigt die laufenden Prozesse an und ermöglicht das Durchblättern.")
    async def processes_command(self, interaction: discord.Interaction):
        processes = [(p.info["name"], p.info["cpu_percent"]) for p in psutil.process_iter(["name", "cpu_percent"])]
        processes = sorted(processes, key=lambda x: x[1], reverse=True)

        view = ProcessesView(processes)
        await interaction.response.send_message(embed=view.get_embed(), view=view)

async def setup(bot):
    await bot.add_cog(Processes(bot))
