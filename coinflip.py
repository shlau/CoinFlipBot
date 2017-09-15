import discord
import asyncio
import config
import certifi
import random
import urllib3
import json

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('---------')

@client.event
async def on_message(message):
    if message.content.startswith('!coinflip'):
        rand = random.randint(0,1)
        if(rand == 0):
            await client.send_message(message.channel,'heads')
        else:
            await client.send_message(message.channel,'tails')

client.run(config.token)
