from email import message
from http import server
from lib2to3.pgen2.token import AWAIT
from math import fabs
from discord.utils import get
from discord.ext import commands # New import
import numbers
import discord, asyncio, datetime, pytz

client = discord.Client()
client2 = commands.Bot(command_prefix="*")

GuildName = "`Servername`"
MemberCount = 22
BotMadeby = "`꼬쟁 (양하율)#1582`"

CommandCount = 8
CommandList = "`안내야 도움말`, `안내야 서버 인원 수`, `안내야 멈춰!`, `안내야 바보`, `안내야 샌즈`, `안내야 안내는 누가 만들었어?`, `안내야 깃허브`"

@client.event
async def on_ready(): # 봇이 실행됬을 때
    print("안내봇이 실행되었습니다!")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("안내야 도움말로 도움말을 받아보세요!"))

@client.event
async def on_message(message):
    if message.content == "안내야 도움말":
        await message.channel.send ("{}, DM으로 안내를 전송했어요! 확인해보세요!".format(message.author.mention))
        await message.author.send ("{}님 안녕하세요! 저에게는 {}개의 명령어가 있고 {}의 명령어 들이 있어요! 더 추가하면 좋을거 같은 명령어는 {}에게 DM으로 알려주세요!".format(message.author.mention, CommandCount, CommandList, BotMadeby))
    
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
    




# 그냥 토큰이다
client.run('')

# 근데 굳이 내 깃헙에 와서 이걸 읽는 이상한 사람이 있진 않겠지?
