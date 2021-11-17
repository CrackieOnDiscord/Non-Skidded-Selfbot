import discord
import json
import requests
import os
import colorama
from colorama import Fore, init
import ctypes
from discord.ext import commands

ctypes.windll.kernel32.SetConsoleTitleW("Welcome to NSSB! Status: Loading Selfbot...")

with open("./config.json") as f:
    config = json.load(f)
    
token = config.get('token')
prefix = config.get('prefix')
rpc = config.get('RPC')

nssb = discord.Client()
nssb = commands.Bot(command_prefix=prefix, self_bot = True)


def Init():
    
    
    header = {
        'Authorization': token
    }
    
    check = requests.get('https://discordapp.com/api/v9/auth/login', headers=header)
    
    if check.status_code == 200:
        nssb.run(token, bot = False, reconnect = True)
    else:
        print(f"{Fore.RED}[{Fore.WHITE}-{Fore.RED}] Invalid Token Entered! Please try again.{Fore.RESET}")
    
    

@nssb.command()
async def ping(ctx):
    em = discord.Embed()
    em.title = 'Pong ! :ping_pong:'
    em.color = discord.Colour.random()
    em.add_field(name = 'Latency:', value = f'{round(nssb.latency * 1000)}ms!')
    await ctx.send(embed = em)





@nssb.event
async def on_connect():
    print('test')






if __name__ == '__main__':
    Init()