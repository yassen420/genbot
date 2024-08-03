import discord, os
from discord.ext import commands

class stock(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def stock(self, ctx):
        accounts = os.listdir('Stock')
        ava = ''
        for file in accounts:
            with open(f'Stock/{file}', 'r') as f:
                account_count = sum(1 for line in f)
                ava += f'**{file[:-4]}**:   {account_count}\n'
        embed = discord.Embed(
            title="Stock",
            description=f"""
{ava}
""",color=0x0000FF)
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(stock(client))
