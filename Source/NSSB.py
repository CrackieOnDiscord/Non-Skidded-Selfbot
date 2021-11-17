import discord
import json
import random
import time
import requests
import os
import colorama
import asyncio
import ctypes
import threading
from pypresence import Presence
from colorama import Fore, init
from discord import DMChannel
from discord.ext import commands



with open("./Data/config.json") as f:
    config = json.load(f)
    
token = config.get('token')
prefix = config.get('prefix')
rpc = config.get('RPC') #Broken until Leimag realizes this is going to be impossible

nssb = discord.Client()
nssb = commands.Bot(command_prefix=prefix, self_bot = True)
nssb.remove_command('help')

ctypes.windll.kernel32.SetConsoleTitleW("Welcome to NSSB! Status: Loading Selfbot...")

#Token Request Starts

def Run():
    
    
    header = {
        'Authorization': token
    }
    
    check = requests.get('https://discordapp.com/api/v9/auth/login', headers=header)
    
    try:
        nssb.run(token, bot = False, reconnect = True)
    except discord.errors.LoginFailure:
        print(f"[-] Invalid Token Entered! Please try again.")
        os.system('pause')

#Token Request Ends

def cls():
    os.system('cls')

def Loading():
    print(f'{Fore.LIGHTBLUE_EX}[+]{Fore.WHITE}Loading Selfbot.')
    time.sleep(0.3)
    cls()
    print(f'{Fore.LIGHTBLUE_EX}[+]{Fore.WHITE}Loading Selfbot..')
    time.sleep(0.3)
    cls()
    print(f'{Fore.LIGHTBLUE_EX}[+]{Fore.WHITE}Loading Selfbot...')
    time.sleep(0.3)
    cls()
    print(f'{Fore.LIGHTBLUE_EX}[+]{Fore.WHITE}Loading Selfbot....')
    time.sleep(0.3)
    cls()
    if token == "":
        print(f'{Fore.RED}[-]{Fore.WHITE}You havent put a token inside the config.json! Try again.')
        return
    else:
        print(f'{Fore.BLUE}[+]{Fore.WHITE}Token Recognized.')
    time.sleep(1)
    if prefix == "":
        print(f'{Fore.RED}[-]{Fore.WHITE}You havent put a prefix inside the config.json! Try again.')
        return
    else:
        print(f'{Fore.BLUE}[+]{Fore.WHITE}Prefix Recognized.')
    time.sleep(2)
    
    
#GUI Starts
    

def LoadedPrint():
    
    print(f'''{Fore.WHITE}
                                              {colorama.Fore.LIGHTBLUE_EX}███╗░░██╗░██████╗░██████╗██████╗░
                                              {colorama.Fore.WHITE}████╗░██║██╔════╝██╔════╝██╔══██╗
                                              {colorama.Fore.LIGHTBLUE_EX}██╔██╗██║╚█████╗░╚█████╗░██████╦╝
                                              {colorama.Fore.WHITE}██║╚████║░╚═══██╗░╚═══██╗██╔══██╗
                                              {colorama.Fore.LIGHTBLUE_EX}██║░╚███║██████╔╝██████╔╝██████╦╝
                                              {colorama.Fore.WHITE}╚═╝░░╚══╝╚═════╝░╚═════╝░╚═════╝░
             {colorama.Fore.LIGHTBLUE_EX}─────────────────────────────────────────────{colorama.Fore.WHITE}─────────────────────────────────────────────
                                                  {colorama.Fore.LIGHTBLUE_EX}Prefix: [{colorama.Fore.WHITE}{prefix}{colorama.Fore.LIGHTBLUE_EX}]
                                                  {colorama.Fore.LIGHTBLUE_EX}User: {colorama.Fore.LIGHTBLUE_EX}{nssb.user.name}{colorama.Fore.WHITE}#{nssb.user.discriminator}
                                                  {colorama.Fore.LIGHTBLUE_EX}Type {colorama.Fore.LIGHTBLUE_EX}{prefix}help{colorama.Fore.LIGHTBLUE_EX} to see commands
             {colorama.Fore.LIGHTBLUE_EX}─────────────────────────────────────────────{colorama.Fore.WHITE}─────────────────────────────────────────────
    ''' + Fore.WHITE)
    ctypes.windll.kernel32.SetConsoleTitleW(f'NSSB | Version 1.2 DEV |')
          
#GUI Ends

#Help Command Starts

@nssb.command()
async def help(ctx):
    await ctx.message.delete()
    em = discord.Embed()
    em.title = 'Help Commands'
    em.set_footer(text='Made by Clumsy && Leimag')
    em.color = discord.Colour.random()
    em.add_field(name = f'{prefix}help', value = 'This command...', inline=False)
    em.add_field(name = f'{prefix}massdm', value = 'Mass DM\'s friends in your friendslist, can mass dm an ID if provided.', inline=False)
    em.add_field(name = f'{prefix}leaveservers', value = 'Leaves servers for you.', inline=False)
    em.add_field(name = f'{prefix}randomnumber', value = 'Generates a random integer.', inline=False)
    await ctx.send(embed = em)

#Help Command Ends

#Misc Command Starts

@nssb.command()
async def ping(ctx):
    await ctx.message.delete()
    em = discord.Embed()
    em.title = 'Pong ! :ping_pong:'
    em.set_footer(text='Made by Clumsy && Leimag')
    em.color = discord.Colour.random()
    em.add_field(name = 'Latency:', value = f'{round(nssb.latency * 1000)}ms!')
    await ctx.send(embed = em)
    
    

@nssb.command()
async def massdm(ctx, msg, id = None):
    try:
        await ctx.message.delete()
    except:
        pass

        global massdm
        
        massdm = True
        
        if id == None:
            while massdm == True:
                for friend in nssb.user.friends:
                    try:
                        await friend.send(msg)
                        print(f"{Fore.GREEN}[+]Sent {msg}] to {friend.name}!")
                    except:
                        print(f"{Fore.RED}[-]Couldnt message {friend.name}!")
        else:
            user = await nssb.fetch_user(id)
            while massdm == True:
                await DMChannel.send(user, msg)
                print(f"{Fore.GREEN}[+]Sent {msg} to {id}!")
                
@nssb.command()
async def stopdm(ctx):
    global massdm
    try:
        await ctx.message.delete()
    except:
        pass
    massdm = False

@nssb.command()
async def leaveservers(ctx):
    await ctx.message.delete()
    headers = {"authorization": token}
    resp = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers)
    data = json.loads(resp.text)
    serversleft = int(0)

    for i in range(len(data)):
        serverleaving = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{data[i]['id']}",headers=headers).status_code
        if serverleaving == 204:
            serversleft += 1
        else:
            await asyncio.sleep(0.1)

    print(f"{Fore.GREEN}[-] {Fore.WHITE}Left {serversleft} Servers")
                
            
@nssb.command()
async def randomnumber(ctx):
    await ctx.message.delete()
    em = discord.Embed()
    RanNumber = {random.randrange(10000000)}
    em.title = 'Random Number Generated'
    em.description = f'Here is your randomly number: {RanNumber}'
    await ctx.send(embed = em)


#Misc Command Ends

#About Command Starts

@nssb.command()
async def about(ctx):
    await ctx.message.delete()
    em = discord.Embed()
    em.title = 'About NSSB'
    em.set_footer(text='Made by Clumsy && Leimag')
    em.color = discord.Colour.random()
    em.description = 'This Non Skidded SelfBot was made by Leimag#0001 and Clumsy#0420'
    await ctx.send(embed = em)

#About Command Ends
@nssb.event
async def on_connect():
    cls()
    Loading()
    cls()
    LoadedPrint()






if __name__ == '__main__':
    Run()