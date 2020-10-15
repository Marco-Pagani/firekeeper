import discord
import configparser
import image_handler

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

    if message.content.startswith('*help'):
         await message.channel.send('```\nCOMMANDS:\n*died - send a red message\n*lit - send an orange message\n*restored - send a green message\n```')

    if message.content.startswith('*emerald'):
        await message.channel.send('Bearer of the curse,')
        await message.channel.send('Seek')
        await message.channel.send('Seek')
        await message.channel.send('Lest')
        
    if message.content.startswith('*died'):
        image = image_handler.make_death_meme(message.content[6:])
        await message.delete()
        print(message.author.nick + " sent " + message.content)
        await message.channel.send('', file=discord.File(image))
        await message.channel.send('-' + message.author.nick)

    if message.content.startswith('*lit'):
        image = image_handler.make_bonfire_meme(message.content[5:])
        await message.delete()
        print(message.author.nick + " sent " + message.content)
        await message.channel.send('', file=discord.File(image))
        await message.channel.send('-' + message.author.nick)

    if message.content.startswith('*restored'):
        image = image_handler.make_humanity_meme(message.content[10:])
        await message.delete()
        print(message.author.nick + " sent " + message.content)
        await message.channel.send('', file=discord.File(image))
        await message.channel.send('-' + message.author.nick)


client.run(config['SECRET']['DISCORD_CLIENT_TOKEN'])

#image_handler.make_death_meme("test")