import discord
from discord.ext import commands
from langdetect import detect
from deepl import Translator

intents = discord.Intents.all()
translator = Translator("your-deepl-token-here")
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    await bot.process_commands(message)  # Add this line to process commands
    try:
        source_lang = detect(message.content)
        if source_lang == "en":
            return  # Do not translate if the message is in English
        result = translator.translate_text(message.content, target_lang="EN-US")
        await message.channel.send(f'Translated to English: {result.text}')
    except Exception as e:
        await message.channel.send(f'Error: {e}')

bot.run('your-discord-bot-token-here')  # Replace 'YOUR_BOT_TOKEN' with your bot's token