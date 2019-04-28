import discord
import asyncio
import logging
from discord.ext import commands
import random
import time
import fileservice

logging.basicConfig(level=logging.INFO)
client = discord.Client()
#Variables
Version, token, alttoken, prefix = fileservice.loadconfig()
bot = commands.Bot(command_prefix=prefix)

#Startup
@client.event
async def on_ready():
    print('Hello! Welcome to ShrimpBot! Take a nice blast of information about me.')
    print('Username | ' + client.user.name + ' | User ID | ' + client.user.id + ' | Prefix | ' + prefix)



client.run(alttoken)
