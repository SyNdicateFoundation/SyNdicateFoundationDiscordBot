import datetime
from asyncio import sleep

import discord
from discord.ext import commands
import openai

openai.api_key = 'your-api-key'
token = 'your-token'
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix='x!', intents=intents)
starttime = datetime.datetime.utcnow()

#Send an error while command is unknown
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(embed=discord.Embed(title=f"Error!",
                                           description=f"Command not found. use x!help", color=ctx.author.color)
        )


#do things while we are ready
@client.event
async def on_ready():
    print('Servers connected to:')
    for guild in client.guilds:
        print(guild.name)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f" x!help"))


@client.event
async def on_message(message: discord.message.Message):
    if message.author.bot:
        return

    channel = client.get_channel(message.channel.id)
    if message.channel.id == 1200147835648221296:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "system", "content": "You are xenon bot"},
                {"role": "user", "content": message.content}
            ],
            max_tokens=150,
            temperature=0.7,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        await message.channel.send(response['choices'][0]['message']['content'])
        return

    await client.process_commands(message)

client.remove_command('help')


@client.command(aliases=['help', 'HELP', 'HElp', 'HELp'])
async def HElP(ctx: commands.Context):
    await ctx.send(embed=discord.Embed(title=f"Help", description=f"> :nerd~1: Help\n"
                                                     f"{ctx.author.name}\n"
                                                     f"development_team\n"
                                                     f"clear\n"
                                                     f"ping\n"
                                                     f"kick\n"
                                                     f"ban\n"
                                                     f"moveall\n"
                                                     f"avatar\n"
                                                     f"stats\n"
                                                     f"userinfo\n"
                                                     f"serverinfo\n"
                                                     f"uptime\n"
                                                     f"suggest\n"
                                                     f"helpme\n"
                                                     f"lock\n"
                                                     f"unlock\n"
                                                     f"unban\n"
                                                     f"mute\n"
                                                     f"unmute\n"
                                                     f"role\n"
                                                     f"join\n"
                                                     f"send\n"
                                                     f"> Prefix -->  x!", color=0x0B5394))


@client.command()
async def development_team(ctx: commands.Context):
    await ctx.send(embed=discord.Embed(title=f"Xenon Development Community", description=f"Xenon Development Community\n"
                                                                            f"https://discord.gg/BzY7hf2ACD\n"
                                                                            f"x!help for commands .", color=0x0B5394))
    await ctx.send("""https://discord.gg/BzY7hf2ACD""")


@client.command(aliases=['clean', 'hazf', 'c'])
async def clear(ctx, amount=1):
    try:
        await ctx.message.delete()
        if amount > 300 or amount < 1:
            s = await ctx.send(
                embed=discord.Embed(title=f"Faild!",
                                    description=f"Faild!\n"
                                                f"reseon : amount should be lower than 300 and higher than 1.\n"
                                                f"x!help for commands .",
                                    color=0xFF0000)
            )
            await sleep(5)
            await s.delete()
            await sleep(5)
            return
        textchannel = ctx.channel
        await ctx.send(embed=discord.Embed(title=f"doing your request ...",
                                           description=f"doing your request ...\n"
                                                       f"x!help for commands .",
                                           color=0x0B5394))
        await textchannel.purge(limit=amount + 1)
        s = await ctx.senddiscord.Embed(title=f"done ?", description=f"done!\n"
                                                                     f"deleted {amount} messages in {ctx.channel.name} text channel .\n"
                                                                     f"x!help for commands .", color=0x57ff36)
        await sleep(5)
        await s.delete()
        await sleep(5)
    except discord.errors.Forbidden:
        s = await ctx.send(discord.Embed(title=f"Need permission!",
                                         description=f"I need **manage messages** permission\n"
                                                     f"x!help for commands .", color=0x0B5394)
                           )
        await sleep(5)
        await s.delete()
        await sleep(5)


@client.command(aliases=['connection', 'pong', 'ertebat'])
async def ping(ctx: commands.Context):
    try:
        s = await ctx.send(embed=discord.Embed(title=f"Ping", description=f"perfoming test ...\n"
                                                                          f"x!help for commands",
                                               color=0x0B5394)
                           )
        await sleep(5)
        await s.delete()
        await sleep(5)
        s = await ctx.send(
            embed=discord.Embed(title=f"Ping", description=f"test 1 : {round(client.latency * 1000)} ms\n"
                                                           f"test 2 : {round(client.latency * 1000)} ms\n"
                                                           f"test 3 : {round(client.latency * 1000)} ms\n"
                                                           f"x!help for commands",
                                color=0x0B5394)
            )
        await sleep(5)
        await s.delete()
        await sleep(5)
        s = await ctx.send(embed=discord.Embed(title=f"Ping", description=f"Done ?\n"
                                                                          f"x!help for commands",
                                               color=0x57ff36)
                           )
        await sleep(5)
        await s.delete()
        await sleep(5)
    except discord.errors.Forbidden:
        s = await ctx.send(embed=discord.Embed(title=f"Error",
                                               description=f"please try later\n"
                                                           f"x!help for commands",
                                               color=0x0B5394)
                           )
        await sleep(5)
        await s.delete()
        await sleep(5)


# owner commands
@client.command()
async def serverlist(ctx):
    if ctx.author.id == 1042894447815430229:
        msg = "\n".join(f"{x}" for x in client.guilds)
        s = ctx.send(embed=discord.Embed(title=f"server list", description=f"```\n{msg}\n```\n"
                                                                           f"x!help for commands",
                                         color=0x57ff36)
                     )
    else:
        s = await ctx.send(
            embed=discord.Embed(title=f"Only dev can use this.", description=f"this is only owner command .\n"
                                                                             f"x!help for commands", color=0x57ff36)
            )
        await sleep(5)
        await s.delete()
        await sleep(5)


# mod command
@client.command()
async def kick(ctx: commands.Context, member: discord.Member, *, reason: str = "no reason", error):
    if member.id == ctx.author.id:
        s = await ctx.send(
            embed=discord.Embed(title=f":|", description=f"Why you wanna kick yourself?\n"
                                                         f"x!help for commands",
                                color=0x57ff36)
        )
        await sleep(5)
        await s.delete()
        await sleep(5)
        return

    if ctx.author.guild_permissions.kick_members:
        embed = await ctx.send(embed=discord.Embed(title=f"User Kicked", description=f"kicked : {member.display_name}\n"
                                                                                     f"by : {ctx.author.display_name}\n"
                                                                                     f"reason : {reason}",
                                                   color=0x57ff36)
                               )
        await member.kick(reason=reason)
        await sleep(5)
        await embed.delete()
        await sleep(5)
    else:
        s = await ctx.send(embed=discord.Embed(title=f"access denied?", description=f"your access denied !\n"
                                                                                    f"reseon : you dont have **kick_members** permission .\n"
                                                                                    f"x!help for commands .",
                                               color=0xFF0000)
                           )
        await sleep(5)
        await s.delete()
        await sleep(5)


@client.command()
async def ban(ctx: commands.Context, member: discord.Member, *, reason: str = "no reason"):
    if member.id == ctx.author.id:
        s = await ctx.send(
            embed=discord.Embed(title=f":|", description=f"Why you wanna ban yourself?\n"
                                                         f"x!help for commands",
                                color=0x57ff36)
        )
        await sleep(5)
        await s.delete()
        await sleep(5)
        return

    if ctx.author.guild_permissions.ban_members:
        s = await ctx.send(embed=discord.Embed(title=f"User banned", description=f"banned : {member.display_name}\n"
                                                                                 f"by : {ctx.author.display_name}\n"
                                                                                 f"reason : {reason}", color=0x57ff36)
                           )
        await member.ban(reason=reason)
        await sleep(5)
        await s.delete()
        await sleep(5)
    else:
        s = await ctx.send(embed=discord.Embed(title=f"access denied?", description=f"your access denied !\n"
                                                                                    f"reseon : you dont have **ban_members** permission .\n"
                                                                                    f"x!help for commands .",
                                               color=0xFF0000)
                           )
        await sleep(5)
        await s.delete()
        await sleep(5)


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        s = await ctx.send(embed=discord.Embed(title="Wrong Usage",
                                               description=f"x!ban @member ",
                                               colour=discord.Colour.blue())
                           )
        await sleep(5)
        await s.delete()
        await sleep(5)
    if isinstance(error, commands.MissingRequiredArgument):
        s = await ctx.send(embed=discord.Embed(title="Wrong Usage",
                                               description=f"x!ban @member ",
                                               colour=discord.Colour.blue())
                           )
        await sleep(5)
        await s.delete()
        await sleep(5)
    if discord.errors.Forbidden:
        s = await ctx.send(embed=discord.Embed(title="no perm",
                                               description=f"I dont have ban access.",
                                               colour=discord.Colour.blue())
                           )
        await sleep(5)
        await s.delete()
        await sleep(5)


@client.command(aliases=['move'])
async def moveall(ctx: commands.Context):
    if not ctx.author.guild_permissions.move_members:
        s = await ctx.send(
            embed=discord.Embed(title=f"Faild!", description=f"Join a voice first or check your perms.\n",
                                color=0x57ff36)
        )
        await sleep(5)
        await s.delete()
        await sleep(5)
        return
    try:
        if ctx.author.voice != None:
            moved_members = []
            for voice_channel in ctx.guild.voice_channels:
                for member in voice_channel.members:
                    await member.move_to(ctx.author.voice.channel)
                    moved_members.append(member)
            s = await ctx.send(
                embed=discord.Embed(title=f"Users moved", description=f"channel : {ctx.author.voice.channel}\n"
                                                                      f"by : {ctx.author.display_name}\n",
                                    color=0x57ff36)
                )
            await sleep(5)
            await s.delete()
            await sleep(5)
        else:
            s = await ctx.send(
                embed=discord.Embed(title=f"Faild!", description=f"Join a voice first or check your perms.\n",
                                    color=0x57ff36)
            )
            await sleep(5)
            await s.delete()
            await sleep(5)
    except discord.errors.Forbidden:
        s = await ctx.send(
            embed=discord.Embed(title=f"No perm", description=f"I don't have **move members** perm\n",
                                color=0x57ff36)
        )
        await sleep(5)
        await s.delete()
        await sleep(5)


@client.command()
async def avatar(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
    embed = discord.Embed(
        title="Avatar Link",
        url=member.avatar_url,
        colour=0xf9cb11
    )
    embed.set_author(
        name=f"{member}",
        icon_url=member.avatar_url)
    embed.set_footer(
        text=f"Requested by {ctx.author}",
        icon_url=ctx.author.avatar_url)
    embed.set_image(url=member.avatar_url)
    await ctx.send(embed=embed)


@client.command()
async def stats(ctx: commands.Context):
    member_count = len(ctx.guild.members)

    no_bot = len([m for m in ctx.guild.members if not m.bot])
    embed = discord.Embed(title=f"Xenon Development Community's bot stats",
                          description=f"servers : {len(client.guilds)}\n"
                                      f"members : {member_count}\n"
                                      f"ping : {round(client.latency * 1000)}\n"
                                      f"real members : {round(no_bot)}"
                                      f"x!help for commands", color=0x0B5394)
    await ctx.send(embed=embed)


@client.event
async def on_guild_join(guild):
    bot_entry = await guild.audit_logs(action=discord.AuditLogAction.bot_add).flatten()
    join = discord.Embed(title="Thanks for adding Xenon Development Community", colour=discord.Colour.blue(),
                         )
    try:
        await bot_entry[0].user.send(embed=join)
    except discord.errors.Forbidden:
        try:
            await guild.system_channel.send(embed=join)
        except:
            pass


@client.command(pass_context=True)
async def serverinfo(ctx):
    guild_roles = len(ctx.guild.roles)
    guild_categories = len(ctx.guild.categories)
    guild_members = len(ctx.guild.members)
    text_channels = len(ctx.guild.text_channels)
    voice_channels = len(ctx.guild.voice_channels)
    channels = text_channels + voice_channels
    serverinfo = discord.Embed(colour=discord.Colour.blue())
    serverinfo.add_field(name="Server Name", value=f"{ctx.guild.name}")
    serverinfo.add_field(name="Server ID", value=f"{ctx.guild.id}")
    serverinfo.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    serverinfo.add_field(name="Boosts", value=f"{ctx.guild.premium_subscription_count}")
    serverinfo.add_field(name="Channels", value=f"{channels}")
    serverinfo.add_field(name="Roles", value=f"{guild_roles}")
    serverinfo.add_field(name="Categories", value=f"{guild_categories} Categories")
    serverinfo.add_field(name="Members", value=f"{guild_members}")
    if ctx.guild.icon:
        serverinfo.set_thumbnail(url=ctx.guild.icon.url)
    await ctx.send(embed=serverinfo)


@client.command()
async def uptime(ctx):
    uptime = datetime.datetime.utcnow() - starttime
    hour = str(uptime).split('.')[0]
    await ctx.send(embed=discord.Embed(title="Uptime",
                                       description=f"{uptime}",
                                       color=discord.Colour.blue()))


@client.command()
async def userinfo(ctx, member: discord.Member = None):
    username = member.display_name
    user_url = member.avatar.url
    user_join_date = member.joined_at.utcnow()
    embed2 = discord.Embed(title=f"User Info: {member.display_name}",
                           colour=discord.Colour.blue())
    embed2.add_field(name="Server", value=f"{ctx.guild.name}")
    if ctx.guild.icon:
        embed2.set_thumbnail(url=ctx.guild.icon.url)
    await ctx.send(embed=embed2)


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


@client.command()
async def suggest(ctx, *, message=None):
    if message == None:
        await ctx.send(f"there is no message.")
    else:
        await ctx.send("Thank you for giving a suggestion.")
        channel = client.get_channel(1195764301538000997)
        embed2 = discord.Embed(title=f"suggest by {ctx.author}", colour=discord.Colour.blue())
        embed2.add_field(name="Server", value=f"{ctx.guild.name}")
        embed2.add_field(name="suggest", value=f"{message}")
        if ctx.guild.icon:
            embed2.set_thumbnail(url=ctx.guild.icon.url)
        await channel.send(embed=embed2)


@client.command()
async def helpme(ctx, *, message=None):
    if message == None:
        await ctx.send(f"there is no message.")
    else:
        await ctx.send("Thank you for reporting this helpme XyPz Will see it!")

        channel = client.get_channel(1195763758962843738)
        embed2 = discord.Embed(title=f"helpme by {ctx.author}", colour=discord.Colour.blue())
        embed2.add_field(name="Server", value=f"{ctx.guild.name}")
        embed2.add_field(name="helpme", value=f"{message}")
        if ctx.guild.icon:
            embed2.set_thumbnail(url=ctx.guild.icon.url)
        await channel.send(embed=embed2)


@client.command()
async def lock(ctx, channel: discord.TextChannel = None):
    try:
        if ctx.author.guild_permissions.manage_channels:
            channel = channel or ctx.channel
            overwrite = channel.overwrites_for(ctx.guild.default_role)
            overwrite.send_messages = False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
            s = await ctx.send(embed=discord.Embed(title=f"Locked.", description=f"by {ctx.author.display_name}\n"
                                                                                 f"x!help for commands .",
                                                   color=0xFF0000)
                               )
            await sleep(5)
            await s.delete()
            await sleep(5)
        else:
            s = await ctx.send(embed=discord.Embed(title=f"access denied?", description=f"your access denied !\n"
                                                                                        f"reseon : you dont have **ban_members** permission .\n"
                                                                                        f"x!help for commands .",
                                                   color=0xFF0000)
                               )
            await sleep(5)
            await s.delete()
            await sleep(5)

    except discord.errors.Forbidden:
        embed = discord.Embed(title=f"No perm",
                              description=f"Xenon Development Community has no permission to manage channels\n"
                                          f"x!help for commands .", color=0xFF0000)
        await ctx.send(embed=embed)


@client.command()
async def unlock(ctx, channel: discord.TextChannel = None):
    try:
        if ctx.author.guild_permissions.manage_channels:
            channel = channel or ctx.channel
            overwrite = channel.overwrites_for(ctx.guild.default_role)
            overwrite.send_messages = True
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
            await ctx.send(f"{channel.mention} unlocked!")
        else:
            s = await ctx.send(embed=discord.Embed(title=f"access denied?", description=f"your access denied !\n"
                                                                                        f"reseon : you dont have **ban_members** permission .\n"
                                                                                        f"x!help for commands .",
                                                   color=0xFF0000)
                               )
            await sleep(5)
            await s.delete()
            await sleep(5)
    except discord.errors.Forbidden:
        embed = discord.Embed(title=f"Xenon Development Community need access",
                              description=f"Xenon Development Community has no permission to manage channels\n"
                                          f"x!help for commands .", color=0xFF0000)
        await ctx.send(embed=embed)


@client.command()
async def role(ctx, args, member: discord.Member, role: discord.Role):
    if not ctx.author.guild_permissions.manage_channels:
        s = await ctx.send(embed=discord.Embed(title=f"access denied?", description=f"your access denied !\n"
                                                                                    f"reseon : you dont have **ban_members** permission .\n"
                                                                                    f"x!help for commands .",
                                               color=0xFF0000)
                           )
        await sleep(5)
        await s.delete()
        await sleep(5)
        return
    try:
        args = args.lower()

        if args == 'add':
            if role == ctx.author.top_role:
                s = await ctx.send("his weanie is much bigger than yours is")
                await sleep(5)
                await s.delete()
                await sleep(5)
                return

            if role in member.roles:
                s = await ctx.send("he got this in his basement, already")
                await sleep(5)
                await s.delete()
                await sleep(5)
                return

            if role.position >= ctx.guild.me.top_role.position:
                s = await ctx.send(f"his weanie is much bigger than mine is")
                await sleep(5)
                await s.delete()
                await sleep(5)
                return

            await member.add_roles(role)
            s = ctx.send(f"I've added {member.mention} the role {role.mention}")
            await sleep(5)
            await s.delete()
            await sleep(5)

        elif args == 'remove':

            if role == ctx.author.top_role:
                return await ctx.send("his weanie is much bigger than yours is")

            if role not in member.roles:
                return await ctx.send("he got none of this in his basement, LeAvE hIm AlOnE")

            if role.position >= ctx.guild.me.top_role.position:
                return await ctx.send(f"his weanie is much bigger than mine is")

            await member.remove_roles(role)
            await ctx.send(f"I have removed {member.mention} the role {role.mention}")
    except discord.errors.Forbidden:
        s = discord.Embed(title=f"No perm",
                              description=f"i need manage members perm.\n"
                                          f"x!help for commands .", color=0xFF0000)
        await ctx.send(embed=s)
        await s.add_reaction('\u2705')
        await s.add_reaction('\u274c')


@client.command()
async def join(ctx):
    await ctx.message.delete()
    if (ctx.author.voice):
        s = discord.Embed(title=f"connected", description=f"voice connected\n"
                                                              f"x!help for commands .", color=0xFF0000)
        await ctx.send(embed=s)
        channel = ctx.author.voice.channel
        await channel.connect()

        await s.add_reaction('\u2705')
        await s.add_reaction('\u274c')
    else:
        s = discord.Embed(title=f"you arent in a voice", description=f"join a voice for connect\n"
                                                                         f"x!help for commands .", color=0xFF0000)
        await ctx.send(embed=s)
        await s.add_reaction('\u2705')
        await s.add_reaction('\u274c')


@client.command()
async def leave(ctx):
    await ctx.message.delete()
    s = discord.Embed(title=f"disconnected", description=f"leaved\n"
                                                             f"x!help for commands .", color=0xFF0000)
    await ctx.send(embed=s)
    await ctx.voice_client.disconnect()
    await s.add_reaction('\u2705')
    await s.add_reaction('\u274c')


@client.command()
async def vote(ctx, *, message=None):
    await ctx.message.delete()
    if message is None:
        await ctx.send(f"no message to vote for.")
    else:
        s = discord.Embed(title=f"Vote By {ctx.author}", colour=discord.Colour.blue())
        s.add_field(name="Vote For :", value=f"{message}")
        if ctx.guild.icon:
            s.set_thumbnail(url=ctx.guild.icon.url)
        await ctx.send(embed=s)
        await s.add_reaction('\u2705')
        await s.add_reaction('\u274c')


@client.command()
async def send(ctx, *, message=None):
    await ctx.message.delete()
    if message is None:
        await ctx.send("No message to send.")
    elif ctx.author.guild_permissions.manage_channels:
        embed2 = discord.Embed(title=f"A message From {ctx.guild.name}", colour=discord.Colour.blue())
        embed2.add_field(name="Message :", value=message)
        if ctx.guild.icon:
            embed2.set_thumbnail(url=ctx.guild.icon.url)
        s = await ctx.send(embed=embed2)
        await s.add_reaction('\u2705')
        await s.add_reaction('\u274c')


client.run(token)
