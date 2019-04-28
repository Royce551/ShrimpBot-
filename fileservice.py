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

