import discord, os, json, asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(intents=intents, command_prefix='!')

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
#cmds
@client.command()
async def cmds(ctx):
    embed = discord.Embed(
            title="Commands",
            description="""
[!gen]              -   sends a acc to your dms
[!stock]            -   shows all accs in stock
""",color=0x0000FF)
    embed.set_footer(text="dev: Yassen420 | Made with discord.py")
    await ctx.send(embed=embed)



#main stuff
@client.event
async def on_ready():
    client.remove_command('help')
    # load modules/cmds/cogs
    from Commands.gen import gen
    from Commands.stock import stock

    await client.add_cog(stock(client))
    await client.add_cog(gen(client))

    clear_console()
    print("gen bot is online!")

def tk():
     f = open("settings.json")
     data = json.load(f)
     token_ = data["token"]
     return token_

token = tk()
async def main():
    await client.start(token)
asyncio.run(main())
