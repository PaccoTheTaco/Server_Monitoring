import discord
from discord.ext import commands
import psutil
import platform

class NetstatView(discord.ui.View):
    def __init__(self, connections, port=None, timeout=60):
        super().__init__(timeout=timeout)
        self.connections = connections
        self.port = port
        self.current_page = 0
        self.per_page = 10

    def get_embed(self):
        start = self.current_page * self.per_page
        end = start + self.per_page
        current_connections = self.connections[start:end]

        if self.port:
            embed = discord.Embed(title=f"Verbindungen für Port {self.port}", color=discord.Color.orange())
            for i, conn in enumerate(current_connections, start=start + 1):
                embed.add_field(name=f"Verbindung {i}", value=f"Remote IP: {conn.raddr.ip}, Status: {conn.status}", inline=False)
        else:
            embed = discord.Embed(title="Verbindungen pro Port", color=discord.Color.orange())
            for i, (port, count) in enumerate(current_connections, start=start + 1):
                embed.add_field(name=f"Port {port}", value=f"Anzahl der Verbindungen: {count}", inline=False)

        embed.set_footer(text=f"Seite {self.current_page + 1}/{(len(self.connections) - 1) // self.per_page + 1}")
        return embed

    @discord.ui.button(label="Zurück", style=discord.ButtonStyle.secondary)
    async def previous_page(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.current_page > 0:
            self.current_page -= 1
            await interaction.response.edit_message(embed=self.get_embed(), view=self)

    @discord.ui.button(label="Weiter", style=discord.ButtonStyle.secondary)
    async def next_page(self, interaction: discord.Interaction, button: discord.ui.Button):
        if (self.current_page + 1) * self.per_page < len(self.connections):
            self.current_page += 1
            await interaction.response.edit_message(embed=self.get_embed(), view=self)

class Netstat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="netstat", description="Anzahl der Verbindungen pro Port oder Details für einen Port.")
    @discord.app_commands.describe(port="Optional: Port für Details anzeigen.")
    async def netstat_command(self, interaction: discord.Interaction, port: int = None):
        if platform.system() in ["Linux", "Darwin"]:
            connections = psutil.net_connections(kind='inet')

            if port:
                port_connections = [conn for conn in connections if conn.laddr.port == port and conn.status == psutil.CONN_ESTABLISHED and conn.raddr]
                if port_connections:
                    view = NetstatView(port_connections, port=port)
                    await interaction.response.send_message(embed=view.get_embed(), view=view)
                else:
                    await interaction.response.send_message(f"Keine aktiven Verbindungen für Port {port} gefunden.")
            else:
                port_count = {}
                for conn in connections:
                    if conn.status == psutil.CONN_ESTABLISHED and conn.raddr:
                        port = conn.laddr.port
                        port_count[port] = port_count.get(port, 0) + 1

                sorted_ports = sorted(port_count.items(), key=lambda x: x[1], reverse=True)
                view = NetstatView(sorted_ports)
                await interaction.response.send_message(embed=view.get_embed(), view=view)
        else:
            await interaction.response.send_message("Dieser Befehl ist nur auf Debian/Unix-Systemen verfügbar.")

async def setup(bot):
    await bot.add_cog(Netstat(bot))
