import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot
import os

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = '도움')
    async def 도움(self, ctx):
        embed = discord.Embed(title = '도움말', description = '땅콩 봇 도움말입니다.', colour = 0xFF00, inline=True)
        embed.add_field(name = '> 유틸리티', value = '`+티켓생성`, `+질문`, `+크레딧`, `+청소`')
        embed.add_field(name = '> 게임', value = '`+낚시`')
        embed.add_field(name = '> 관리 - 개발중', value = '`+차단`, `+킥`')
        await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Help(bot))