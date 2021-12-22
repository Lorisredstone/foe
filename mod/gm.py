import discord, requests
import mod.traduction as traduction


def get_batiment_info(batiment, lvl):
    return requests.get(f"https://api.foe-helper.com/v1/LegendaryBuilding/get?id={batiment}&level={lvl}").json()["response"]


async def gm(message, color):
    if message.content == "$gm help":
        embed = discord.Embed(color=color, title="Commandes $gm", description="**$gm list**: liste les GM\n**$gm info *<nom>* *<lvl>***: Affiche des informations sur le GM")
        await message.channel.send(embed=embed)
    elif message.content == "$gm list":
        liste = ", ".join([traduction.GMname[b] for b in traduction.GMname.keys()])
        embed = discord.Embed(color=color, title="Liste des GM", description=liste)
        await message.channel.send(embed=embed)