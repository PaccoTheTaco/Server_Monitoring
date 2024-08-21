import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} ist online!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Error syncing commands: {e}")

async def main():
    await bot.load_extension("cpu")
    await bot.load_extension("ram")
    await bot.load_extension("systemload")
    await bot.start(TOKEN)

asyncio.run(main())
