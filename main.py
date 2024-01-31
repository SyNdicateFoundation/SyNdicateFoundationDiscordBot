import datetime
import discord
from discord.ext import commands
import openai
import events
import basecommands
import modcommands
import othercommands
import voicecommands

openai.api_key = 'your-api-key'
token = 'your-token'
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix='x!', intents=intents)
starttime = datetime.datetime.utcnow()


async def start():
    await client.add_cog(events.Events(client))
    await client.add_cog(basecommands.BaseCommands(client))
    await client.add_cog(modcommands.ModCommands(client))
    await client.add_cog(voicecommands.VoiceCommands(client))
    await client.add_cog(othercommands.OtherCommands(client))


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
