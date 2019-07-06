import discord
import asyncio
import logging
from discord.ext import commands
import random
import time
import fileservice
import cuteservice

logging.basicConfig(level=logging.INFO)
client = discord.Client()
#Variables
Version, token, alttoken, prefix = fileservice.loadconfig()
description = '''an example'''
bot = commands.Bot(command_prefix='s#', description=description)
bot.remove_command('help')
#Startup
@bot.event
async def on_ready():
    print('Hello! Welcome to ShrimpBot! Take a nice blast of information about me.')
    print('Username | ' + bot.user.name + ' | User ID | ' + str(bot.user.id) + ' | Prefix | ' + prefix)
    await bot.change_presence(activity=discord.Game(name='Rewriting my way to the future | ' + Version))
#Commands Area
#Core
@bot.command()
async def help(ctx, page ='0'):
    if page == '0':
        embed = discord.Embed(title=":information_source: **ShrimpBot Help**", description="━━━━━━━━━━━━━━━━━", color=0x04a0db)
        embed.add_field(name="placeholder", value="this is a placeholder for a command", inline=False)
        embed.set_footer(text="Need help with a specific command? Use s:help (command).")
        await ctx.send(embed=embed)
    else:
        await ctx.send(cuteservice.help(page))
@bot.command()
async def ping(ctx):
    await ctx.send('Pong! I\'m here! Heartbeat - **' + str(round(bot.latency, 3)) + '** seconds')
@bot.command()
async def about(ctx):
    embed=discord.Embed(title="**ShrimpBot Information**", description="━━━━━━━━━━━━━━━━━", color=0x04a0db)
    embed.set_image(url="https://cdn.discordapp.com/attachments/426843523623682048/596834585862602762/Banner.png")
    embed.add_field(name="Created in Python with discord.py", value="by Squid Grill", inline=False)
    embed.add_field(name="Version", value=Version, inline=False)
    embed.add_field(name="Additional Help", value="AdrUlb", inline=False)
    embed.add_field(name="Official ShrimpBot Discord Server", value="https://discord.gg/XztEQAh", inline=False)
    embed.set_footer(text="This bot uses the MIT license. You can learn more here!   https://opensource.org/licenses/MIT")
    await ctx.send(embed=embed)
#Moderation
@bot.command()
async def add(ctx):
    """test"""
    await ctx.send('Pong!')

@bot.command()
async def kick(ctx, user: discord.Member, reason):
    await ctx.send(':ok_hand: , I kicked this user for "' + reason + '".')
    try:
        await user.send('Oopsies! You screwed up! You got booted!')
    except:
        await ctx.send('Note - I was unable to send the kick message to this user.')
    await user.kick(reason=reason)
@bot.command()
async def ban(ctx, user: discord.Member, reason ='none '):
    if ctx.message.author.server_permissions.ban_members == True:
        if reason != 'none ':
            await ctx.send(':ok_hand: , I banned this user for "' + reason + '".')
            try:
                await user.send('Oopsies! You screwed up! You got banned!')
            except:
                await ctx.send('Note - I was unable to send the ban message to this user.')
            await user.ban(reason=reason)
        else:
            await ctx.send('Please provide a reason for banning this user.')
    else:
        await ctx.send('You lack permissions to ban this user.')
#Roleplay
@bot.command()
#async def cute(ctx, flag):
async def pet(ctx, pet ='none'):
    petsend, petinfo = cuteservice.pet()
    if pet == 'none':
        await ctx.send('Aww, I see you\'re lonely, take a head pat.')
        await ctx.send(file=discord.File(petsend))
    else:
        if '@everyone' in ctx.message.content:
            await ctx.send('Can\'t ping everyone.')
        else:
            await ctx.send(pet + ' got petted.')
            await ctx.send(file=discord.File(petsend))
            await ctx.send(petinfo)
@bot.command()
async def hug(ctx, pet ='none'):
    hugsend, huginfo = cuteservice.hug()
    if pet == 'none':
        await ctx.send('Aww, I see you\'re lonely, take a hug.')
        await ctx.send(file=discord.File(hugsend))
    else:
        if '@everyone' in ctx.message.content:
            await ctx.send('Can\'t ping everyone.')
        else:
            await ctx.send(pet + ' got hugged. Naisu.')
            await ctx.send(file=discord.File(hugsend))
            await ctx.send(huginfo)
@bot.command()
async def slap(ctx, pet ='none'):
    slapsend, slapinfo = cuteservice.slap()
    if pet == 'none':
        await ctx.send('Oh. You didn\'t specify anyone. Guess I\'ll slap you instead!')
        await ctx.send(file=discord.File(slapsend))
    else:
        if '@everyone' in ctx.message.content:
            await ctx.send('Can\'t ping everyone.')
        else:
            await ctx.send(pet + ' got slapped. Must have hurt.')
            await ctx.send(file=discord.File(slapsend))
            await ctx.send(slapinfo)
#Fun/Games
@bot.command()
async def cute(ctx, argu ='all'):
    await ctx.send('Here\'s something cute!')
    await ctx.send(file=discord.File(cuteservice.cute(argu)))
    
@bot.command()
async def patriotic(ctx):
    await ctx.send('Happy 4th of July! https://media.discordapp.net/attachments/356228137866231810/596428778712989702/Nylon-American-Flag-closeup-1.png?width=481&height=321')
#Economy
@bot.command()
async def testmoney(ctx, target, value = '100'):
    userID = str(target).strip('<>@')
    currentmoney = 50
    try:
        currentmoney = int(fileservice.luserconfig(str(userID)))
    except:
        fileservice.cuserconfig('50', str(userID))
    currentmoney += int(value)
    fileservice.cuserconfig(str(currentmoney), userID)
    await ctx.send('Successfully gave {} money!'.format(value))
    await ctx.send('You now have {} money!'.format(currentmoney))


#Error Handling
#@bot.event
#async def on_command_error(self, ctx):
    #await ctx.send('Looks like you are missing a required argument. For more information, do s:help (command you\'re trying to run).')
bot.run(alttoken)
    
