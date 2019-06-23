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
description = '''an example'''
bot = commands.Bot(command_prefix='s#', description=description)

#Startup
@bot.event
async def on_ready():
    print('Hello! Welcome to ShrimpBot! Take a nice blast of information about me.')
    print('Username | ' + bot.user.name + ' | User ID | ' + str(bot.user.id) + ' | Prefix | ' + prefix)
#Commands Area
#Core/Moderation
@bot.command()
async def add(ctx):
    await ctx.send('Pong!')

@bot.command()
async def kick(ctx, user: discord.Member, reason):
    await ctx.send(':ok_hand: , I kicked this user for "' + reason + '".')
    await user.send('Oopsies! You screwed up! You got booted!')
    await user.kick(reason=reason)
#Roleplay
@bot.command()
async def pet(ctx, pet):
    petsend, petinfo = cuteservice.pet()
    if '@everyone' in message.content:
        await ctx.send('Can\'t ping everyone.')
    else:
        await ctx.send(pet + ' got petted.')
        await ctx.send(file=discord.File(petsend)
        await ctx.send(petinfo)
#Fun/Games

bot.run(alttoken)
