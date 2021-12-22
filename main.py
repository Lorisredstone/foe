import asyncio
import discord
import json
import mod.gm as gm

config_private = json.load(open('config/private.json'))
config = json.load(open('config/config.json'))

bot = discord.Client()

@bot.event
async def on_ready():
    while True:
        for status in config["status"]["liste_status"]:
            await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=status, type=3))
            await asyncio.sleep(config["status"]["sleep_time"])

@bot.event
async def on_message(message):
    if message.content == "$ping":
        await message.channel.send("pong")

    if message.content == "$help":
        await message.channel.send("Voici la liste des commandes: $ping, $help")
    
    if message.content.startswith("$gm"):
        await gm(message)
        
bot.run(config_private["discord_token"])