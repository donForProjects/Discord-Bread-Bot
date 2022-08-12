from http import client
import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('hello'):
        await message.channel.send("Bread.")
    elif message.content.startswith('Bread'):
        await message.channel.send("Nice.")

client.run('OTc5MzA4MDQ2OTM1Mjc3NjU4.Gh6Dq1.QL1XaD8GG_3iX0iWreaPBXFGieCA0twkcH7oBU')