from email import message
from http import server
from lib2to3.pgen2.token import AWAIT
from math import fabs
from discord.utils import get
from discord.ext import commands # New import
import numbers
import discord, asyncio, datetime, pytz
import os

# 주석은 수정이 필요한 코드에만 있습니다.
# 테스트 명령어는 `안내야` 가 아닌 `*안내야` 로 시작합니다. 

client = discord.Client()
client2 = commands.Bot(command_prefix="*")


GuildName = "`5학년 6반 수다수다`" # 디스코드 서버 이름
MemberCount = 22 #디스코드 서버 멤버 수
BotMadeby = "`꼬쟁 (양하율)#1582`" #봇 만든 사람 이름

GuildName = "`Servername`"
MemberCount = 22
BotMadeby = "`꼬쟁 (양하율)#1582`"

CommandCount = 16 #명령어 개수
CommandList = "`안내야 도움말`, `안내야 서버 인원 수`, `안내야 멈춰!`, `안내야 바보`, `안내야 샌즈`, `안내야 안내는 누가 만들었어?`, `안내야 깃허브`, `안내야 뭐해?`" #명령어 종류

@client.event
async def on_ready(): # 봇이 실행됬을 때
    print("안내봇이 실행되었습니다!")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("안내야 도움말로 도움말을 받아보세요!"))

@client.event
async def on_message(message):
    if message.content == "안내야 도움말":
        await message.channel.send ("{}, DM으로 안내를 전송했어요! 확인해보세요!".format(message.author.mention))
        await message.author.send ("{}님 안녕하세요! 저에게는 {}개의 명령어가 있고 계속 추가됩니다!".format(message.author.mention, CommandCount))
    
    if message.content == "안내야 서버 인원 수":
        await message.channel.send ("지금 {} 서버에는 {}명의 사용자가 있어요!".format(GuildName, MemberCount))

    if message.content == "안내야 멈춰!":
        await message.channel.send ("{}님도 멈취!".format(message.author.mention))

    if message.content == "안내야 바보":
        await message.channel.send ("안내는 바보 아니거든요!")

    if message.content == "안내야 샌즈":
        await message.channel.send ("와! 샌즈! 언더태일! 아시는구나! 참고로 그거 겁나 어렵습니다")

    if message.content == "안내야 안내는 누가 만들었어?":
        await message.channel.send ("`꼬쟁 (양하율)#1582` 님이 만들어주셨어요!")
    
    if message.content == "안내야 안녕":
        await message.channel.send ("{}님 안녕하세요!".format(message.author.mention))

    if message.content == "안내야 깃허브":
        await message.channel.send ("안내의 코드는 `꼬쟁 (양하율)#1582` 님의 깃허브에 올라와있어요!")

    if message.content == "안내야 뭐해?":
        await message.channel.send ("안내는 지금 {}님과 대화하고 있어요!".format(message.author.mention))

    if message.content == "안내야 뭐해":
        await message.channel.send ("안내는 지금 {}님과 대화하고 있어요!".format(message.author.mention))

    if message.content == "안내야":
        await message.channel.send ("저 부르셨어요?")

    if message.content == "안내야 꺼져":
        await message.channel.send ("안내는 계속 여기 있을거거든요! 😣")
    
    if message.content == "안내야 가자":
        await message.channel.send ("어디가요? 주어가 없잖아요!")

    if message.content == "안내야 꼬쟁":
        await message.channel.send ("저를 만들어주신 분 닉네임 이에요! 봇 관련 문의 사항이 있으면 {}에게 보내주세요!".format(BotMadeby))

    if message.content == "안내야 토큰":
        await message.channel.send ("제 토큰은 ODk... 잠깐만요! 그걸 왜 물어보세요!")

    if message.content == "안내야 어쩔티비":
        await message.channel.send ("저쩔티비")

    if message.content == "안내야 저쩔티비":
        await message.channel.send ("뇌절티비 쿠루루삥뽕 아무것도 못하죠?")

    if message.content == "안내야 임베드":
        embed = discord.Embed(title="서버 현황", description="서버의  현재 멤버 수 등을 알려줘요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)

        embed.add_field(name="서버 이름", value=GuildName, inline=True)
        embed.add_field(name="서버 인원 수", value=MemberCount, inline=True)

        embed.add_field(name="서버 관리자", value="`이름이#9486`", inline=False)
        embed.add_field(name="서버 관리자 2", value=BotMadeby, inline=True)

        embed.set_footer(text="Bot Made by. 꼬쟁 (양하율)#1582", icon_url="https://cdn.discordapp.com/avatars/471661032335474689/c0df8484dcfac6d28838d4aea4674a1a.webp?size=128")
        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/898441706750476298/f2737612adf6b59401abc3401b5f5b99.webp?size=96")
        await message.channel.send (embed=embed)
    





# 그냥 토큰이다
client.run('')

# 근데 굳이 내 깃헙에 와서 이걸 읽는 이상한 사람이 있진 않겠지?
