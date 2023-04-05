import discord
import requests
import os
from discord.ext import commands
from bs4 import BeautifulSoup
from random import choice

intents= discord.Intents.all()

intents.members = True

bot = commands.Bot(command_prefix="/",intents = intents)

@bot.event
async def on_ready():
    print(f'The bot has been log in as {bot.user}')
    game = discord.Game("水時數")
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.event 
async def on_member_join(member):
    channel = bot.get_channel()
    await channel.send(f'{member}join!') 
    
@bot.event 
async def on_member_remove(member):
    channel = bot.get_channel()
    await channel.send(f'{member}leave!') 

@bot.command()
async def say(ctx, *, word):
    await ctx.message.delete()
    await ctx.send(word)

@bot.command()
async def clear(ctx, num:int):
    await ctx.channel.purge(limit = num+1)

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

@bot.command()
async def receipt(ctx):
    url = 'https://invoice.etax.nat.gov.tw/index.html'
    web = requests.get(url)    
    web.encoding='utf-8'       

    soup = BeautifulSoup(web.text, "html.parser")                   
    td = soup.select('.container-fluid')[0].select('.etw-tbiggest')  
    ns = td[0].getText() 
    n1 = td[1].getText() 
    n2 = [td[2].getText()[-8:], td[3].getText()[-8:], td[4].getText()[-8:]] 
    await ctx.send(ns)
    await ctx.send(n1)
    await ctx.send(n2)

@bot.command()
async def receipt_check(ctx, num):
    url = 'https://invoice.etax.nat.gov.tw/index.html'
    web = requests.get(url)    
    web.encoding='utf-8'       

    soup = BeautifulSoup(web.text, "html.parser")                   
    td = soup.select('.container-fluid')[0].select('.etw-tbiggest')  
    ns = td[0].getText() 
    n1 = td[1].getText() 
    n2 = [td[2].getText()[-8:], td[3].getText()[-8:], td[4].getText()[-8:]] 
    
    if num == ns: await ctx.send('恭喜你對中了1000萬元')
    elif num == n1: await ctx.send('恭喜你對中200萬元')
    for i in n2:
        if num == i:
            await ctx.send('恭喜你對中 20 萬元！')
            break
        elif num[-7:] == i[-7:]:
            await ctx.send('恭喜你對中 4 萬元！')
            break
        elif num[-6:] == i[-6:]:
            await ctx.send('恭喜你對中 1 萬元！')
            break
        elif num[-5:] == i[-5:]:
            await ctx.send('恭喜你對中 4000 元！')
            break
        elif num[-4:] == i[-4:]:
            await ctx.send('恭喜你對中 1000 元！')
            break
        elif num[-3:] == i[-3:]:
            await ctx.send('恭喜你對中 200 元！')
            break

@bot.command()
async def stock(ctx, num):
    url = f'https://tw.stock.yahoo.com/quote/{num}' 
    web = requests.get(url)                         
    soup = BeautifulSoup(web.text, "html.parser")   
    name = soup.find_all('h1')[1]             
    money = soup.select('.Fz\(32px\)')[0]    
    await ctx.send(f'{name.get_text()}: {money.get_text()}') 

@bot.command()
async def money(ctx):
    url = 'https://rate.bot.com.tw/xrt'
    web = requests.get(url)
    web.encoding = 'utf-8'
    soup = BeautifulSoup(web.text, "html.parser")
    for i in range (19):
        name = soup.select('hidden-phone print_show xrt-cur-indent')[i]
        buyin = soup.select('rate-content-cash text-right print_hide')[i]
        soldout = soup.select('rate-content-cash text-right print_hide')[i]
        await ctx.send(f'{name.get_text()} {buyin.get_text()} {soldout.get_text()}')
        
bot.run("token")

#發票的程式碼引用自:https://steam.oxxostudio.tw/category/python/spider/invoice-auto.html
