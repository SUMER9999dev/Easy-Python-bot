import discord
import random
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, MissingRequiredArgument
from colorama import init, Fore
init()
client = commands.Bot(command_prefix = '#')
token = "Token here!"
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(name="#commands | bot by SUMER"))
    print(Fore.CYAN + "bot ready")
@client.event
async def on_member_join(member):
       print(Fore.YELLOW + f"{member} has joined to server!")
@client.event
async def on_member_remove(member):
    print(Fore.RED + f"{member} leave from server :C")
@client.event
async def on_member_ban(guild, user):
    print(Fore.RED + f"{user} has banned in {guild}")

@client.command()
async def ping(ctx):
    await ctx.send(f"pong! ms - {round(client.latency * 1000)}")
@client.command(aliases=['8ball'])
async def eightball(ctx, *, question):
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
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")
@client.command()
@has_permissions(manage_channels=True)
async def clear(ctx, amount=5):
    if ctx.author.bot != True:
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"{amount} messages deleted!")
    else:
        await ctx.send("Bots cant use this command!")
@clear.error
async def clear_error(error, ctx):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await ctx.send(text)
@client.command(name="say")
@has_permissions(administrator=True)
async def _say(ctx, *, message):
    if ctx.author.bot != True:
        await ctx.channel.purge(limit=1)
        await ctx.send(message)
    else:
        await ctx.send("Bots cant use this command!")
@_say.error
async def say_error(error, ctx):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await ctx.send(text)
@client.command(name="ban")
@has_permissions(ban_members=True)
async def _ban(ctx, member : discord.Member, *, reason=None):
    if ctx.author.bot != True:
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} has banned!")
    else:
        await ctx.send("Bots not allowed!")
@_ban.error
async def ban_error(error, ctx):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await ctx.send(text)
    if isinstance(error, MissingRequiredArgument):
        text = "Sorry {}, missed arguments :<".format(ctx.message.author)
        await ctx.send(text)
@client.command(name="kick")
@has_permissions(kick_members=True)
async def _kick(ctx, member : discord.Member, *, reason=None):
    if ctx.author.bot != True:
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} has kicked!")
    else:
        await ctx.send("bots cant use this command!")
@_kick.error
async def kick_error(error, ctx):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await ctx.send(text)
    if isinstance(error, MissingRequiredArgument):
        text = "Sorry {}, missed arguments :<".format(ctx.message.author)
        await ctx.send(text)
@client.command(name="commands")
async def _commands(ctx):
    embed = discord.Embed(title="Commands!", description = "bot prefix is #\nping - return pong and ms\n8ball - #8ball {question} return random answer\nclear - clear messages purge messages\nsay - say text bot send text\nban - #ban {user} {reason} ban user\nkick - #kick {user} {reason} kick user", colour = 0x8df542)
    await ctx.send(embed=embed)
# i know python :V
client.run(token)