import discord
from discord.ext import commands


class BaseCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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
    async def invite_link(self, ctx: commands.Context):
        await ctx.send("""https://discord.gg/BzY7hf2ACD""")
