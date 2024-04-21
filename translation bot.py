import discord
from discord.ext import commands
from langdetect import detect
from deepl import Translator

intents = discord.Intents.all()
translator = Translator("your-deelp-token-here")
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:  # Ignore bot's own messages
        return
    if message.author.bot:  # Ignore messages from other bots
        return
    try:
        source_lang = detect(message.content)
        if source_lang == "en":
            return  # Do not translate if the message is in English
        result = translator.translate_text(message.content, target_lang="EN-US")
        await message.channel.send(f'Translated to English: {result.text}')
    except Exception as e:
        await message.channel.send(f'Error: {e}')

bot.run('your-discord-token-here')  # Replace 'YOUR_BOT_TOKEN' with your bot's token
