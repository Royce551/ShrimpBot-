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
Version, token, alttoken, prefix, currency = fileservice.loadconfig()
Blueprint = True
description = '''an example'''
bot = commands.Bot(command_prefix='s#', description=description)
currenttime = int(time.time())
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
    if Blueprint == True:
        banner = 'https://cdn.discordapp.com/attachments/556283742008901645/600468110641987614/Banner-Blueprint.png'
    else:
        banner = 'https://cdn.discordapp.com/attachments/556283742008901645/600468110109048837/Banner.png'
    embed=discord.Embed(title="**ShrimpBot Information**", description="━━━━━━━━━━━━━━━━━", color=0x04a0db)
    embed.set_image(url=banner)
    embed.add_field(name="Created in Python with discord.py", value="by Squid Grill", inline=False)
    embed.add_field(name="Version", value=Version, inline=False)
    embed.add_field(name="Additional Help", value="AdrUlb", inline=False)
    embed.add_field(name="Official ShrimpBot Discord Server", value="https://discord.gg/XztEQAh", inline=False)
    embed.set_footer(text="This bot uses the MIT license. You can learn more here!   https://opensource.org/licenses/MIT")
    await ctx.send(embed=embed)

@bot.command()
async def report(ctx, message ='null'):
    if message != 'null':
        channel = client.get_channel(552304130992111641)
        await channel.send('**Bug Report from {}** - {}'.format(Version, message))
        await ctx.send('Successfully sent your bug report, "{}"'.format(message))
    else:
        await ctx.send('You need to provide a message first!')
    
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
        elif '@here' in ctx.message.content:
            await ctx.send('Can\'t ping everyone online.')
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
        elif '@here' in ctx.message.content:
            await ctx.send('Can\'t ping everyone online.')
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
        elif '@here' in ctx.message.content:
            await ctx.send('Can\'t ping everyone online.')
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
async def eightball(ctx):
    result, positive = cuteservice.get8ball()
    await ctx.send('''
**:8ball: The 8-Ball has spoken!**
It says - **{}**
'''.format(result))
@bot.command()
async def coinflip(ctx):
    flip = random.randint(1, 2)
    if flip == 1:
        await ctx.send('<@{}> flipped and got **HEADS!** :boy:'.format(ctx.message.author.id))
    else:
        await ctx.send('<@{}> flipped and got **TAILS!** :cat2:'.format(ctx.message.author.id))
#Economy

@bot.command()
async def balance(ctx):
    id = str(ctx.message.author.id).strip('<>@!')
    money = 50
    DMID = ctx.message.author
    try:
        money = int(fileservice.luserconfig(id))
    except:
        fileservice.cuserconfig(str(money), id)
    if money > 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
        await ctx.send('Holy fucking shit you\'re rich! To prevent spam, I\'ll DM you your balance.')
        await DMID.send('You have {} {}.'.format(money, currency))
    else:
        await ctx.send('You have {} {}.'.format(money, currency))
    
@bot.command()
async def pay(ctx, target, value = '100'):
    if int(value) < 1:
        await ctx.send("Please specify an amount larger than 0.")
        return

    recID = str(target).strip('<>@!')
    senderID = str(ctx.message.author.id).strip('<>@!')
    
    recMoney = 50
    senderMoney = 50
    
    # load money from recepient
    try:
        recMoney = int(fileservice.luserconfig(recID))
    except:
        fileservice.cuserconfig(str(recMoney), recID)
    # load money from sender
    try:
        senderMoney = int(fileservice.luserconfig(senderID))
    except:
        fileservice.cuserconfig(str(senderMoney), senderID)
    
    if senderMoney < int(value):
        await ctx.send("Oopsies! Looks like you don't have enough money!")
        return
    
    recMoney += int(value)
    senderMoney -= int(value)
    
    fileservice.cuserconfig(str(recMoney), recID)
    fileservice.cuserconfig(str(senderMoney), senderID)
    
    await ctx.send('Successfully gave {} {}.'.format(value, currency))
    await ctx.send('You now have {} {}.'.format(senderMoney, currency))

@bot.command()
async def gamble(ctx, value = 'null'):
    userID = str(ctx.message.author.id).strip('<>@!')
    
    if value != 'null':
        usergamble = random.randint(1,20)
        shrimpgamble = random.randint(1,20)
        if usergamble > shrimpgamble:
            try:
                money = int(fileservice.luserconfig(userID))
            except:
                fileservice.cuserconfig('50', userID)
            if money > 0:
                bet = int(value)
                bet *= 2
                money += bet
                await ctx.send('You - {} | ShrimpBot - {}. You won! Your bet got doubled. You\'re richer now, that\'s naisu.'.format(usergamble, shrimpgamble))
                fileservice.cuserconfig(str(money), userID)
            else:
                await ctx.send('Hold on, you don\'t even have enough money to bet this amount!')
        else:
            try:
                money = int(fileservice.luserconfig(userID))
            except:
                fileservice.cuserconfig('50', userID)
            if money > 0:
                money -= int(value)
                await ctx.send('You - {} | ShrimpBot - {}. ShrimpBot won, you lost all your money now. Oh dear.'.format(usergamble, shrimpgamble))
                fileservice.cuserconfig(str(money), userID)
            else:
                await ctx.send('Hold on, you don\'t even have enough money to bet this amount!')
    else:
        await ctx.send('You need to define an amount of money to gamble first!')

#Error Handling
#@bot.event
#async def on_command_error(self, ctx):
    #await ctx.send('Looks like you are missing a required argument. For more information, do s:help (command you\'re trying to run).')
if Blueprint == True:
    bot.run(alttoken)
else:
    bot.run(token)
    
