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
from dateutil.parser import isoparse
import locale
locale.setlocale(locale.LC_TIME, "es_ES")
from datetime import datetime
from dateutil import relativedelta
from dateutil import parser
import time








with open('config.json') as f: 
    config = json.load(f) 


bot = commands.Bot(command_prefix=config['prefijo']) #Añadir un prefijo si gustas
bot.remove_command("help") #Borramos el comando !help por defecto

 


#Comienza el codigo de habbo.es
@bot.command()
async def habbo(ctx,  *, Habboinfo):
  
  async with ctx.typing():
   
    await asyncio.sleep(0)
    await ctx.message.delete() #Borramos el comando para no dejar sucio el chat xD
    await ctx.send(f"Generando información del keko  {Habboinfo}...", delete_after=0)
    time.sleep(3)

   

    try:

     response = requests.get("https://www.habbo." + config['hotel']+  f"/api/public/users?name={Habboinfo}")


   


     id = response.json()['uniqueId']
     Habbokeko = response.json()['name']
     mision = response.json()['motto']

   

   
   
   

     fecha = isoparse(response.json()['memberSince']).timestamp()
     timestamp = fecha
     dt_object = datetime.fromtimestamp(timestamp).strftime("%A, %#d de %B del %Y %H:%M:%S")
    #registrado = MiembroDesde
    #miembro = registrado.split("T")[0].split("-")
    #fecha = "/".join(reversed(miembro))
    #MiembroDesde = MiembroDesde.replace("."," ")
    #MiembroDesde = MiembroDesde.replace("000+0000","")

    #registradodesde = MiembroDesde
    #miembro1 = registradodesde.split("T")[1].split(" ")
    #hora = " ".join(reversed(miembro1))

     url = "https://www.habbo." + config['hotel']+  f"/api/public/users/{id}/groups"
     r= requests.get(url)
     habbo4 = r.text
     habbo4 = r.json()
     grupos = len(habbo4)
     grupos=(str(grupos))

     url = "https://www.habbo." + config['hotel'] + f"/api/public/users/{id}/rooms"
     r= requests.get(url)
     habbo3 = r.text
     habbo3 = r.json()
     salas = len(habbo3)
     salas=(str(salas))

     url = "https://www.habbo." + config['hotel'] + f"/extradata/public/users/{id}/photos"
     r= requests.get(url)
     habbo2 = r.text
     habbo2 = r.json()
     fotos = len(habbo2)
     fotos=(str(fotos))

     url= "https://www.habbo." + config['hotel'] + f"/api/public/users/{id}/friends"
     r= requests.get(url)
     habbo1 = r.text
     habbo1 = r.json()
     amigos = len(habbo1)
     amigos=(str(amigos))

     url= "https://www.habbo." + config['hotel'] + f"/api/public/users/{id}/badges"
     r= requests.get(url)
     habbo2 = r.text
     habbo2 = r.json()
     placas = len(habbo2)
     placas = ('{:,}'.format(placas)).replace(",",".")


    
    
    
    
    

    
   ####
    
    

     fecha = isoparse(response.json()['lastAccessTime']).timestamp()
    except KeyError:
      fecha="No muestra"

    except TypeError:
      fecha=""

      
    timestamp = fecha

    try:

     date1 =  parser.parse(datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")) 
    except TypeError:
      date1="No muestra"

    date2 = datetime.now()

    try:

     r = relativedelta.relativedelta(date2, date1)
    except TypeError:
      r=""

    try:

     r.months + (12*r.years)
    except AttributeError:
      r=""

    try:

     tiempotrans = f"{r.years} Años {r.days} Días {r.hours} Horas {r.months} Meses {r.minutes} Minutos {r.seconds} Segundos"
    except AttributeError:
      tiempotrans="No muestra ❌"
   ###


   ####
     
    try:

     fecha = isoparse(response.json()['memberSince']).timestamp()
    except KeyError:
      fecha=""
    


    
    timestamp = fecha


    try:

     date1 =  parser.parse(datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")) 
    except TypeError:
      await ctx.send("El keko no existe!")
        
    date2 = datetime.now()
  
    try:

     r = relativedelta.relativedelta(date2, date1)
    except TypeError:
      r="" 
  
    try:

     r.months + (12*r.years)
  
      
  
     
    

     tiempo = f"{r.years} Años {r.days} Días {r.hours} Horas {r.months} Meses {r.minutes} Minutos {r.seconds} Segundos"
    except AttributeError:
      tiempo=""
      r=""


   #####
    
    
    
    

    
   

  try:
    
    estado = response.json()["online"]
    estado = (str(estado)).replace("True","Conectado✅").replace("False","desconectado❌")
    

    totalxp = response.json()['totalExperience']
    totalxp = ('{:,}'.format(totalxp)).replace(",",".")
    
    NivelActual = response.json()['currentLevel']
    NivelActual = (str(NivelActual))

    GemasHabbo = response.json()['starGemCount']
    GemasHabbo = ('{:,}'.format(GemasHabbo)).replace(",",".")

    siguientenivel = response.json()['currentLevelCompletePercent']
    siguientenivel = (str(siguientenivel))

    try:

     ultiomoaccesso = isoparse(response.json()['lastAccessTime']).timestamp()
    except TypeError:
      ultiomoaccesso=""
    timestamp = ultiomoaccesso

    try:

     ultmimoacesso = datetime.fromtimestamp(timestamp).strftime("%A, %#d de %B del %Y %H:%M:%S")
    except TypeError:
      ultmimoacesso="No muestra ❌"

    
    

    


    perfil = response.json()['profileVisible']

    

    perfil = (str(perfil)).replace("False","No muestra su perfil❌").replace("True","Muestra su perfil")

    
   

   
   
    
    

  

    
    

    


  except KeyError:

    estado ="desconectado❌"
    totalxp="No muestra Xp❌"
    NivelActual="No muestra el nivel❌"
    GemasHabbo="no muestra sus gemas❌"
    siguientenivel="No muestra proceso❌"
    ultmimoacesso="No muestra la fecha ❌"
    horaAccesso="ni la hora❌"
    perfil="No muestra su perfil❌"
    grupos="No muestra sus grupos❌"
    salas="No muestra sus salas❌"
    amigos="No muestra sus amigos❌"
    placas="No muestra sus placas❌"
   
    
    
  
    
  
    


  
 
    
  except AttributeError:
    ultiomoaccesso="nada"
    perfil="Muestra su perfil"
    fechaAccesso="Lo tiene oculto❌"
    horaAccesso=""
   
   
    


 
    
   
    
    
    
    


    
   
    ####
   
    ###
    



  

  
  try:

   embed = discord.Embed(title="\n\n\nEstá es la info de 🡺 " + Habbokeko, description=f"•ID🡺 " + id + "\n\n•Estado🡺 " +estado + "\n\n•Total XP🡺 " + totalxp + "\n\n•Misión 🡺 " + mision  + "\n\n•Nivel actual🡺 " +  NivelActual + "\n\n•Gemas Obtenidas (Estrellas)🡺 " + GemasHabbo + "\n\n•Siguiente Nivel🡺 " + siguientenivel + "\n\n•Hora Miembro desde🡺 " +dt_object +"\n\n•Hora último accesso🡺 "  +ultmimoacesso +" \n\n•Perfil🡺 " +perfil + "\n\n•Grupos Totales🡺 " + grupos + "\n\n•Salas Totales🡺 " + salas + "\n\n•Fotos Totales🡺 " + fotos +"\n\n•Total Amigos🡺 " + amigos + "\n\n•Placas Totales🡺 " +placas + " \n\n•Tiempo de último acesso🡺 "   +tiempotrans+ "\n\n•Tiempo Miembro desde🡺 "+tiempo+ "\n\n[Visita el perfil de " + Habbokeko + "](https://habbo.es/profile/"+ Habbokeko + ")"  "\n\n[twitter oficial](https://twitter.com/ESHabbo) | " "[facebook oficial](https://www.facebook.com/Habbo) | " "[instagram oficial](https://www.instagram.com/habboofficial)", timestamp=datetime.utcnow(), color=discord.Colour.random())



    
   embed.set_thumbnail(url="https://www.habbo.es/habbo-imaging/avatarimage?user=" + Habbokeko + "&&headonly=1&size=b&gesture=sml&head_direction=4&action=std")
   embed.set_author(name="Habbo [ES]", icon_url="https://i.imgur.com/0UDuO3n.png")
   embed.set_footer(text="habbo[ES]", icon_url="https://i.imgur.com/6ePWlHz.png")
   await ctx.send(embed=embed)
  except UnboundLocalError:
    Habbokeko=""



  

    
  
 



   


    
    




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



   



    
  

  