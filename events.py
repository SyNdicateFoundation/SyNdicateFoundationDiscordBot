import time

import discord
import openai
from discord.ext import commands


class Events(commands.Cog):
    queues = {
    }

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message: discord.message.Message):
        message.content = message.content.lower()
        await self.handle_input(message)

    async def handle_input(self, message: discord.Message):
        if message.author.bot: return
        if message.channel.id == 1409448237882146898:
            if not message.author.name in self.queues:
                self.queues[message.author.name] = {"message": message.content, "lastqueue": int(time.time() * 1000)}
            for user_name, user_data in self.queues.items():
                req, ttime = user_data['message'], user_data['lastqueue']
                if int(time.time() * 1000) - ttime > 30000:
                    await message.channel.send(
                        f"please wait before you queue again. you should wait {int(ttime.time() * 1000) - ttime}")
                    return
                else:
                    self.queues.pop(message.author.name)
                    await self.getchatgptanswer(message)

    async def getchatgptanswer(self, message: discord.Message):

        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "developer", "content": "is SyNdicateFoundation bot"},
                {
                    "role": "user",
                    "content": message.content,
                },
            ],
        )
        return response['choices'][0]['message']['content']

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        bot_entry = await guild.audit_logs(action=discord.AuditLogAction.bot_add).flatten()
        join = discord.Embed(title="Thanks for adding our bot!", colour=discord.Colour.blue(),
                             )
        try:
            await bot_entry[0].user.send(embed=join)
        except discord.errors.Forbidden:
            try:
                await guild.system_channel.send(embed=join)
            except:
                pass
