import discord

async def gm(message, color):
    print(color)
    if message.content == "$gm help":
        embed = discord.Embed(color=color, title="commande $gm", description="$gm list\n$gm info <nom> <lvl>")
        await message.channel.send(embed=embed)