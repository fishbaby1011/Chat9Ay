import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message) and message.author != bot.user:
        response = get_random_nonsense()
        await message.channel.send(response)
    await bot.process_commands(message)

def get_random_nonsense():
    with open('nonsense_phrases.txt', 'r', encoding='utf-8') as file:
        nonsense_list = file.readlines()
    return random.choice(nonsense_list).strip()

bot.run('put your DC bot key here')
