import discord, requests
import mod.traduction as traduction


def get_batiment_info(batiment, lvl):
    return requests.get(f"https://api.foe-helper.com/v1/LegendaryBuilding/get?id={batiment}&level={lvl}").json()["response"]


async def gm(message, color):
    if message.content == "$gm help":
        embed = discord.Embed(color=color, title="Commandes $gm", description="**$gm list**: liste les GM\n**$gm info *<id>* *<lvl>***: Affiche des informations sur le GM")
        await message.channel.send(embed=embed)

    elif message.content in ["$gm list", "$gm liste"]:
        liste = ", ".join([f"[{traduction.GMname[b][0]}] *{traduction.GMname[b][1]}*" for b in traduction.GMname.keys()])
        embed = discord.Embed(color=color, title="Liste des GM", description=liste)
        await message.channel.send(embed=embed)

    elif message.content.startswith("$gm info"):
        try:
            GMdico = int(message.content.split(" ")[2])
            try:
                GMlvl = int(message.content.split(" ")[3])
            except:
                GMlvl = 1
            for b in traduction.GMname.keys():
                if GMdico == traduction.GMname[b][0]:
                    batiment = b
            batiment_info = get_batiment_info(traduction.GM_ID[batiment], GMlvl)
            embed = discord.Embed(color=color, title=f"{traduction.GMname[batiment][1]} - lvl{GMlvl}", description=f"**ère**: {traduction.ere[batiment_info['era']]}\n**PF lvl{GMlvl}**: {batiment_info['total_fp']}\n**produit**:")
            embed.set_thumbnail(url=batiment_info["image"])
            for k in batiment_info["rewards"].keys():
                embed.add_field(name=k.replace("_", " "), value=batiment_info["rewards"][k])
            await message.channel.send(embed=embed)
        except Exception as e:
            await message.channel.send(f"oups une erreur est survenue:\n{e}")