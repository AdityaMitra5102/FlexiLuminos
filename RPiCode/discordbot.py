#import webbrowser
import discord

from os import system

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
   

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        await message.channel.send('Write $help for commands')
        print('Introduction printed')
    if message.content.startswith('$help'):
        await message.channel.send('Hello!')
        await message.channel.send('Write $turnon to Turn on light')
        await message.channel.send('Write $turnoff to Turn off light')
        print('Help printed')
    if message.content.startswith('$turnon'):
        system('python switchon.py')
        #r=requests.get(url = URL, params = 'switchon')
        await message.channel.send('Turned Light on')
        print('Light turn on request received from Discord')
    if message.content.startswith('$turnoff'):
        system('python switchoff.py')
        #r=requests.get(url = URL, params = 'switchoff')
        await message.channel.send('Turned Light off')
        print('Light turn off request received from Discord')
a1="gWad2q1ctZNHc5IjEAFtzAhpajs"
a2="Nzc0NDY1NTgyNzExOTYzNjY5."
a3="X6YLRw."
a4=a2+a3+a1
client.run(a4)
