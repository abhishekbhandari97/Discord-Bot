import discord
from discord.ext import commands

client = commands.Bot(command_prefix= '.')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def hello(ctx):
    await ctx.send('Hello!')    

@client.command()
async def ping(ctx):
    await ctx.send(f' Pong {round(client.latency *1000)}ms')

@client.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = amount)

@client.command()
async def pic(ctx):
    await ctx.send(file = discord.File("t1.png"))

@client.command()
async def youtube(url):
    await url.send("https://www.youtube.com/watch?v=Tc0tLGWIqxA&list=RDTc0tLGWIqxA&start_radio=1")



@client.command()
async def bye(ctx):
    await ctx.send('Bye!')  

client.run('token')