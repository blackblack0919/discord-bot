import discord
import requests
import os
from discord.ext import commands
from bs4 import BeautifulSoup
from random import choice
from core.classes import Cog_Extension

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
async def stock(ctx):
    url = (f'https://tw.stock.yahoo.com/quote/2330')
    r = requests.get(url) 
    soup = BeautifulSoup(r.text, 'html.parser')
    await ctx.send(soup.fint("span", class_="Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)"))

class draw(Cog_Extension):
    @commands.command()
    async def draw(self,ctx):
        member_list = []
        guild = self.bot.get_guild(int(self.GUILDID_TOKEN))
        for user in guild.members:            
            if str(user.status) != "offline":
                member_list.append(f"<@{user.id}>")
        await ctx.message.reply(choice(member_list))

bot.run("MTA4NjU0NDQ1NjIyMTc0MTExNg.GZ1-3M.o1leIDU-gsM9YwPbSZLftkyMlRVaQxevwayiyM")
