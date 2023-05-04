import os
from components.vbot import show_message
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
# from components.vbot import show_message

intents = discord.Intents.default()
intents.message_content = True
TOKEN = os.getenv('TOKEN')
# bot = commands.Bot(command_prefix='>', intents=intents)
# bot = commands.Bot(commands_prefix = "!")
bot = commands.Bot(command_prefix='$',intents=intents)

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
    # print(f"msg: {message}")
    # author = message.author
    # content = message.content.text
    # print(f"content: {content}")
    # response = f"Hello, {author.mention}! You said: '{content}'"

    # await ctx.send(response)


bot.run(TOKEN)
# import discord
# from discord.ext import commands
# from dotenv import load_dotenv
# import os

# load_dotenv()
# token = os.getenv('TOKEN')

# intents = discord.Intents.default()
# intents.message_content = True
# client = commands.Bot(command_prefix='!', intents=intents)

# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     print(f'{message.author} said: {message.content}')

# client.run(token)
