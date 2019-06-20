#Import Modules
import discord
import asyncio
import logging
from discord.ext import commands
import random
import ShrimpConfig
import time
import pickle
import cuteservice

logging.basicConfig(level=logging.INFO)

client = discord.Client()
#Variables
Version = 'Shrimpbot 16.4'
uptimeA = time.time()
Gtrycount = 0
bot = commands.Bot(command_prefix='s:', description=' ')
prefix = 's:'

#Startup Message
timer = 0
@client.event
async def on_ready():
    print('Hello, user! Welcome to Shrimpbot! This is some information about me!')
    print('  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print('Username of what I am connected to.')
    print(client.user.name)
    print('My user ID.')
    print(client.user.id)
    print('My prefix.')
    print(prefix)
    print('  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print('Fully locked and loaded, let\'s do this!')
    await client.change_presence(game=discord.Game(name='My robot body is ready. | ' + Version))
    await client.edit_profile(password=None, username= '' + Version)
    
#Commands 

    @client.event
    async def on_message(message):
        if message.content.startswith(prefix + 'mes'):
            counter = 0
            tmp = await client.send_message(message.channel, 'Calculating messages...')
            async for log in client.logs_from(message.channel, limit=100):
                if log.author == message.author:
                    counter += 1

            await client.edit_message(tmp, 'You have sent {} messages since Shrimpbot started running.'.format(counter))

        elif message.content.startswith(prefix + 'cool'):
            coolname = message.content[len('$$cool'):].strip()
            await client.send_message(message.channel, 'Hmm, you seem like a cool individual!'.format(coolname))
    
        elif message.content.startswith(prefix + 'yep'):
            await client.send_message(message.channel, 'Nope!')
            print('Succesfully executed !yep.')

        elif message.content.startswith(prefix + 'help'):
            helppage = message.content[len('$$help'):].strip()
            if helppage == '2':
                await client.send_message(message.channel, '''
                    :book: **Page 2 of 2** - Roleplay and Games | For general, go to Page 1.
                    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    **s:pet \(someone)** - Pets someone.
                    **s:hug \(someone)** - Hugs someone.
                    **s:slap \(someone)** - Slaps someone.
                    :video_game: **Fun and Games** :video_game:
                    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    **s:cute** - Gives you randomized cute anime girls.
                    **s:random \(number lower than 36)** - Shrimpbot picks a random number, if the number you
                    pick matches it, you win! If not, you lose, obviously!
                    **s:coinflip** - Flips a virtual coin.
                    **s:rate** - Rates people based on how GREAT they are!
                    *Note: Don't spam this command, please! You\'ll ratelimit the bot!*
                    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    Commands with the "#" symbol behind them don't need to be typed all the way, just type
                    the first 3 letters!
                    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    ''')
            elif helppage == '1':
                await client.send_message(message.channel, ''':information_source: **ShrimpBot Help | Updated 11/16/2018**
                    :book: **Page 1 of 2** - General | For roleplay and games, go to Page 2.
                    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    **# s:messages** - Tells you how many messages you sent since Shrimpbot started.
                    **s:cool** - Says that you are cool for self-gratification.
                    **s:wait** - I\'ll just do nothing, literally, that's it. Boring, right?
                    **s:yep and s:nope** - I'll say the opposite
                    **#s:information** - Tells you information about me.
                    **# s:useDM** -Makes me open a new DM with you so that you can use me in DM\'s.
                    **s:countdown** - Counts down from 10.
                    **# s:changelog** \(page number) - Shows the changes made in the current and previous versions of
                                                    Shrimpbot.
                    **s:uptime** - Shows the time since ShrimpBot started in seconds.
                    **s:report** - Sends messages directly to a "support channel" from anywhere.
                   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    Commands with the "#" symbol behind them don't need to be typed all the way, just type
                    the first 3 letters!
                    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    ''')
            elif helppage == '':
                await client.send_message(message.channel, ''':information_source: **ShrimpBot Help | Updated 11/16/2018**
                    :book: **Page 1 of 2** - General | For roleplay and games, go to Page 2.
                    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    **# s:messages** - Tells you how many messages you sent since Shrimpbot started.
                    **s:cool** - Says that you are cool for self-gratification.
                    **s:wait** - I\'ll just do nothing, literally, that's it. Boring, right?
                    **s:yep and s:nope** - I'll say the opposite
                    **#s:information** - Tells you information about me.
                    **# s:useDM** -Makes me open a new DM with you so that you can use me in DM\'s.
                    **s:countdown** - Counts down from 10.
                    **# s:changelog** \(page number) - Shows the changes made in the current and previous versions of
                                                    Shrimpbot.
                    **s:uptime** - Shows the time since ShrimpBot started in seconds.
                    **s:report** - Sends messages directly to a "support channel" from anywhere.
                   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    Commands with the "#" symbol behind them don't need to be typed all the way, just type
                    the first 3 letters!
                    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    ''')
            else:
                try:
                    await client.send_message(message.channel, cuteservice.help(helppage))
                except:
                    await client.send_message(message.channel, '''**An error has occured.**
                        The command you're trying to look up does not have any help documentation!''')
                print('Someone had an issue')
            print('Executed !help.')

        elif message.content.startswith(prefix + 'nope'):
            await client.send_message(message.channel, 'Yes!')
            print('Executed !nope.')

        elif message.content.startswith(prefix + 'inf'):
            await client.send_message(message.channel, ''':information_source: **ShrimpBot Information**
                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                **Created in Python with discord.py by Squid Grill.**
                **Programming and proofreading help** - KeinSkill
                **Version** - '''  + Version + '''
                **Cuteservice version** - '''  + cuteservice.cuver() + '''
                **Official ShrimpBot discord server** - https://discord.gg/fuJ6J4s
                This bot uses the MIT license. Learn more here - https://opensource.org/licenses/MIT
                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')
            await client.send_file(message.channel, 'Banner.png')
            print('Executed s:information')
            

        elif message.content.startswith(prefix + 'use'):
            await client.send_message(message.channel, 'Alright, I\'m opening up a DM.')
            await client.send_message(message.author, 'Hello there! You can use me as normal here!')
        elif message.content.startswith(prefix + 'ping'):
            await client.send_message(message.channel, 'Pong! I am currently working, as you can clearly see!')
#Roleplay commands 
        elif message.content.startswith(prefix + 'fart'):
            fartname = message.content[len('$$fart'):].strip()
            await client.send_message(message.channel, 'Roleplay commands in Shrimpbot will be disabled until they can be properly fixed, sorry.'.format(fartname))

        elif message.content.startswith(prefix + 'pet'):
            petname = message.content[len('$$pet'):].strip()
            if '@everyone' in message.content:
                await client.send_message(message.channel, 'Don\'t even try pinging everyone, mate.')
            elif '@here' in message.content:
                await client.send_message(message.channel, 'You can\'t do a here ping using Shrimpbot!')
            else:
                await client.send_message(message.channel, 'Aw, **{}** got petted by **'.format(petname) + str(message.author) + '**.')
                petsend, petinfo = cuteservice.pet()
                await client.send_file(message.channel, petsend)
                await client.send_message(message.channel, petinfo)

        elif message.content.startswith(prefix + 'kiss'):
            kissname = message.content[len('$$pet'):].strip()
            if '@everyone' in message.content:
                await client.send_message(message.channel, 'You can\'t ping everyone using Shrimpbot.')
            elif '@here' in message.content:
                await client.send_message(message.channel, 'You can\'t do a here ping using Shrimpbot.')
            else:
                await client.send_message(message.channel, 'Roleplay commands in Shrimpbot will be disabled until they can be properly fixed, sorry.'.format(kissname))

        elif message.content.startswith(prefix + 'slap'):
            hugname = message.content[len('$$slap'):].strip()
            if '@everyone' in message.content:
                await client.send_message(message.channel, 'Don\'t even try pinging everyone, mate.')
            elif '@here' in message.content:
                await client.send_message(message.channel, 'You can\'t do a here ping using Shrimpbot!')
            else:
                await client.send_message(message.channel, 'Ouch, **{}** got slapped by **'.format(hugname) + str(message.author) + '**.')
                slapsend, slapinfo = cuteservice.slap()
                await client.send_file(message.channel, slapsend)
                await client.send_message(message.channel, slapinfo)
                                      
        elif message.content.startswith(prefix + 'cute'):
            flag = message.content[len('$$cute'):].strip()
            if '@everyone' in message.content:
                await client.send_message(message.channel, 'Don\'t even try pinging everyone, mate.')
            elif '@here' in message.content:
                await client.send_message(message.channel, 'You can\'t do a here ping using Shrimpbot!')
            else:
                await client.send_message(message.channel, 'Here\'s something cute!')
                await client.send_file(message.channel, cuteservice.cute(flag))

        elif message.content.startswith(prefix + 'hug'):
            hugname = message.content[len('$$hug'):].strip()
            if '@everyone' in message.content:
                await client.send_message(message.channel, 'Don\'t even try pinging everyone, mate.')
            elif '@here' in message.content:
                await client.send_message(message.channel, 'You can\'t do a here ping using Shrimpbot!')
            else:
                await client.send_message(message.channel, '**{}** got hugged by **'.format(hugname) + str(message.author) + '**.')
                hugsend, huginfo = cuteservice.hug()
                await client.send_file(message.channel, hugsend)
                await client.send_message(message.channel, huginfo)

        elif message.content.startswith(prefix + 'cou'):
            countmessage = message.content[len('$$countdown'):].strip()
            tmp = await client.send_message(message.channel, '10!')
            await asyncio.sleep(1)
            await client.edit_message(tmp, '9!')
            await asyncio.sleep(1)
            await client.edit_message(tmp, '8!')
            await asyncio.sleep(1)
            await client.edit_message(tmp, '7!')
            await asyncio.sleep(1)
            await client.edit_message(tmp, '6!')
            await asyncio.sleep(1)
            await client.edit_message(tmp, '5!')
            await asyncio.sleep(1)
            await client.edit_message(tmp, '4!')
            await asyncio.sleep(1)
            await client.edit_message(tmp, '3!')
            await asyncio.sleep(1)
            await client.edit_message(tmp, '2!')
            await asyncio.sleep(1)
            await client.edit_message(tmp, '1!')
            await asyncio.sleep(1)
            await client.edit_message(tmp, 'Zero! The timer is finished!'.format(countmessage))
        elif message.content.startswith(prefix + 'changelog'):
            changepage = message.content[len('$$changelog'):].strip()
            if changepage == '1':
                await client.send_message(message.channel, '''
                :gear: **Changelog**
                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   
                :book: **Page 1 of 3** - For 15x, go to page 1, for versions prior to 15x, go to page 3
                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
                **Shrimpbot 16** 
                - Even more images and an improved interface for roleplay commands!
                - New cute command which gives you randomized cute anime girls.
                - Help and Changelog have multiple pages now.
                - Prefix can now be changed.
                - You can now get more information about a command by running s:help (command).
                - New fun commands including **flip**, **rate**, and more to come.
                - Some command interfaces got a fresh coat of paint.
                **Shrimpbot 16.1** 
                - Implemented new branding.
                **Shrimpbot 16.2** **Current Version!**
                - New report command that lets you send messages to squid from anywhere if you see
                something going wrong
                - Subtle improvements to formatting that will reduce OCD triggering.
                - Added some commands that were missing from the help command.
                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
                ''')
            elif changepage == '2':
                await client.send_message(message.channel, '''
                :gear: **Changelog**
                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                :book: **Page 2 of 3** - For Shrimpbot 16.x changes, go to page 1, for old\; page 3
                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
                 **Shrimpbot 15** 
                - Roleplay commands have returned!
                - The bot will now send you a message if you try to run a command that it does not
                   recognize.
                - Many major security issues with the bot have been fixed.
                - Games have been added! The games currently available include **random**.
                - Menus in the bot, such as **help** now look nicer.
                  **Shrimpbot 15.1**
                - Added an uptime command and support for working with time.
                  **Shrimpbot 15.2** 
                - Fixed a bug that caused the uptime command to stop working when it tried to add days to
                  the counter.
                - Minor formatting change for **help**.
                  **Shrimpbot 15.3**
                - Fixed formatting issues with roleplay commands
                ''')
            elif changepage == '3':
                await client.send_message(message.channel, '''
                 :gear: **Changelog**
                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                :book: **Page 3 of 3** - For Shrimpbot 16x changes, go to page 1, for 15x\; page 3
                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
                **Alpha 0.1.3**
                - Disabled all roleplay commands and other commands that allows the bot to send your own
                    message, this is to prevent abuse.
                - s:countdown no longer lets you send a reminder message. This, again, is to prevent abuse.
                - Improved formatting and general text on all information commands.
                - You no longer need to type the full name of long command names, you only need to type
                    the first 3 characters.
                - Removed the github link on the information panel. New releases of Shrimpbot will no
                    longer be on GitHub. DM me if you want to tell me about issues n\' stuff.
                - Some other minor internal changes.
                - Changed wording of some commands
                - Cleaned up code
                **Shrimpbot 14**
                - Minor Changes -''')
            else:
                await client.send_message(message.channel, 'That\'s not a valid page number!')
        elif message.content.startswith(prefix + 'testing'):
            if 'yes' in message.content:
                await client.send_message(message.channel, 'SUCCESS!' + Version)
                await client.send_file(message.channel, 'SakamotoAngary.png')
            else:
                await client.send_message(message.channel, 'SUCCESS BUT YES WASNT DETECTED!')

                
        elif message.content.startswith(prefix + 'random'):
            guessname = message.content[len('$$random '):].strip()
            randomnumber = str(random.randint(1,35))
            if guessname == randomnumber:
                await client.send_message(message.channel, ' :tada: **Great job! You are correct!**')
            else:
                await client.send_message(message.channel, ' :frowning2: Sorry, but you\'re wrong, the number was **' + str(randomnumber) + '**!')

 
        elif message.content.startswith(prefix + 'coinflip'):
            coin = random.randint(1,2)
            if coin == 1:
                await client.send_message(message.channel, str(message.author) + ' flipped and got **HEADS!** :boy:')
            else:
                await client.send_message(message.channel, str(message.author) + ' flipped and got **TAILS!** :cat2:')
        elif message.content.startswith(prefix + 'rate'):
            ratevalue = random.randint(1,100)
            person = message.content[len('$$rate '):].strip()
            if person == '':
                await client.send_message(message.channel, 'WOAH WOAH WOAH DUDE! You gotta mention someone to rate first!')
            elif person == '@everyone':
                await client.send_message(message.channel, 'WOAH WOAH WOAH! I ain\'t that stupid! No pinging everyone here!')
            elif person == '@here':
                await client.send_message(message.channel, 'WOAH WOAH WOAH! You can\'t just be going around pinging people like that!')
            else:
                if ratevalue < 30:
                    await client.send_message(message.channel, str(ratevalue) + ':star: ' + person + ' seems like an asshole to me!')
                elif ratevalue < 50:
                    await client.send_message(message.channel, str(ratevalue) + ':star: ' + ' I don\'t really like this person.')
                elif ratevalue < 70:
                    await client.send_message(message.channel, str(ratevalue) + ':star: ' + person + ' is really nice!')
                elif ratevalue < 95:
                    await client.send_message(message.channel, str(ratevalue) + ':star: ' + person + ' is soooo cool! I want to be like that.')
                else:
                    await client.send_message(message.channel, str(ratevalue) + ':star: ' + person + ' is the absolute best person alive right now.')
        elif message.content.startswith(prefix + 'uptime'):
            seconds = round(time.time() - uptimeA)
            minutes = 0
            hours = 0
            days = 0
            while seconds >= 60:
                seconds -= 60
                minutes += 1
            
            while minutes >= 60:
                minutes -= 60
                hours += 1

            while hours >= 24:
                hours -= 24
                days += 1

            await client.send_message(message.channel, ''':clock1: **Uptime**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
The bot has been running for ''' + str(days) + ''' days, ''' + str(hours) + ''' hours, ''' + str(minutes) + ''' minutes and ''' + str(seconds) + ''' seconds!''')

            if hours < 1:
                await client.send_message(message.channel, '    Looks like I booted up recently. Hopefully things go well!')
            elif hours > 1:
                await client.send_message(message.channel, '    That\'s pretty long for Shrimpbot!')
            elif hours > 10:
                await client.send_message(message.channel, '    Wow! That\'s a long time. Time to celebrate!')

        elif message.content.startswith(prefix + 'report'):
            reportmessage = message.content[len('$$report '):].strip()
            try:
                if '@everyone' in reportmessage:
                    await client.send_message(message.channel, 'i ain\'t that dumb, mate!')
                elif '@here' in reportmessage:
                    await client.send_message(message.channel, 'i ain\'t that dumb, mate!')
                else:
                    await client.send_message(message.channel, ':ok_hand:, Your message,"{}", has been sent successfully!'.format(reportmessage))
                    await client.send_message(discord.Object(id='552304130992111641'), '**bug report - **' + reportmessage)
            except:
                await client.send_message(message.channel, '''I'm sure you have more to say than just that...''')

        elif message.content.startswith(prefix + '8ball'):
            result, positive = cuteservice.get8ball()
            emoj = ''''''
            if positive == 'P':
                emoj == ''':green_heart:'''
            elif positive == 'C':
                emoj == ''':yellow_heart:'''
            else:
                emoj == ''':circle:'''
            await client.send_message(message.channel, ''':8ball: **8-Ball**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')
            await client.send_message(message.channel, '''''' + emoj + '''The 8 ball says: **''' + result + '''**''')
        elif message.content.startswith(prefix + 'Shrimpbot, get the weeb guns out'):
            await client.send_message(message.channel, '''ALRIGHT COMRADES, GET THE WEEB SHIT OUT, IT'S TIME TO WIPE OUT THE NON WEEBS.''')
            await client.send_file(message.channel, 'cute7.png')
            await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/417998031481208832/583947719647952896/72408310_p10.jpg')
            await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/417998031481208832/583947729668145163/72408310_p12.jpg')
        
                        #This must run last.
        elif message.content.startswith(prefix):
                await client.send_message(message.channel, '''**This is not a command I recognize.**
                 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                 **Did you mistype something?** Give it another shot!
                 Some commands may have been removed between versions.
                 **If you're not sure what you can do with Shrimpbot,** you can see the full list of
                 commands by using **s:help**.
                 ''')
        @client.event
        async def on_server_join():
            await client.send_message(message.channel, 'This works')
  
  
    

client.run('' + ShrimpConfig.token)
