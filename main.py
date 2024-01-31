import datetime
from asyncio import sleep

import discord
from discord.ext import commands
import openai

import basecommands
import events

openai.api_key = 'your-api-key'
token = 'your-token'
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix='x!', intents=intents)
starttime = datetime.datetime.utcnow()


async def start():
    await client.add_cog(basecommands.BaseCommands(client))
    await client.add_cog(events.Events(client))
# do things while we are ready
@client.event
async def on_ready():
    client.remove_command('help')
    await start()
    print('Servers connected to:')
    for guild in client.guilds:
        print(guild.name)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f" x!help"))









@client.command()
async def bug(ctx, *, message=None):
    if message == None:
        await ctx.send(f"there is no message.")
    else:
        await ctx.send("Thank you for reporting this bug.")

        channel = client.get_channel(1195763719620272249)
        embed2 = discord.Embed(title=f"Bug reported by {ctx.author}", colour=discord.Colour.blue())
        embed2.add_field(name="Server", value=f"{ctx.guild.name}")
        embed2.add_field(name="Bug", value=f"{message}")
        if ctx.guild.icon:
            embed2.set_thumbnail(url=ctx.guild.icon.url)
        await channel.send(embed=embed2)






client.run(token)
