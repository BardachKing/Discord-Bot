import discord
from discord.ext import commands

# Define intents (needed for certain features)
intents = discord.Intents.default()
intents.messages = True  # Enable message events

# Initialize the bot
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command: Ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong! 🏓')

# Run the bot
bot.run('MTMwNjQxMTg3MDI5ODgzNzAzMw.GT9QMe.lC9EVGmr55lBPoX90KJomzIbM7-I2c0ZG2J7nQ')
