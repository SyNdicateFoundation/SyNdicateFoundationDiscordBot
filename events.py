import time

import discord
import openai
from discord.ext import commands



class Events(commands.Cog):
    queues = {}

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message: discord.message.Message):
        message.content = message.content.lower()
        await self.handle_input(message)

    async def handle_input(self, message: discord.Message):
        if message.author.bot: return
        if message.channel.id == 1200147835648221296:
            self.queues[message.author.name]["message"] = message.content
            self.queues[message.author.name]["lastqueue"] = int(time.time() * 1000)
            return
        await self.client.process_commands(message)

    async def getchatgptanswer(self, message: discord.Message):
        for user_name, user_data in self.queues.items():
            req, time = user_data['message'], user_data['lastqueue']
            if int(time.time() * 1000) - time > 30000:
                await message.channel.send(f"please wait before you queue again. you should wait {int(time.time() * 1000) - time}")
                return

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
        return response['choices'][0]['message']['content']
