import discord
import discord.ext.commands  as commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()

token= os.getenv('DISCORD_TOKKEN')

handler= logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True


bot = commands.Bot(command_prefix='!', intents=intents)
#!hello 
#events
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.name}')

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
