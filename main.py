import discord
from discord.ext import commands

bot=commands.Bot(command_prefix="!")

bot.run("OTExOTY1NjgwOTczMjcxMDgw.YZpEOQ.AAg8KaXRpAOvUzBGmvHBufMCMrg")

@bot.event
async def on_ready():
    print("ONLINE!")


@bot.command()
async def test(ctx):
    await ctx.send("Hey")