import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

bot.run(os.getenv('MTMwNjQxMTg3MDI5ODgzNzAzMw.GT9QMe.lC9EVGmr55lBPoX90KJomzIbM7-I2c0ZG2J7nQ'))