import discord
from discord.ext import commands

class Developer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = '크레딧')
    async def 개발자(self, ctx):
        embed = discord.Embed(title = '땅콩 봇 개발자', description = '땅콩 봇의 개발자 목록입니다.', colour = 0xFF00, inline=True)
        embed.add_field(name = '`총관리자`', value = '땅콩#7610')
        embed.add_field(name = '`디자이너`', value = '명암없는 그림 전문 햄버그#7128')
        embed.add_field(name = '`아이디어 제공`', value = '호두과자#8981')
        await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Developer(bot))
