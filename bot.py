import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def scantank(ctx):
    await ctx.send('Temperature: 82 Degrees. PH Balance: Normal.')

bot.run('NzczOTU5MzI4NTk5NTA2OTQ0.X6Qzyw.thBEDTEeybZH0zMhlTfG5fW5jtk')