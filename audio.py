import discord, time, datetime
from discord.ext import commands
from discord.ext.commands import Bot
import youtube_dl
from discord.utils import find
import asyncio
import time
import sys
import subprocess
import os
import json
import traceback
import random
import request as rq


start_time = time.time()


bot = commands.Bot(command_prefix='-')
print (discord.__version__)


	
	

@bot.event
async def on_ready():
    print ("Bot Toxic On")
    print ("quem ta falando é o " + bot.user.name)
    print ("Meu numero do ZipZop: " + bot.user.id)
    bot.loop.create_task(bg())
    await bot.change_presence(game=discord.Game(name='Fui criado pelo El_Brahmaᶠᶸᶜᵏᵧₒᵤ| t!ajuda'.format(len(bot.servers)), type=2))
    await asyncio.sleep(20)
    await bot.change_presence(game=discord.Game(name=str(len(set(bot.get_all_members())))+ ' soldados Toxic!', type=3))
    await asyncio.sleep(20)
    await bot.change_presence(game=discord.Game(name='FREE FIRE'))

from discord import opus
OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll',
             'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']


def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True

    for opus_lib in opus_libs:
            try:
                opus.load_opus(opus_lib)
                return
            except OSError:
                pass

    raise RuntimeError('Could not load an opus lib. Tried %s' %
                       (', '.join(opus_libs)))


opts = {
    'default_search': 'auto',
    'quiet': True
}  # youtube_dl options


load_opus_lib()

servers_songs = {}
player_status = {}
now_playing = {}
song_names = {}
paused = {}
rq_channel={}


async def set_player_status():
    for i in bot.servers:
        player_status[i.id] = False
        servers_songs[i.id] = None
        paused[i.id] = False
        song_names[i.id] = []
    print(200)


async def bg():
    bot.loop.create_task(set_player_status())



@bot.event
async def on_voice_state_update(before, after):
    if bot.is_voice_connected(before.server) == True: #bot is connected to voice channel in the server
        # if before.voice.voice_channel == None:
        #     pass
        if before.voice.voice_channel != None: #user in voice channel

            if after.voice.voice_channel!= None and after.voice.voice_channel.id == bot.voice_client_in(before.server).channel.id:
                if player_status[before.server.id]==True:
                    if paused[before.server.id]==True:
                        servers_songs[before.server.id].resume()
                        paused[before.server.id]=False

            if before.voice.voice_channel.id == bot.voice_client_in(before.server).channel.id: # user left the voice channel detected
                if len(bot.voice_client_in(before.server).channel.voice_members) <= 1: #there is only bot in voice channel
                    if player_status[before.server.id]==True:
                        servers_songs[before.server.id].pause()
                        paused[before.server.id]=True
                        await asyncio.sleep(10)
                        if len(bot.voice_client_in(before.server).channel.voice_members) <= 1:
                            await bot.voice_client_in(before.server).disconnect()
                            servers_songs[before.server.id]=None
                            player_status[before.server.id]=False
                            paused[before.server.id]=False
                            now_playing[before.server.id]=None
                            song_names[before.server.id].clear()
                            await bot.send_message(discord.Object(id=rq_channel[before.server.id]),"**Kurusaki left because there was no one inside `{}`**".format(before.voice.voice_channel))






@bot.event
async def on_command_error(con,error):
    pass


async def queue_songs(con, skip, clear):
    if clear == True:
        await bot.voice_client_in(con.message.server).disconnect()
        player_status[con.message.server.id] = False
        song_names[con.message.server.id].clear()

    if clear == False:
        if skip == True:
            servers_songs[con.message.server.id].pause()

        if len(song_names[con.message.server.id]) == 0:
            servers_songs[con.message.server.id] = None

        if len(song_names[con.message.server.id]) != 0:
            r = rq.Session().get('https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q={}&key=AIzaSyDy4gizNmXYWykfUACzU_RsaHtKVvuZb9k'.format(
                song_names[con.message.server.id][0])).json()
            pack = discord.Embed(title=r['items'][0]['snippet']['title'],
                                 url="https://www.youtube.com/watch?v={}".format(r['items'][0]['id']['videoId']))
            pack.set_thumbnail(url=r['items'][0]['snippet']
                               ['thumbnails']['default']['url'])
            pack.add_field(name="Requested by:", value=con.message.author.name)

            song = await bot.voice_client_in(con.message.server).create_ytdl_player(song_names[con.message.server.id][0], ytdl_options=opts, after=lambda: bot.loop.create_task(after_song(con, False, False)))
            servers_songs[con.message.server.id] = song
            servers_songs[con.message.server.id].start()
            await bot.delete_message(now_playing[con.message.server.id])
            msg = await bot.send_message(con.message.channel, embed=pack)
            now_playing[con.message.server.id] = msg

            if len(song_names[con.message.server.id]) >= 1:
                song_names[con.message.server.id].pop(0)

        if len(song_names[con.message.server.id]) == 0 and servers_songs[con.message.server.id] == None:
            player_status[con.message.server.id] = False


async def after_song(con, skip, clear):
    bot.loop.create_task(queue_songs(con, skip, clear))


@bot.command(pass_context=True)
async def play(con, *, url):
    """PLAY THE GIVEN SONG AND QUEUE IT IF THERE IS CURRENTLY SOGN PLAYING"""
    if con.message.channel.is_private == True:
        await bot.send_message(con.message.channel, "**You must be in a `server text channel` to use this command**")

    if con.message.channel.is_private == False: #command is used in a server
        rq_channel[con.message.server.id]=con.message.channel.id
        if bot.is_voice_connected(con.message.server) == False:
            await bot.join_voice_channel(con.message.author.voice.voice_channel)

        if bot.is_voice_connected(con.message.server) == True:
            if player_status[con.message.server.id] == True:
                song_names[con.message.server.id].append(url)
                r = rq.Session().get('https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q={}&key=put your youtube token here'.format(url)).json()
                await bot.send_message(con.message.channel, "**Song `{}` Queued**".format(r['items'][0]['snippet']['title']))

            if player_status[con.message.server.id] == False:
                player_status[con.message.server.id] = True
                song_names[con.message.server.id].append(url)
                song = await bot.voice_client_in(con.message.server).create_ytdl_player(song_names[con.message.server.id][0], ytdl_options=opts, after=lambda: bot.loop.create_task(after_song(con, False, False)))
                servers_songs[con.message.server.id] = song
                servers_songs[con.message.server.id].start()
                r = rq.Session().get('https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q={}&key=AIzaSyDy4gizNmXYWykfUACzU_RsaHtKVvuZb9k'.format(url)).json()
                pack = discord.Embed(title=r['items'][0]['snippet']['title'],
                                     url="https://www.youtube.com/watch?v={}".format(r['items'][0]['id']['videoId']))
                pack.set_thumbnail(
                    url=r['items'][0]['snippet']['thumbnails']['default']['url'])
                pack.add_field(name="Requested by:",
                               value=con.message.author.name)
                msg = await bot.send_message(con.message.channel, embed=pack)
                now_playing[con.message.server.id] = msg
                song_names[con.message.server.id].pop(0)



@bot.command(pass_context=True)
async def pular(con):
    if con.message.channel.is_private == True:
        await bot.send_message(con.message.channel, "**You must be in a `server text channel` to use this command**")

    # COMMAND NOT IN DM
    if con.message.channel.is_private == False:
        if servers_songs[con.message.server.id] == None or len(song_names[con.message.server.id]) == 0 or player_status[con.message.server.id] == False:
            await bot.send_message(con.message.channel, "**não há mais musicas para eu tocar :(**")
        if servers_songs[con.message.server.id] != None:
            bot.loop.create_task(queue_songs(con, True, False))
            await bot.say('musica pulada com sucesso!')

@bot.command(pass_context=True)
async def entrar(con,*,channel=None):
    """JOIN A VOICE CHANNEL THAT THE USR IS IN OR MOVE TO A VOICE CHANNEL IF THE BOT IS ALREADY IN A VOICE CHANNEL"""


    # COMMAND IS IN DM
    if con.message.channel.is_private == True:
        await bot.send_message(con.message.channel, "**You must be in a `server text channel` to use this command**")

    # COMMAND NOT IN DM
    if con.message.channel.is_private == False:
        voice_status = bot.is_voice_connected(con.message.server)

        voice=find(lambda m:m.name == channel,con.message.server.channels)

        if voice_status == False and channel == None:  # VOICE NOT CONNECTED
            if con.message.author.voice_channel == None:
                await bot.send_message(con.message.channel,"**você deve estar em um canal de voz para executar esse comando!**")
   
            if con.message.author.voice_channel != None:
                await bot.join_voice_channel(con.message.author.voice.voice_channel)

        if voice_status == False and channel != None:  # PICKING A VOICE CHANNEL
            await bot.join_voice_channel(voice)

        if voice_status == True:  # VOICE ALREADY CONNECTED
            if voice == None:
            	await bot.send_message(con.message.channel, "**Entrei no canal de voz!**")


            if voice != None:            
                if voice.type == discord.ChannelType.voice:
                     await bot.voice_client_in(con.message.server).move_to(voice)
                  


@bot.command(pass_context=True)
async def sair(con):
    """LEAVE THE VOICE CHANNEL AND STOP ALL SONGS AND CLEAR QUEUE"""
    # COMMAND USED IN DM
    if con.message.channel.is_private == True:
        await bot.send_message(con.message.channel, "**You must be in a `server text channel` to use this command**")

    # COMMAND NOT IN DM
    if con.message.channel.is_private == False:

        # IF VOICE IS NOT CONNECTED
        if bot.is_voice_connected(con.message.server) == False:
            await bot.send_message(con.message.channel, "**Saí do canal de voz e a musica parou!**")

        # VOICE ALREADY CONNECTED
        if bot.is_voice_connected(con.message.server) == True:
            bot.loop.create_task(queue_songs(con, False, True))
      
@bot.command(pass_context=True)
async def pause(con):
    # COMMAND IS IN DM
    if con.message.channel.is_private == True:
        await bot.send_message(con.message.channel, "**You must be in a `server text channel` to use this command**")

    # COMMAND NOT IN DM
    if con.message.channel.is_private == False:
        if servers_songs[con.message.server.id] != None:
            if paused[con.message.server.id] == True:
                await bot.send_message(con.message.channel, "**Audio already paused**")
            if paused[con.message.server.id] == False:
                servers_songs[con.message.server.id].pause()
                paused[con.message.server.id] = True





@bot.command(pass_context=True)
async def resume(con):
    # COMMAND IS IN DM
    if con.message.channel.is_private == True:
        await bot.send_message(con.message.channel, "**You must be in a `server voice channel` to use this command**")

    # COMMAND NOT IN DM
    if con.message.channel.is_private == False:
        if servers_songs[con.message.server.id] != None:
            if paused[con.message.server.id] == False:
                await bot.send_message(con.message.channel, "**Audio already playing**")
            if paused[con.message.server.id] == True:
                servers_songs[con.message.server.id].resume()
                paused[con.message.server.id] = False



@bot.command(pass_context=True)
async def volume(con,vol:float):
    if player_status[con.message.server.id] == False:
        await bot.send_message(con.message.channel,"Não há musica tocando no momento")
    if player_status[con.message.server.id] == True:
        servers_songs[con.message.server.id].volume =vol;
     



# if __name__ == "__main__":
#     for extension in extensions:
#         try:
#             bot.load_extension(extension)
#             print("{} loaded".format(extension))
#         except Exception as error:
#             print("Unable to load extension {} error {}".format(extension, error))
    
@bot.command(pass_context=True)
async def ping(ctx):
	channel = ctx.message.channel
	t1 = time.perf_counter()
	await bot.send_typing(channel)
	t2 = time.perf_counter()
	embed=discord.Embed(title="Pong!", description='Meu Ping {}ms.'.format(round((t2-t1)*1000)), color=0x76FF03)
	embed.set_footer(text ='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial Toxic')
	await bot.say(embed=embed)


@bot.command(pass_context=True)
async def perfil(ctx, user: discord.Member):
    embed = discord.Embed(title="perfil de {}".format(user.name), description="Reflexão: Hoje n tem reflexão :(", color=0x00ff00)
    embed.add_field(name="Nome", value=user.name, inline=True)
    embed.add_field(name="ID do usuário", value=user.id, inline=True)
    embed.add_field(name="Status do usuário", value=user.status, inline=True)
    embed.add_field(name="Melhor cargo", value=user.top_role)
    embed.add_field(name="entrou no servidor", value=user.joined_at)
    embed.set_footer(text ='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial Toxic')
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
		join = discord.Embed(description= '%s '%(str(server)),title = 'Nome', colour = 0xFFFF);
		join.set_thumbnail(url = server.icon_url);
		join.add_field(name = '👑 Dono',
		value = str(server.owner) + '\n' + server.owner.id);
		join.add_field(name = '💻ID', value = str(server.id))
		join.add_field(name = '👥Total de membros', value = str(server.member_count));
		join.add_field(name = '📝Total de canais Texto/voz', value = str(channelz));
		join.add_field(name="🎭 Total de roles", value=len(ctx.message.server.roles), inline=True)
		join.add_field(name='🌎 Região', value=server.region)
		join.add_field(name ='📆Criado em', value='Data: %s'%time);
		
		join.add_field(name='👮Role Top1', value=server.role_hierarchy[0])
		join.set_footer(text ='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ | Bot Oficial TOXIC');
		await bot.say(embed=join);

@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, userName: discord.User):
	await bot.kick(userName)
	embed = discord.Embed(title='usuário kickado', description='{} usuário kickado com sucesso'.format(ctx.message.author.mention), color=0xff0bb)
	embed.set_footer(text='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial TOXIC')
	await bot.say(embed=embed)
	print ("user has kicked")		
	
			
@bot.command(pass_context=True)
async def ajuda(ctx):
    embed = discord.Embed(title="Toxic Bot", description="Meu comandos são", color=0x00ff00)
    embed.set_footer(text="Bot Oficial TOXIC")
    embed.set_author(name="Fui criado pelo By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ ")
    embed.add_field(name="ban", value="bane o usuário", inline=True)
    embed.add_field(name="kick", value="expulsa o usuário", inline=True)
    embed.add_field(name="serverinfo", value="Veja informações do servidor do discord Atual!", inline=True)
    embed.add_field(name="perfil", value="mostra seu perfil!", inline=True)
    embed.add_field(name="ping", value="Veja minha velocidade de resposta!", inline=True)
    embed.add_field(name="avatar", value="Veja o avatar de determinado usuário!", inline=True)
    embed.add_field(name="deathnote", value="escreva o nome de determinado usuário em seu death note!", inline=True)
    embed.add_field(name="kiss", value="O amor esta no ar.. beije determinado usuário!", inline=True)
    embed.add_field(name="hug", value="abrace seu/sua melhor amigo(a)!", inline=True)
    embed.add_field(name="flipcoin", value="cara ou coroa?", inline=True)
    await bot.say(embed=embed)	
    
@bot.command(pass_context=True)
async def avatar(ctx, user: discord.User):
	
	list = (user.avatar_url), (user.avatar_url)
	hug = random.choice(list)
	hugemb = discord.Embed(title='Avatar de {}'.format(user.name), color=0x6A1B9A)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial TOXIC')
	await bot.say(embed=hugemb)    								
  
@bot.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, userName: discord.User):
	await bot.ban(userName)
	embed = discord.Embed(title='usuário banido!', description='{} usuário banido com sucesso'.format(ctx.message.author.mention), color=0xff0Ab)
	embed.set_footer(text='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial TOXIC')
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
	hugemb.set_footer(text='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial TOXIC')
	await bot.say(embed=hugemb)

@bot.command(pass_context=True)
async def deathnote(ctx, user: discord.User):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/534806488531599380/14ae937e622c452bc45e509ed43c8e38a410fc0b_hq.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/533615190273425409/67dc6ce11c0ebe1c723983f18d7f68a8b0d11887_hq.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Death Note 💀',  description='**{}** escreveu o nome de **{}** em seu Death Note'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial TOXIC')
	await bot.say(embed=hugemb)
	await asyncio.sleep(5)
	hugemb = discord.Embed(title='Death Note 💔',  description='**{}** morreu apos um ataque cardiaco depois de ter seu nome escrito no Death Note de **{}**'.format(user.name, ctx.message.author.name), color=0xA7ffbb)
	hugemb.set_footer(text='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial TOXIC')
	await bot.say(embed=hugemb)
	
@bot.command()
async def flipcoin():
	list = 'tapa na **CARA**', 'Rei perdeu a **COROA**'
	await bot.say(random.choice(list))																								
																																				
bot.run(os.environ['BOT_TOKEN'])
