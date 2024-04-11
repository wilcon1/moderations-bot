import config
from nextcord import Interaction,SlashOption
import nextcord
from nextcord.ext import commands,tasks
import mysql.connector
import os
import datetime
import random
intents = nextcord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)
@bot.event
async def on_ready():
    print("bot is ready")

for filename in os.listdir("./protoflio"):
    if filename.endswith(".py"):
        bot.load_extension(f"protoflio.{filename[:-3]}")
bot.run(config.TOKEN)