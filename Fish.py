import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot
import random
from dbjson import Database

class Fish(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = '낚시')
    async def 낚시(self, ctx):
        money_db = Database('database/Money.json')
        if str(ctx.author.id) in money_db:
            pass
        elif str(ctx.author.id) not in money_db:
            embed = discord.Embed(title = '회원 가입 진행', description = '회원 정보를 찾을 수 없습니다. \n회원가입을 진행합니다..', colour = 0xFF00, inline=True)
            embed.add_field(name = '이용 약관 동의', value = '아래의 이용약관을 읽고, \n이용약관에 동의하시면 회원가입이 완료됩니다. \n\n [이용약관](<https://cafe.naver.com/teampeanut/2>) [개인정보처리방침](<https://cafe.naver.com/teampeanut/3>)')
            a = await ctx.send(embed=embed)
            await a.add_reaction('⭕')
            await a.add_reaction('❌')
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '⭕'
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                money_db[ctx.author.id] = '0'
                money_db.commit()
                pass
            except asyncio.TimeoutError:
                embed = discord.Embed(title = '시간 초과', description = '시간이 초과되었습니다. \n`+낚시` 명령어로 다시 회원가입을 진행해주세요.')
                
        embed = discord.Embed(title = '낚시 시작', description = '낚시를 시작합니다. \n아래에서 자세한 정보를 확인하세요!')
        list_fishing_hole = ['독도', '제주도', '울릉도', '강원도', '부산']
        fishing_hole = random.choice(list_fishing_hole)
        embed.add_field(name = '낚시터', value = f'현재 낚시터 : {fishing_hole}')
        await ctx.send(embed=embed)
        await asyncio.sleep(5)
        msg = embed = discord.Embed(title = '기다리는 중입니다...', description = '물고기가 잡히길 기다리는 중 입니다.\n최대 1분이 소요됩니다.', colour = 0xFF00, inline=True)
        await ctx.send(embed=embed)
        cool_time = random.randint(1, 60)
        await asyncio.sleep(cool_time)
        random_fish_list = ['붕어', '빙어', '도미', '참돔', '소라', '미역', '말미잘', '전갱이', '다금바리', '참치', '갈치', '고등어', '능성어', '철갑돔', '히라스', '우럭', '흑치', '쥐돔', '닭새우', '진주', '한치', '오징어']
        A_fish_list = ['능성어', '히라스', '진주', '다금바리', '갈치', '닭새우', '참치', '진주']
        B_fish_list = ['붕어', '빙어', '도미', '참돔', '말미잘', '전갱이', '고등어', '철갑돔', '우럭', '흑치', '쥐돔']
        C_fish_list = ['소라', '미역', '오징어', '한치']

        fish = random.choice(random_fish_list)
        await ctx.delete_message(msg)
        if fish in A_fish_list:
            price = random.randint(500, 700)
            grade = 'A급'
            embed = discord.Embed(title = '물고기를 잡았습니다!', description = '물고기를 잡았습니다. \n자세한 정보는 아래에서 확인하세요.', colour = 0xFF00, inline=True)
            embed.add_field(name = '생선 이름', value = f'생선 이름 : {fish}')
            embed.add_field(name = '생선 가격', value = f'생선 가격 : {price}')
            embed.add_field(name = '생선 등급', value = f'생선 등급 : {grade}')
            await ctx.send(embed=embed)
            money_db[str(ctx.author.id)] = money_db[int(ctx.author.id)] + int(price)
            money_db.commit()
        if fish in B_fish_list:
            price = random.randint(300, 500)
            grade = 'B급'
            embed = discord.Embed(title = '물고기를 잡았습니다!', description = '물고기를 잡았습니다. \n자세한 정보는 아래에서 확인하세요.', colour = 0xFF00, inline=True)
            embed.add_field(name = '생선 이름', value = f'생선 이름 : {fish}')
            embed.add_field(name = '생선 가격', value = f'생선 가격 : {price}')
            embed.add_field(name = '생선 등급', value = f'생선 등급 : {grade}')
            await ctx.send(embed=embed)
            money_db[str(ctx.author.id)] = money_db[int(ctx.author.id)] + int(price)
            money_db.commit()
        if fish in C_fish_list:
            price = random.randint(100, 300)
            grade = 'C급'
            embed = discord.Embed(title = '물고기를 잡았습니다!', description = '물고기를 잡았습니다. \n자세한 정보는 아래에서 확인하세요.', colour = 0xFF00, inline=True)
            embed.add_field(name = '생선 이름', value = f'생선 이름 : {fish}')
            embed.add_field(name = '생선 가격', value = f'생선 가격 : {price}')
            embed.add_field(name = '생선 등급', value = f'생선 등급 : {grade}')
            await ctx.send(embed=embed)
            money_db[str(ctx.author.id)] = money_db[int(ctx.author.id)] + int(price)
            money_db.commit()


    
def setup(bot):
    bot.add_cog(Fish(bot))