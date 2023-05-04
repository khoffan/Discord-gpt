import os
from components.vbot import show_message
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()


intents = discord.Intents.default()
intents.message_content = True
TOKEN = os.getenv('TOKEN')
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is now running")

@bot.command()
async def greet(ctx,*,message):
    try:
        print(message)
        gpt = show_message(message)
        print(gpt)
        
        await ctx.send(gpt)
    except Exception as e:
        print(e)


bot.run(TOKEN)