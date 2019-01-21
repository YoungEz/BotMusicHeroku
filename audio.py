import discord, time, datetime
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from discord.utils import get
import asyncio
import time
import colorsys
import sys
import subprocess
import os
import json
import traceback
import random
import request


start_time = time.time()


bot = commands.Bot(command_prefix='-')
print (discord.__version__)
bot.remove_command('help')



	
	

@bot.event
async def on_ready():
    print ("Bot FF • DW On")
    print ("quem ta falando é o " + bot.user.name)
    print ("Meu numero do ZipZop: " + bot.user.id)
    while True:
    	await bot.change_presence(game=discord.Game(name='Fui criado pelo El_Brahmaᶠᶸᶜᵏᵧₒᵤ| -ajuda'.format(len(bot.servers)), type=2))
    	await asyncio.sleep(20)
    	await bot.change_presence(game=discord.Game(name=str(len(set(bot.get_all_members())))+ ' soldados DW!', type=3))
    	await asyncio.sleep(10)
    	await bot.change_presence(game=discord.Game(name='FREE FIRE'))


    
@bot.command(pass_context=True)
async def ping(ctx):
	channel = ctx.message.channel
	t1 = time.perf_counter()
	await bot.send_typing(channel)
	t2 = time.perf_counter()
	embed=discord.Embed(title="Pong!", description='Meu Ping {}ms.'.format(round((t2-t1)*1000)), color=0x76FF03)
	embed.set_footer(text ='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial FF • DW')
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def stopmat(ctx):
	stop = discord.Embed(title= 'Desligando...', description='Bot Off para manuteção', color=0xA0bb00)
	stop.add_field(name="Autor do stop", value=ctx.message.author.mention, inline=True)
	await bot.say(embed=stop)
	
@bot.command(pass_context=True)
async def start(ctx):
	start = discord.Embed(title='ligando...', description='Bot online!', color=0xFFFFFF)
	start.add_field(name="Autor Start", value=ctx.message.author.mention, inline=True)
	await bot.say(embed=start)
	
@bot.command(pass_context=True)
async def report(ctx, *, arg, limit: int=1):
	async for msg in bot.logs_from(ctx.message.channel, limit=1):
            try:
                await bot.delete_message (msg)
            except:
                pass
                embed = discord.Embed(title="usuário reportado", description="{} seu reporte foi enviado com sucesso! caso for aprovado o usuário reportado sera punido".format(ctx.message.author.mention), color=0x00ff00)
                await bot.send_message(embed=embed)
                await asyncio.sleep(2)
	canal = bot.get_channel("535829555189907469")
	ms = discord.Embed(title='usuário reportado', color=0x00ff00)
	ms.add_field(name="Autor", value=ctx.message.author.name, inline=True)
	ms.add_field(name="usuário reportado e motivo", value=arg, inline=True)
	await bot.send_message(canal, embed=ms)

@bot.command(pass_context=True)
async def perfil(ctx, user: discord.Member):
	embed = discord.Embed(title="perfil de {}".format(user.name), description="Reflexão: Hoje n tem reflexão :(", color=0x00ff00)
	embed.add_field(name="Nome", value=user.name, inline=True)
	embed.add_field(name="ID do usuário", value=user.id, inline=True)
	embed.add_field(name="Status do usuário", value=user.status, inline=True)
	embed.add_field(name="Melhor cargo", value=user.top_role)
	embed.add_field(name="entrou no servidor", value=user.joined_at)
	embed.set_footer(text ='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial FF • DW')
	embed.set_thumbnail(url=user.avatar_url)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
	server = ctx.message.server
	roles = [x.name for x in
	server.role_hierarchy]
	role_length = len(roles)
	
	if role_length > 50:
		roles = roles[:50]
		roles.append('>>>> [50/%s] Roles'%len(roles))
		roles = ', '.join(roles)
		channelz = len(server.channels);
		time = str(server.created_at); time = time.split(' '); time= time[0];
		join = discord.Embed(description= '%s '%(str(server)),title = 'Nome', color=0x00ff00);
		join.set_thumbnail(url = server.icon_url);
		join.add_field(name = '👑 Dono',
		value = str(server.owner) + '\n' + server.owner.id, inline=True);
		join.add_field(name = '💻ID', value = str(server.id), inline=True)
		join.add_field(name = '👥Total de membros', value = str(server.member_count), inline=True);
		join.add_field(name = '📝Total de canais Texto/voz', value = str(channelz), inline=True);
		join.add_field(name="🎭 Total de roles", value=len(ctx.message.server.roles), inline=True)
		join.add_field(name='🌎 Região', value=server.region, inline=True)
		join.add_field(name ='📆Criado em', value='Data: %s'%time, inline=True);
		
		join.add_field(name='👮Role Top1', value=server.role_hierarchy[0], inline=True);
		await bot.say(embed=join);

@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, userName: discord.User):
	await bot.kick(userName)
	embed = discord.Embed(title='usuário kickado', description='{} usuário kickado com sucesso'.format(ctx.message.author.mention), color=0xff0bb)
	embed.set_footer(text='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial FF • DW')
	await bot.say(embed=embed)
	print ("user has kicked")		
	
				
    
@bot.command(pass_context = True)
async def ajuda(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    
    Piada = 'Sabia que Estou apenas no FREE FIRE DA DEEP WEB', 'Se rosas são vermelhas violetas são azuis?'
    
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Help')
    embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field(name = '``Curiosidade``',value=random.choice(Piada), inline = False)
    embed.add_field(name = '-modhelp ',value ='Comandos de moderação Ex: ban,kick e clear etc...',inline = False)
    embed.add_field(name = '-diversaohelp ',value ='Comandos de diversão e que todos podem usar! Ex: kiss,hug e deathnote.',inline = False)
    embed.set_footer(text='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ | Bot Oficial FF • DW')
    await bot.send_message(author,embed=embed)
    await bot.say('Olhe Sua DM Soldado!')
    
@bot.command(pass_context = True)
async def modhelp(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Comandos Moderação Help')
    embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field(name = '-kick ',value ='como usar ``-kick @usuário`` Expulsa o usuário marcado',inline = False)
    embed.add_field(name = '-ban ',value ='Como usar ``-ban @usuário`` bane o usuário marcado',inline = False)
    embed.add_field(name = '-addrole ',value ='Como usar ``-addrole @role @usuário`` adiciona um determinado cargo ao usuário marcado',inline = False)
    embed.add_field(name = '-removerole',value ='Como usar ``-removerole @role @usuário`` remove um determinado cargo do usuário marcado ',inline = False)
    embed.add_field(name = '-clear',value ='Como usar ``-clear`` apaga as mensagens do canal de texto atual ',inline = False)
    embed.add_field(name = '-avisar',value ='Como usar ``-avisar @usuário`` avisa um usuário no PV ',inline = False)


    await bot.send_message(author,embed=embed)
    await bot.say('Olhe sua DM Seu Platina!')
    
   
   
@bot.command(pass_context=True)
async def diversaohelp(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name = '-flsff ',value ='Como usar ``-flsff`` As falas mais comuns do free fire',inline = False)
    embed.add_field(name = '-kiss ',value ='Como usar ``-kiss @usuário`` O amor esta no ar! beije determinado usuário!',inline = False)
    embed.add_field(name = '-hug ',value ='Como usar ``-hug @usuário`` abrace seu/sua melhor amigo(a).',inline = False)
    embed.add_field(name = '-flipcoin ',value ='Como usar ``-flipcoin`` Cara ou coroa?',inline = False)
    embed.add_field(name = '-deathnote ',value ='Como usar ``-deathnote @usuário`` Escreva o nome de determinado usuário em seu Death Note ',inline = False)
    embed.add_field(name = '-avatar ',value ='Como usar ``-avatar @usuário`` Veja o avatar do usuário',inline = False)
    embed.add_field(name="-sugt", value="como usar ``-sugt <sugestão>`` de uma sugestao de comando!", inline=False)
    embed.add_field(name="-ping", value="como usar ``-ping`` Veja se eu estou lagado!", inline=False)
    embed.add_field(name="-perfil", value="como usar ``-perfil @usuário`` Veja o perfil de um determinado usuário!", inline=True)
     	
     	     	
    await bot.send_message(author,embed=embed)
    await bot.say('Olhe sua DM soldado')
    
    
@bot.command(pass_context=True)
async def avatar(ctx, user: discord.User):
	
	list = (user.avatar_url), (user.avatar_url)
	hug = random.choice(list)
	hugemb = discord.Embed(title='Avatar de {}'.format(user.name), color=0x6A1B9A)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial FF • DW')
	await bot.say(embed=hugemb)    								
  
@bot.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, userName: discord.User):
	await bot.ban(userName)
	embed = discord.Embed(title='usuário banido!', description='{} usuário banido com sucesso'.format(ctx.message.author.mention), color=0xff0Ab)
	embed.set_footer(text='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial FF • DW')
	await bot.say(embed=embed)
	print("user has banned")

@bot.command(pass_context=True)
async def hug(ctx, user: discord.User):
	list = 'https://cdn.discordapp.com/attachments/531090629715951629/532667673943736351/action.gif','https://cdn.discordapp.com/attachments/531090629715951629/532672938596368393/action.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Abraço ❤',  description='**{}** Ele(a) recebeu um abraço de **{}**!! :heart_eyes:'.format(user.name, ctx.message.author.name), color=0x00ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial TOXIC')
	await bot.say(embed=hugemb)  

@bot.command(pass_context=True)
async def kiss(ctx, user: discord.User):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/533253217883258890/tumblr_mie2frAdXc1rfj82jo2_500.gif','https://cdn.discordapp.com/attachments/514045065929162764/533253218860269577/86d4a046c8a32a28341353fc95bedc82.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Beijo! ❤',  description='**{}** recebeu um beijo de **{}**! Casal Fofo! :heart_eyes:'.format(user.name, ctx.message.author.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial FF • DW')
	await bot.say(embed=hugemb)

@bot.command(pass_context=True)
async def deathnote(ctx, user: discord.User):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/534806488531599380/14ae937e622c452bc45e509ed43c8e38a410fc0b_hq.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/533615190273425409/67dc6ce11c0ebe1c723983f18d7f68a8b0d11887_hq.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Death Note 💀',  description='**{}** escreveu o nome de **{}** em seu Death Note'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial FF • DW')
	await bot.say(embed=hugemb)
	await asyncio.sleep(5)
	hugemb = discord.Embed(title='Death Note 💔',  description='**{}** morreu apos um ataque cardiaco depois de ter seu nome escrito no Death Note de **{}**'.format(user.name, ctx.message.author.name), color=0xA7ffbb)
	hugemb.set_footer(text='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial FF • DW')
	await bot.say(embed=hugemb)
	
@bot.command()
async def flipcoin():
	list = 'tapa na **CARA**', 'Rei perdeu a **COROA**'
	await bot.say(random.choice(list))																								
@bot.command()
@commands.has_permissions(ban_members=True)
async def voicemute(member: discord.Member):
    await bot.server_voice_state(member,mute=True)
    emb = discord.Embed(title='Usuário mutado voz', description='{} foi mutado com sucesso.'.format(member.mention), color=0xE57373)
    emb.set_footer(text='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial FF • DW')
    await bot.say(embed=emb)

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def voiceunmute(member: discord.Member):
	await bot.server_voice_state(member,mute=False)
	emb = discord.Embed(title='Usuário desmutado voz', description='{} foi desmutado com sucesso.'.format(member.mention), color=0x00ffbb)
	emb.set_footer(text='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial FF • DW')
	await bot.say(embed=emb)
    
@bot.command(pass_context=True)
async def flsff(ctx):
	list = 'Deitei 3 falta 1!', 'Taaaca o gelo', 'Me salva aqui men', '-49 pontos!', 'Olha o cara la no campo aberto!', ' diminuiram o lança!', 'lança mizeravel pior arma do jogo!', 'A garena ouviu a gente!', 'Cai em PEAK!', 'Buga a mira BUGA A MIRA!', 'Joga muito!'
	embed = discord.Embed(title='Falas mais comuns no free fire!', description=(random.choice(list)), color=0xE57373)
	embed.set_footer(text='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial FF • DW')
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def sugt(ctx, *, arg):
	sugt = discord.Embed(title='Sugestão de {}'.format(ctx.message.author.name), description=(arg), color=0x00838F)
	sugt.set_footer(text='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial FF • DW')
	await bot.say(embed=sugt)
	
@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def clear(ctx, limit: int=None):
    async for msg in bot.logs_from(ctx.message.channel, limit=limit):
            try:
                await bot.delete_message (msg)
            except:
                pass
    embed = discord.Embed(description="mensagens apagadas com sucesso! {} :smile:".format(ctx.message.author.mention), color=0x00ff00)
    await bot.say (embed=embed)
    
@bot.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def avisar(ctx, member: discord.Member, *, content: str):
	embed = discord.Embed(description='{} foi avisado com sucesso! por {}'.format(member.mention, ctx.message.author.mention), color=0x7a00bb)
	await bot.send_message(member, content)
	await bot.say(embed=embed)  
	
@bot.event
async def on_member_join(member):
  canal = bot.get_channel("535191091113099304")
  regras = bot.get_channel("535191091113099304")
  msg = "{} Seja bem vindo ao FF DW Divirta-se em nossos chats e leia as regras!".format(member.mention, regras.mention)
  await bot.send_message(canal, msg) 

@bot.event
async def on_member_remove(member):
   canal = bot.get_channel("535191091113099304")
   msg = "{} Vai nas sombras para o Exercito da DW não te pegar ".format(member.mention)
   await bot.send_message(canal, msg)
   
bot.run(str(os.environ.get('BOT_TOKEN')))




