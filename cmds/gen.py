import discord, json
from discord.ext import commands

class gen(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def gen(self, ctx, account):
        f = open("settings.json")
        data = json.load(f)
        channel = data["channel_id"]
        if int(ctx.channel.id) == int(channel):
            try:
                with open(f"Stock/{account}.txt", "r"):
                    pass
                f = open(f"Stock/{account}.txt", "r").readlines()
                if len(f) == 0:
                    embed = discord.Embed(
                    title="out of stock :skull:",
                    description=f"we are out of {account} accs bruh",color=0xFF0000)
                    await ctx.send(embed=embed)
                else:
                    def account_():
                        with open(f'Stock/{account}.txt', 'r') as file:
                            r = file.readline().strip()
                            return r
                    with open(f'Stock/{account}.txt', 'r') as file:
                        lines = file.readlines()
                        embed1 = discord.Embed(
                        title=f"Here is your {account} account",
                        description=f"{account_()}",
                        color=0x00FF00)
                        await ctx.author.send(embed=embed1)
                    with open(f'Stock/{account}.txt', 'r') as file:
                        lines1 = file.readlines()
                    with open(f'Stock/{account}.txt', 'w') as file:
                        file.writelines(lines1[1:])
                    embed = discord.Embed(
                    title="Acc Sent!",
                    description=f"Sent a {account} acc to your dms!",
                    color=0x00FF00)
                    await ctx.send(embed=embed)
            except:
                embed = discord.Embed(
                title="Error",
                description=f"there are no {account} accounts in our stock :skull:",color=0xFF0000)
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
            title="Error",
            description=f"this command can be used In <#{channel}> only, faggot",color=0xFF0000)
            await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(gen(client))
