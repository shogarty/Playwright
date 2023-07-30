import discord
import os

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$scene'):
    #substring
    chan = message.channel
    scene = await chan.create_thread(name = 'mythread')
    

  #create thread
  

  #make all past threads public


client.run(os.getenv('TOKEN'))
