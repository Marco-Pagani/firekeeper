import discord
import configparser

client = discord.Client()
config = configparser.ConfigParser()
config.read('secret.ini')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('*emerald'):
        await message.channel.send('Bearer of the curse,')
        await message.channel.send('Seek')
        await message.channel.send('Seek')
        await message.channel.send('Lest')

client.run(config['SECRET']['DISCORD_CLIENT_TOKEN'])