import datetime
import discord
from discord.ext import commands
import openai
import events
import basecmds
import modcmds
import othercmds
import voicecmds

starttime = datetime.datetime.utcnow()
openai.api_key = 'your key'
token = 'your token'
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix='x!', intents=intents)



async def start():
    await client.add_cog(events.Events(client))
    await client.add_cog(basecmds.BaseCommands(client, starttime))
    await client.add_cog(modcmds.ModCommands(client))
    await client.add_cog(voicecmds.VoiceCommands(client))
    await client.add_cog(othercmds.OtherCommands(client))


# do things while we are ready
@client.event
async def on_ready():
    client.remove_command('help')
    await start()
    print('Servers connected to:')
    for guild in client.guilds:
        print(guild.name)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f" x!help"))


client.run(token)
