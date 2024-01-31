import datetime
import discord
from discord.ext import commands
from asyncio import sleep


class BaseCommands(commands.Cog):
    def __init__(self, client, starttime):
        self.client = client
        self.starttime = starttime

    @commands.command()
    async def help(self, ctx: commands.Context):
        await ctx.send(embed=discord.Embed(title=f"Help", description=f"> :nerd~1: Help\n"
                                                                      f"{ctx.author.name}\n"
                                                                      f"invite_link\n"
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

    @commands.command()
    async def stats(self, ctx: commands.Context):
        member_count = len(ctx.guild.members)
        realmembers = len([m for m in ctx.guild.members if not m.bot])
        embed = discord.Embed(title=f"Xenon Development Community's bot stats",
                              description=f"servers : {len(self.client.guilds)}\n"
                                          f"members : {member_count}\n"
                                          f"ping : {round(self.client.latency * 1000)}\n"
                                          f"real members : {round(realmembers)}"
                                          f"x!help for commands", color=0x0B5394)
        await ctx.send(embed=embed)

    @commands.command()
    async def invite_link(self, ctx: commands.Context):
        await ctx.send("""https://discord.gg/BzY7hf2ACD""")

    @commands.command()
    async def ping(self, ctx: commands.Context):
        try:
            s = await ctx.send(embed=discord.Embed(title=f"Ping", description=f"perfoming test ...\n"
                                                                              f"x!help for commands",
                                                   color=0x0B5394)
                               )
            await sleep(5)
            await s.delete()
            await sleep(5)
            s = await ctx.send(
                embed=discord.Embed(title=f"Ping", description=f"test 1 : {round(self.client.latency * 1000)} ms\n"
                                                               f"test 2 : {round(self.client.latency * 1000)} ms\n"
                                                               f"test 3 : {round(self.client.latency * 1000)} ms\n"
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

    @commands.command()
    async def uptime(self, ctx: commands.Context):
        uptime = datetime.datetime.utcnow() - self.starttime
        hour = str(uptime).split('.')[0]
        await ctx.send(embed=discord.Embed(title="Uptime",
                                           description=f"{uptime}",
                                           color=discord.Colour.blue()))

    @commands.command()
    async def serverlist(self, ctx: commands.Context):
        if ctx.author.id == 1042894447815430229:
            msg = "\n".join(f"{x}" for x in self.client.guilds)
            s = await ctx.send(embed=discord.Embed(title=f"server list", description=f"```\n{msg}\n```\n"
                                                                                     f"x!help for commands",
                                                   color=0x57ff36)
                               )
            await sleep(5)
            await s.delete()
            await sleep(5)
        else:
            s = await ctx.send(
                embed=discord.Embed(title=f"Only dev can use this.", description=f"this is only owner command .\n"
                                                                                 f"x!help for commands", color=0x57ff36)
            )
            await sleep(5)
            await s.delete()
            await sleep(5)
