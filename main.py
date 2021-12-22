import asyncio, discord, json, random
import mod.gm as gm

config_private = json.load(open('config/private.json'))
config = json.load(open('config/config.json'))

bot = discord.Client()

def random_color():
    color = [0xFF5733, 0xFF8C33, 0xFFB833, 0xFFCD33, 0xFFF033, 0xB8FF33, 0x8CFF33, 0x33FF33, 0x33FF8C, 0x33FFB8, 0x33FFCD, 0x33FFF0, 0x33B8FF, 0x338CFF, 0x3333FF, 0x8C33FF, 0xB833FF, 0xCD33FF, 0xF033FF, 0xFF33F0, 0xFF33CD, 0xFF33B8, 0xFF338C, 0xFF3333]
    return random.choice(color)

@bot.event
async def on_ready():
    print("le bot est prêt")
    while True:
        for status in config["status"]["liste_status"]:
            await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=status, type=3))
            await asyncio.sleep(config["status"]["sleep_time"])

@bot.event
async def on_message(message):
    if message.content == "$ping":
        await message.channel.send("pong")

    elif message.content == "$help":
        color = random_color()
        embed = discord.Embed(color=color, title="Commandes disponiles", description="**$gm list**: liste les GM\n**$gm info *<id>* *<lvl>***: Affiche des informations sur le GM")
        await message.channel.send(embed=embed)
    
    elif message.content.startswith("$gm"):
        color = random_color()
        await gm.gm(message, color)

    elif message.content.startswith("$stop"):
        if message.author.id in [652889258343792661, 623570950754926603]:
            await message.channel.send(embed=discord.Embed(color=0xFF0000, title="Arrêt du bot"))
            await bot.close()
        
bot.run(config_private["discord_token"])