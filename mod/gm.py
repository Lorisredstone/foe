import discord, requests

def get_batiments():
    return list(requests.get("https://api.foe-helper.com/v1/LegendaryBuilding/list").json()["response"]["buildings"])


def get_batiment_info(batiment, lvl):
    return requests.get(f"https://api.foe-helper.com/v1/LegendaryBuilding/get?id={batiment}&level={lvl}").json()["response"]


async def gm(message, color):
    if message.content == "$gm help":
        embed = discord.Embed(color=color, title="commande $gm", description="$gm list\n$gm info <nom> <lvl>")
        await message.channel.send(embed=embed)