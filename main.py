import os
import discord


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('')

    if message.content.startswith('$quiz'):
        await message.channel.send('> 1000 roopayude adhyathe chodhyam!')
        await message.channel.send('> Malayalikalude ishta paneeyam?')
        await message.channel.send("""> a) Chaya
        > b) Kappi
        > c) Pachavellam
        > d) karikk""")

client.run(os.getenv('DISCORDTOKEN'))

