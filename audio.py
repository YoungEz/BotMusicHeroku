import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time

start_time = time.time()


bot = commands.Bot(command_prefix='t#')
print (discord.__version__)





@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)





@bot.command(pass_context=True)
async def perfil(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Nome", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Melhor role", value=user.top_role)
    embed.add_field(name="entrou no servidor", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}' informações do servidor:".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="BY:彡★ｲЩ乃★彡 Brahma#1111")
    embed.add_field(name="Nome do servidor", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID do servidor", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Total de roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Quantidade de Membros", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_role("ðŸ˜‚ðŸ‘Œ Friends")
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya loser!".format(user.name))
    await bot.kick(user)

@bot.command(pass_context=True)
async def ajuda(ctx):
    embed = discord.Embed(title="The World Of Bad 2.0 Bot", description="Meu comandos são", color=0x00ff00)
    embed.set_footer(text="Bot Oficial do servidor The World Of Bad 2.0")
    embed.set_author(name="Fui criado pelo 彡★ｲЩ乃★彡 Brahma#1111")
    embed.add_field(name="ban", value="bane o usuário", inline=True)
    embed.add_field(name="kick", value="expulsa o usuário", inline=True)
    embed.add_field(name="serverinfo", value="Veja informações do servidor do discord Atual!", inline=True)
    embed.add_field(name="perfil", value="mostra seu perfil!", inline=True)
    embed.add_field(name="ping", value="Veja minha velocidade de resposta!", inline=True)
    await bot.say(embed=embed)
    
@bot.command(pass_context=True)
async def ping(ctx):
    """ Pong! """
    await delete_message(ctx.message)
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong!  `{int(ping)}ms`")
    print(f'Ping {int(ping)}ms')
    
    
bot.run('NTI5OTcyODM4OTM3OTE5NDg4.Dw4nWw.bg-PuX1c0KVHO2zJuSHFFtkq-HU')
