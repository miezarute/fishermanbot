# -*- coding: UTF-8 -*- 
import discord
from discord.ext import commands
import json
import os


client = commands.Bot(command_prefix="f!", case_insensitive=True)
chave = open('token.txt','r')
token = chave.read()
chave.close


#imprimindo status do bot
@client.event
async def on_ready():
    print(client.user.name,'está online!')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Na pindaíba'))


############## Prncipal ############


@client.event
async def on_message(message):
    if message.author == client.user:
        return None

    await client.process_commands(message)#!!!não apagar esta linha!!!


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')



client.run(token)
