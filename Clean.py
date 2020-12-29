import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands import has_permissions
import os

class Clean(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = '청소')
    @commands.has_permissions(manage_messages=True)
    async def 청소(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send("메세지 " + str(int(amount + 1)) + "개를 삭제했습니다.")

def setup(bot):
    bot.add_cog(Clean(bot))