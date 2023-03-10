import discord
from discord.ext import commands

intents= discord.Intents.all()

bot = commands.Bot(command_prefix="/",intents = intents)




@bot.event
async def on_ready():
    print(">>bot is online<<")

@bot.event 
async def on_member_join(member):
    channel = bot.get_channel()
    await channel.send(f'{member}join!') 
    

@bot.event 
async def on_member_remove(member):
    channel = bot.get_channel()
    await channel.send(f'{member}leave!') 

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

@bot.listen()
async def on_message(msg):
    if msg.content == "hi":
        await msg.channel.send("hi")

bot.run("MTA4MjI0Nzk0MzEyMzM4NjM4OA.GayRnC.BNbLNDASw_j5KdgKKRDoxSTuZW6XBV-4xrtTcA")