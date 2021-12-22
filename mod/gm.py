import discord

async def gm(message):
    if message.content == "$gm help":
        await message.channel.send("Voici la liste des commandes: $gm help, $gm list, $gm add, $gm remove, $gm clear")