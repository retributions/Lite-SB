#BE SURE TO SEE THE LITEINFO.TXT


import discord
from discord.ext import commands, tasks
import time
import requests
import asyncio
import json
import random
from os import system, name
import colorama
from colorama import init, Fore, Style, Back
from colorama import Fore, Back, Style
import threading
from threading import Thread

from discord import Webhook, AsyncWebhookAdapter
from discord import Permissions

with open("lite.json") as f:
 lite = json.load(f)

token = lite.get("token")
prefix = lite.get("prefix")



intents=discord.Intents.all()

client = discord.Client()

client = commands.Bot(command_prefix = prefix, self_bot = True,intents=intents, case_insensitive=True)




client.copycat = None






client.remove_command('help')


@client.event
async def on_ready():
  print(f'''
            {Fore.CYAN}╦  ┬┌┬┐┌─┐
            {Fore.RED}║  │ │ ├┤ 
            {Fore.WHITE}╩═╝┴ ┴ └─┘ 
{Fore.WHITE}═════════════════════════════════════
{Fore.BLUE}[<>] Logged in as:{Fore.RED} {client.user.name}#{client.user.discriminator}
{Fore.BLUE}[<>] ServerCount: {len(client.guilds)}
{Fore.BLUE}[<>] Prefix: {Fore.GREEN}{client.command_prefix}
{Fore.WHITE}═════════════════════════════════════
{Fore.YELLOW}[<>] Powered By Lite™
{Fore.WHITE}═════════════════════════════════════
  
  
  ''')
 

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
     await ctx.send('`[X] Error: Command Not Found`')

@client.command()
async def dfarm(ctx, *args):
    await ctx.message.delete()
    retStr = str(f"""```css\n💰 {client.command_prefix}f1 - Dank Farming (Basic)\n\n💰 {client.command_prefix}f2 - Dank Farming (Gambling Loop)\n\n💰 {client.command_prefix}quit - Shuts Down Selfbot```""")
    embed = discord.Embed(color=0xfffafa,title="Lite Selfbot💡")
    embed.add_field(name="💰 Dank Memer Farming 💰",value=retStr)
    embed.set_footer(text=f'Powered By Lite™')

    await ctx.send(embed=embed)

@client.command()
async def help(ctx, *args):
    await ctx.message.delete()
    retStr = str(f"""```css\n👉 {client.command_prefix}dfarm - Dank Memer Farming\n\n👉 {client.command_prefix}utils - Useful Commands\n\n👉 {client.command_prefix}fun - Fun Commands\n\n👉 {client.command_prefix}status - Custom Status Commands\n\n👉 {client.command_prefix}calc - Shows Calculator Commands\n\n👉 {client.command_prefix}quit - Shutsdown Selfbot```""")
    embed = discord.Embed(color=0xfffafa,title="Lite Selfbot💡")
    embed.add_field(name="Calculator",value=retStr)
    embed.set_footer(text=f'Powered By Lite™')

    await ctx.send(embed=embed)

@client.command()
async def utils(ctx, *args):
    await ctx.message.delete()
    retStr = str(f"""```css\n👉 {client.command_prefix}mute/unmute - Mute/Unmute Mentioned User\n\n👉 {client.command_prefix}ban/kick - Bans/Kicks Mentioned User\n\n👉 {client.command_prefix}lock/unlock - Locks/Unlocks Chat\n\n👉 {client.command_prefix}nickname - Changes Mentioned User Nickname\n\n👉 {client.command_prefix}purge - Purges Any Amount Of Messages```""")
    embed = discord.Embed(color=0xfffafa,title="Lite Selfbot💡")
    embed.add_field(name="Utility",value=retStr)
    embed.set_footer(text=f'Powered By Lite™')

    await ctx.send(embed=embed)

@client.command()
async def fun(ctx, *args):
    await ctx.message.delete()
    retStr = str(f"""```css\n👉 {client.command_prefix}rolldice - Roll a Dice !\n\n👉 {client.command_prefix}coinflip - Heads or Tails ?\n\n👉 {client.command_prefix}av - Shows Avatar In Embed\n\n👉 {client.command_prefix}stealav - Steal Someones Avatar !\n\n👉 {client.command_prefix}ball - (8ball) Ask a Question !```""")
    embed = discord.Embed(color=0xfffafa,title="Lite Selfbot💡")
    embed.add_field(name="Fun",value=retStr)
    embed.set_footer(text=f'Powered By Lite™')

    await ctx.send(embed=embed)

@client.command()
async def calc(ctx, *args):
    await ctx.message.delete()
    retStr = str(f"""```css\n👉 {client.command_prefix}add - Adds Values\n\n👉 {client.command_prefix}subtract - Subtracts Values\n\n👉 {client.command_prefix}divide - Divides Values\n\n👉 {client.command_prefix}multiply - Multiplys Values\n\n👉 example - {client.command_prefix}add 3 3```""")
    embed = discord.Embed(color=0xfffafa,title="Lite Selfbot💡")
    embed.add_field(name="Calculator",value=retStr)
    embed.set_footer(text=f'Powered By Lite™')

    await ctx.send(embed=embed)

@client.command()
async def status(ctx, *args):
    await ctx.message.delete()
    retStr = str(f"""```css\n👉 {client.command_prefix}stream - Custom Streaming Status\n\n👉 {client.command_prefix}game - Custom Playing Status\n\n👉 {client.command_prefix}listen - Custom Listening Status\n\n👉 {client.command_prefix}watch - Custom Watching Status```""")
    embed = discord.Embed(color=0xfffafa,title="Lite Selfbot💡")
    embed.add_field(name="Status",value=retStr)
    embed.set_footer(text=f'Powered By Lite™')

    await ctx.send(embed=embed)



@client.command()
async def f1(ctx):
  await ctx.message.delete()
  msg = await ctx.send(f"pls beg")
  time.sleep(2)
  msg = await ctx.send(f"pls hunt")
  time.sleep(2)
  msg = await ctx.send(f"pls fish")
  time.sleep(2)
  msg = await ctx.send(f"pls pm")
  time.sleep(2)
  msg = await ctx.send(f"f")
  time.sleep(5)
  msg = await ctx.send(f"pls dep all")
  time.sleep(30)
  msg = await ctx.send(f">f1")

@client.command()
async def f2(ctx):
  await ctx.message.delete()
  msg = await ctx.send(f"pls bet 2500")
  time.sleep(7)
  msg = await ctx.send(f">f2")

@client.command()
async def quit(context):
    exit()



@client.command(pass_contex=True)
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == client.user).map(lambda m: m):
        try:
           await message.delete()
        except:
          pass 


@client.command(aliases=["playing"])
async def game(ctx, *, text):
  await ctx.message.delete()
  await client.change_presence(activity=discord.Game (name = text))

@client.command(aliases=["streaming"])
async def stream(ctx, *, text):
    await ctx.message.delete()
    await client.change_presence(activity=discord.Streaming (url = "https://twitch.tv/liteselfbot", name= text))

@client.command(aliases=["listening"])
async def listen(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=message,))

@client.command(aliases=["watching"])
async def watch(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
        ))

@client.command(aliases=["stopstreaming","stoplistening", "stopplaying", "stopwatching"])
async def stopstatus(ctx):
    await ctx.message.delete()
    await client.change_presence(activity=None, status=discord.Status.dnd)



@client.command(aliases=['avatar'])
async def av(ctx,user: discord.Member = None):
  await ctx.message.delete()
  
  if user is None:
    user = ctx.author
  embed=discord.Embed(color=0x000000)
  embed.set_image(url=user.avatar_url)
  embed.set_footer(text=f'Powered By Lite™')
  await ctx.send(embed=embed)

@client.command()
async def stealav(ctx, *,  avamember : discord.Member=None):
    await ctx.message.delete()
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)



@client.command()
async def coinflip(ctx):
  await ctx.message.delete()
  choices = ["`Heads`","`Tails`"]
  rancoin = random.choice(choices)
  await ctx.send(rancoin)


@client.command()
async def rolldice(ctx):
    await ctx.message.delete()
    message = await ctx.send("`Choose a number:`\n**4**, **6**, **8**, **10**, **12**, **20** ")
    
    def check(m):
        return m.author == ctx.author

    try:
        message = await client.wait_for("message", check = check, timeout = 5.0)
        m = message.content

        if m != "4" and m != "6" and m != "8" and m != "10" and m != "12" and m != "20":
            await ctx.send("`Sorry, invalid choice.`")
            return
        
        coming = await ctx.send("`Rolling The Dice`")
        time.sleep(1)
        await coming.delete()
        await ctx.send(f"**{random.randint(1, int(m))}**")
    except asyncio.TimeoutError:
        await message.delete()
        await ctx.send("`Procces has been canceled because you didn't respond in **30** seconds.`")


@client.command(aliases=['8ball'])
async def ball(ctx, *, question):
  await ctx.message.delete()
  responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
  await ctx.send(f'`Question: {question}`\n**Answer: {random.choice(responses)}**')


@client.command()
async def lock(ctx):
    await ctx.message.delete()
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send( ctx.channel.mention + " ***is now on lockdown.***")

@client.command()
async def unlock(ctx):
    await ctx.message.delete()
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send(ctx.channel.mention + " ***has been unlocked.***")



@client.command() 
async def add(ctx, *nums):
    await ctx.message.delete()
    operation = " + ".join(nums)
    await ctx.send(f'{operation} = {eval(operation)}')

@client.command() 
async def subtract(ctx, *nums): 
    await ctx.message.delete()
    operation = " - ".join(nums)
    await ctx.send(f'{operation} = {eval(operation)}')

@client.command() 
async def multiply(ctx, *nums): 
    await ctx.message.delete()
    operation = " * ".join(nums)
    await ctx.send(f'{operation} = {eval(operation)}')

@client.command() 
async def divide(ctx, *nums): 
    await ctx.message.delete()
    operation = " / ".join(nums)
    await ctx.send(f'{operation} = {eval(operation)}')


@client.command(pass_context=True)
async def nickname(ctx, member: discord.Member, nick):
    await ctx.message.delete()
    await member.edit(nick=nick)
    await ctx.send(f'***Nickname was changed for {member.mention} ***')

@client.command(description="Mutes the specified user.")
async def mute(ctx, member: discord.Member, *, reason=None):
    await ctx.message.delete()
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="Mute", description=f"{member.mention} Was Muted ", colour=discord.Colour.light_grey())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f"** You Have Been Muted In: {guild.name} |  Reason: {reason}**")
   
@client.command(description="Unmutes a specified user.")
async def unmute(ctx, member: discord.Member):
   await ctx.message.delete()
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

   await member.remove_roles(mutedRole)
   await member.send(f"**You Have Be Unmuted In: - {ctx.guild.name}**")
   embed = discord.Embed(title="Unmute", description=f" Unmuted - {member.mention}",colour=discord.Colour.light_gray())
   await ctx.send(embed=embed)


@client.command()

async def kick(ctx, member: discord.Member, *, reason=None):

    await member.kick(reason=reason)

    await ctx.send(f'**{member} Was Kicked.**')


@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.channel.send(f"**{member} Was Banned.**")



client.run(token, bot=False)
