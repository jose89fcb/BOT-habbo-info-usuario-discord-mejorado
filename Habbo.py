import discord, asyncio
from discord.ext import commands
import requests
import json
import discord
from urllib import parse, request
from requests import get
import datetime
import asyncio
import requests, json, discord, datetime, asyncio, aiohttp
from urllib import parse, request
import requests, bs4
import re








with open('config.json') as f: 
    config = json.load(f) 


bot = commands.Bot(command_prefix=config['prefijo']) #Añadir un prefijo si gustas
bot.remove_command("help") #Borramos el comando !help por defecto

 


#Comienza el codigo de habbo.es
@bot.command()
async def HabboES(ctx,  *, Habboinfo):
  async with ctx.typing():
   
    await asyncio.sleep(0)

   

   
    response = requests.get(f'https://www.habbo.es/api/public/users?name={Habboinfo}')


   


    id = response.json()['uniqueId']
    Habbokeko = response.json()['name']
    mision = response.json()['motto']

   
   
   

    MiembroDesde = response.json()['memberSince']
    registrado = MiembroDesde
    miembro = registrado.split("T")[0].split("-")
    fecha = "/".join(reversed(miembro))
    MiembroDesde = MiembroDesde.replace("."," ")
    MiembroDesde = MiembroDesde.replace("000+0000","")

    registradodesde = MiembroDesde
    miembro1 = registradodesde.split("T")[1].split(" ")
    hora = " ".join(reversed(miembro1))

    url = f'https://www.habbo.es/api/public/users/{id}/groups'
    r= requests.get(url)
    habbo4 = r.text
    habbo4 = r.json()
    grupos = len(habbo4)
    grupos=(str(grupos))

    url = f'https://www.habbo.es/api/public/users/{id}/rooms'
    r= requests.get(url)
    habbo3 = r.text
    habbo3 = r.json()
    salas = len(habbo3)
    salas=(str(salas))

    url = f'https://www.habbo.es/extradata/public/users/{id}/photos'
    r= requests.get(url)
    habbo2 = r.text
    habbo2 = r.json()
    fotos = len(habbo2)
    fotos=(str(fotos))

    url= f'https://www.habbo.es/api/public/users/{id}/friends'
    r= requests.get(url)
    habbo1 = r.text
    habbo1 = r.json()
    amigos = len(habbo1)
    amigos=(str(amigos))
    
    
    
    

    

    
    
    
    

    
   

  try:
    
    estado = response.json()["online"]
    estado = (str(estado)).replace("True","Conectado").replace("False","desconectado")
    

    totalxp = response.json()['totalExperience']
    totalxp = ('{:,}'.format(totalxp)).replace(",",".")
    
    NivelActual = response.json()['currentLevel']
    NivelActual = (str(NivelActual))

    GemasHabbo = response.json()['starGemCount']
    GemasHabbo = ('{:,}'.format(GemasHabbo)).replace(",",".")

    siguientenivel = response.json()['currentLevelCompletePercent']
    siguientenivel = (str(siguientenivel))

    ultiomoaccesso = response.json()["lastAccessTime"]
    
    habboaccesso1 = ultiomoaccesso
    accesso = habboaccesso1.split("T")[0].split("-")
    fechaAccesso = "/".join(reversed(accesso))
    ultiomoaccesso = ultiomoaccesso.replace("."," ")
    ultiomoaccesso = ultiomoaccesso.replace("000+0000","")

    habboaccesso = ultiomoaccesso
    accesso1 = habboaccesso.split("T")[1].split(" ")
    horaAccesso = " ".join(reversed(accesso1))


    perfil = response.json()['profileVisible']

    perfil = (str(perfil)).replace("False","No muestra su perfil").replace("True","Muestra su perfil")
    
   

   
   
    
    

   
    
    

    


  except KeyError:

    estado ="desconectado"
    totalxp="No muestra Xp"
    NivelActual="No muestra el nivel"
    GemasHabbo="no muestra sus gemas"
    siguientenivel="No muestra proceso"
    fechaAccesso="No muestra la fecha"
    horaAccesso="ni la hora"
    perfil="No muestra su perfil"
    grupos="No muestra sus grupos"
    salas="No muestra sus salas"
    amigos="No muestra sus amigos"
    
    
    
    
   
    

    
   
    


  embed = discord.Embed(title="\n\n\nEstá es la info de 🡺 " + Habbokeko, description="•ID🡺 " + id + "\n\n•Estado🡺 " +estado + "\n\n•Total XP🡺 " + totalxp + "\n\n•Misión 🡺 " + mision  + "\n\n•Nivel actual🡺 " +  NivelActual + "\n\n•Gemas Obtenidas (Estrellas)🡺 " + GemasHabbo + "\n\n•Siguiente Nivel🡺 " + siguientenivel + "\n\n•Miembro desde🡺 " +fecha +" - " + hora + "\n\n•último accesso🡺 "  +fechaAccesso + " - " +horaAccesso + "\n\n•Perfil🡺 " + perfil + "\n\n•Grupos Totales🡺 " + grupos + "\n\n•Salas Totales🡺 " + salas + "\n\n•Fotos Totales🡺 " + fotos +"\n\n•Total Amigos🡺 " + amigos + "\n\n[Visita el perfil de " + Habbokeko + "](https://habbo.es/profile/"+ Habbokeko + ")"  "\n\n[twitter oficial](https://twitter.com/ESHabbo) | " "[facebook oficial](https://www.facebook.com/Habbo) | " "[instagram oficial](https://www.instagram.com/habboofficial)", timestamp=datetime.datetime.utcnow(), color=discord.Colour.random())

  embed.set_thumbnail(url="https://www.habbo.es/habbo-imaging/avatarimage?user=" + Habbokeko + "&&headonly=1&size=b&gesture=sml&head_direction=4&action=std")
  embed.set_author(name="Habbo [ES]", icon_url="https://i.imgur.com/0UDuO3n.png")
  embed.set_footer(text="habbo[ES]", icon_url="https://i.imgur.com/6ePWlHz.png")
  await ctx.send(embed=embed)
 

  
    
  
 
   



   


    
    




@bot.event
async def on_message(message):
    if message.author.id != bot.user.id:
        if message.guild:  
          
            await bot.process_commands(message)  
        else:
                
            
            embed = discord.Embed(
                
                color = discord.Color.random(),
                title ="Mensaje de frank",
                description = "No puedes escribir comandos por mensaje directo/DM/privado"
                
               


            )
            embed.set_thumbnail(url="https://i.imgur.com/kch7Otk.png")
            
            return await message.author.send(embed=embed)
            





  
    
          

@bot.command(aliases=["quit"])
@commands.has_permissions(administrator=True)
async def cerrar(ctx):
    embed = discord.Embed(title=f" ", description="él BOT **" + bot.user.name + "** ahora está desconectado", color=discord.Color.red())
        
    
    embed.set_thumbnail(url="https://i.imgur.com/iozmWWh.gif")
    await ctx.send(embed=embed)

    await bot.close()
    print("él BOT" + bot.user.name + "se cerró")           
       


@bot.event
async def on_ready():
    
    channel = discord.utils.get(bot.get_all_channels(), name='general')
    embed = discord.Embed(title=f" ", description="él BOT **" + bot.user.name + "** ahora está en linea" + "\n\nEscribe !comandos para conocer los comandos de cada hotel", color=discord.Color.green())
        
    
    embed.set_thumbnail(url="https://i.imgur.com/duRuLN6.gif")
    await channel.send(embed=embed)

    print("BOT " f'{bot.user.name}')
    activity = discord.Game(name="Habbo info", type=1)
    await bot.change_presence(status=discord.Status.online, activity=activity)



@bot.command()
async def comandos(ctx):
  embed = discord.Embed(title="COMANDOS", description="Aquí están todos los comandos para poder generar los usuarios de cada hotel\n\n!HabboES ejemplo\n!HabboCOM ejemplo\n!HabboDE ejemplo\n!HabboFR ejemplo\n!HabboFI ejemplo\n!HabboIT ejemplo\n!HabboTR ejemplo\n!HabboNL ejemplo\n!HabboBR ejemplo\n\n\nEscribe !cerrar para poder cerrar el bot")
  embed.set_author(name="información", icon_url="https://i.imgur.com/grmS8RH.png")
  await ctx.send(embed=embed)  
  



    
bot.run(config['token'])



   



    
  

  
