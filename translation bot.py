import discord
from discord.ext import commands
from deepl import Translator

intents = discord.Intents.all()
translator = Translator("your-deepl-token-here")
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:  # Ignore bot's own messages
        return

    try:
        result = translator.translate_text(message.content, target_lang="EN-US")
        await message.channel.send(f'Translated to English: {result.text}')
    except Exception as e:
        await message.channel.send(f'Error: {e}')

bot.run('your-discord-token-here')  # Replace 'YOUR_BOT_TOKEN' with your bot's token
