import discord
import discord.ext.commands  as commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()

token= os.getenv('DISCORD_TOKKEN')

handler= logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True


bot = commands.Bot(command_prefix='!', intents=intents)

secret_role= "hinata"
#!hello 
#events
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.name}')

@bot.event 
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='general')
    if channel:
        await channel.send(f'Welcome to the server, {member.mention}!')
        
@bot.event 
async def on_message(message):
    if message.author == bot.user:
        return
    if "shit" in message.content.lower():
        await message.delete()
        await message.channel.send(f'{message.author.mention}, please watch your language!')
        
        
    if message.content.startswith('how are you bot'):
        await message.channel.send(f'I am doing great thanks!, {message.author.mention}!')
    await bot.process_commands(message)


#!hello
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}!')


@bot.command()
async def goodbye(ctx):
    await ctx.send(f'Goodbye, {ctx.author.mention}!')

@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name=secret_role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f'{ctx.author.mention}, you have been assigned the {secret_role} role!')
    else:
        await ctx.send('Role not found.')
        
        
@bot.command()

async def remove(ctx): 
    role = discord.utils.get(ctx.guild.roles, name=secret_role)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f'{ctx.author.mention}, you have been removed from the {secret_role} role!')
    else:
        await ctx.send('Role not found.')

 
@bot.command()
async def  dm(ctx):
    try:
        await ctx.author.send(f'Hello {ctx.author.mention}, this is a DM from the bot!')
        await ctx.send(f'{ctx.author.mention}, I have sent you a DM!')
    except discord.Forbidden:
        await ctx.send(f'Sorry, {ctx.author.mention}, I cannot send you a DM. Please check your privacy settings.')
        
@bot.command()
async def reply(ctx):
    await ctx.send(f'{ctx.author.mention}, this is a reply to your message!')
    
@bot.command()
async def poll(ctx, *, question):
    embed = discord.Embed(title="New Poll", description=question)
    poll_message = await ctx.send(embed=embed)
    await poll_message.add_reaction("👍")
    await poll_message.add_reaction("👎")


@bot.command()
@commands.has_rolde(secret_role)
async def secret(ctx):
    await ctx.send(f'Welcome to the wyl, {ctx.author.mention}! You have access to this command because you have the {secret_role} role.')


@secret.error
async def secret_error(ctx, error):
    if isinstance(error, commands.MissingRole):
      await ctx.send(f'Sorry, {ctx.author.mention}, you do not have the required role to access this command.')
bot.run(token, log_handler=handler, log_level=logging.DEBUG)


