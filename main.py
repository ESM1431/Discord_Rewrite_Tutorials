import discord
from discord.ext import commands
from music import Player

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready.")

bot.run("ODg4MTA4MTU5ODAwMDUzNzYw.YUN5LQ.AvSUMfY8eWMcSxVScdYzfwZfx-A")