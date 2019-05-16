import discord
import random
import configparser
config = configparser.ConfigParser()
def loadconfig():
    config = configparser.ConfigParser()
    config.read('config.sffc')
    Version = config['Data']['version']
    token = config['Data']['token']
    alttoken = config['Data']['alttoken']
    prefix = config['Data']['prefix']
    return Version, token, alttoken, prefix;
def cserverconfig(sID, sCH, sMO):
    config = configparser.ConfigParser()
    config.add_section("Data")
    config.add_section("Flags")
    config['Data']['Version'] = '1'
    config['Data']['Server ID'] = sID
    config['Flags']['SuggestChannel'] = sCH
    config['Data']['Moderators'] = sMO
    with open(sID + '.sffs', 'w') as configfile:
        config.write(configfile)

cserverconfig('test', '123', '345')

