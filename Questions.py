import discord
from discord.ext import commands

class Questions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = '질문')
    async def 질문(self, ctx):
        embed = discord.Embed(title = '질문 [자주 묻는 질문]', description = '자주 묻는 질문을 모았습니다.')
        embed.add_field(name = '> Q. 티켓 생성이 안됩니다.', value = 'A. 땅콩 봇 권한을 다시 설정해주세요.\n채널 생성, 이모지 관련한 권한이 허용되어야 합니다.')
        embed.add_field(name = '> Q. 기타 문의는 어디서 하나요?', value = '기타 문의는 `땅콩#7610` 으로 연락주시면 감사하겠습니다.\n항상 땅콩 봇을 이용해주셔서 감사드립니다.')
    
def setup(bot):
    bot.add_cog(Questions(bot))
