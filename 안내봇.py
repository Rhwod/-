from http import server
from math import fabs
import numbers
import discord, asyncio, datetime, pytz

client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행됬을 때
    print("5-6 안내봇이 실행되었습니다!")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("작동 안하는 내 코드~"))

@client.event
async def on_message(message):
    if message.content == "안내야 도움말":
        await message.channel.send ("{}, DM으로 안내를 전송했어요! 확인해보세요!".format(message.author.mention))
        await message.author.send ("{}님 안녕하세요! 안내봇이에요! 이 서버에 대해 궁금한게 있으면 뭐든지 저에게 물어보세요!".format(message.author.mention, message.author))
    
    if message.content == "안내야 서버 인원 수":
        await message.channel.send ("지금 {ctx.guild.name} 서버에는 22명의 사용자가 있어요!")


# 그냥 토큰이다
client.run('')

# 근데 굳이 내 깃헙에 와서 이걸 읽는 이상한 사람이 있진 않겠지?