from asyncio import sleep
import discord
import json

config_private = json.load(open('config/private.json'))

bot = discord.Client()

@bot.event
async def on_ready():
    for a in ["par pf4", "$help"]:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=a, type=3))
        sleep(5)

@bot.event
async def on_message(message):
    if message.content == "$ping":
        await message.channel.send("pong")
        
        
bot.run(config_private["discord_token"])