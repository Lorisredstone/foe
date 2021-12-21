import discord
from botoken import token
from asyncio import sleep

bot = discord.Client()

@bot.event
async def on_ready():
    while True:
        for a in ["par pf4", "$help"]:
            await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=a, type=3))
            await sleep(5)

@bot.event
async def on_message(message):
    if message.content == "$ping":
        await message.channel.send("pong")
        
        
bot.run(token)