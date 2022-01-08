import discord,time,pprint,os,sys,random
from discord.ext import commands
from discord import utils
import srcomapi,srcomapi
import requests,bs4,pprint,csv

from datetime import date
from datetime import datetime,timedelta

from selenium import webdriver,webdriver
from selenium.webdriver.common.keys import Keys,Keys

print("bop")
os.chdir('C:\\Users\\Parker\\Documents\\python bot')

file=open("TOKEN.txt","r")
TOKEN=file.readline()
file.close()
 
intents = discord.Intents.all()
bot = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!')
content=[]

@bot.command()
async def ball8(ctx):
    responses=['As I see it, yes.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        'Don’t count on it.',
        'It is certain.',
        'It is decidedly so.',
        'Most likely.',
        'My reply is no.',
        'My sources say no.',
        'Outlook not so good.',
        'Outlook good.',
        'Reply hazy, try again.',
        'Signs point to yes.',
        'Very doubtful.',
        'Without a doubt.',
        'Yes.',
        'Yes – definitely.',
        'You may rely on it.']
    await ctx.channel.send(random.choice(responses))

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    content.clear()
    content.append(str(message.content))
    print(message.content)

    channel=message.channel

    if message.author == bot.user:
        return

    await bot.process_commands(message)

    if message.content.startswith('!'):
        return

    if message.content.lower().startswith('man') and message.content.lower().endswith('man') and len(message.content)==3:
        await channel.send('https://cdn.discordapp.com/attachments/548410541991919619/817953861884575774/image0.jpg')

@bot.command()
async def sunday(ctx):
    guild=ctx.guild
    dt=datetime.today().weekday()

    if dt==6:
        await ctx.channel.send('https://youtu.be/JoNY0ZVWTg4wa')
    else:
        timeleft=6-dt
        await ctx.channel.send('`%s more days until snake sunday!!`'%(timeleft))

@bot.command()
async def friday(ctx):
    guild=ctx.guild
    dt=datetime.today().weekday()

    if dt==4:
        await ctx.channel.send('https://www.youtube.com/watch?v=nxoe5DjDd74')
    else:
        if dt >4:
            timeleft=11-dt
        else:
            timeleft=4-dt
        await ctx.channel.send('`%s more days until funke monke friday!!`'%(timeleft))

@bot.command()
async def saturday(ctx):
    guild=ctx.guild
    dt=datetime.today().weekday()

    if dt==5:
        await ctx.channel.send('https://cdn.discordapp.com/attachments/313118168925339649/833771353077055518/170480581_495967865150590_6222016406437353393_n.mp4')
    else:
        if dt >5:
            timeleft=12-dt
            await ctx.channel.send('`%s more day until saturday!!`'%(timeleft))
        else:
            timeleft=5-dt
            if timeleft==1:
                await ctx.channel.send('`%s more day until saturday!!`'%(timeleft))
            else:
                await ctx.channel.send('`%s more days until saturday!!`'%(timeleft))

@bot.command()
async def thursday(ctx):
    guild=ctx.guild
    dt=datetime.today().weekday()

    if dt==3:
        await ctx.channel.send('https://cdn.discordapp.com/attachments/546763235051700314/837363451290058813/ITS_FUCKING_TIME_BABY.mp4')
    else:
        
        if dt >3:
            timeleft=10-dt
            await ctx.channel.send('`%s more days until thursday!!`'%(timeleft))
        else:
            timeleft=3-dt
            await ctx.channel.send('`%s more days until thursday!!`'%(timeleft))

@bot.command()
async def tuesday(ctx):
    guild=ctx.guild
    dt=datetime.today().weekday()

    if dt==1:
        await ctx.channel.send('https://cdn.discordapp.com/attachments/546763235051700314/851853957295112222/tactical_toad_tuesday.mp4')
    else:
        if dt >1:
            timeleft=8-dt
            await ctx.channel.send('`%s more days until tuesday!`'%(timeleft))
        else:
            timeleft=1-dt
            await ctx.channel.send('`%s more days until tuesday!!`'%(timeleft))

@bot.command()
async def wednesday(ctx):
    guild=ctx.guild
    dt=datetime.today().weekday()

    if dt==2:
        await ctx.channel.send('https://cdn.discordapp.com/attachments/304821057137672193/715109073359601744/White_Gi-.mp4')
    else:
        if dt >1:
            timeleft=9-dt
            await ctx.channel.send('`%s more days until wednesday!`'%(timeleft))
        else:
            timeleft=2-dt
            await ctx.channel.send('`%s more days until wednesday!!`'%(timeleft))

@bot.command()
async def speedrun(ctx):
    guild=ctx.guild
    File=open("speedruncheck.txt","w")


    api = srcomapi.SpeedrunCom(); api.debug = 1
    lis=api.search(srcomapi.datatypes.Game, {"name": "super mario 64"})

    game=lis[0]
    cat=game.categories

    for i in range(1,6):

        File.write("%s\n" %(cat[i]))

        for k in range(0,3):

            File.write("%s PLACE : " %(k+1))

            three=cat[i].records[0].runs
            
            NAME=three[k]["run"].players[0].name
            TIME=three[k]["run"].times["primary_t"]

            if TIME > 3600:
                TIME-=3600

                minutes=TIME//60
                seconds=int(TIME%60)

                format="1h %sm %ss"%(minutes,seconds)
            else:
                minutes=TIME//60
                seconds=TIME%60
                milliseconds=int(1000*(seconds%1))

                format="%sm %ss %sms"%(int(minutes),int(seconds),milliseconds)

            try:
                File.write(NAME+ ": ")
            except:
                File.write("Akira: ")
            File.write(format+"\n")


    obj=date.today()

    File.write(obj.strftime("%B %d, %Y"))
    File.close()

    Original=open("speedrun.txt","r")
    New=open("speedruncheck.txt","r")

    ogcontent = Original.readlines()
    newcontent= New.readlines()
    isbroken=False

    for k in range(5):
        num=k*4
        cat=ogcontent[k*4]
        for i in range(4):
            origin=ogcontent[num+i]
            new=newcontent[num+i]

            if origin==new:
                pass
            else:
                isbroken=True
                await ctx.channel.send("There is a new record in %s"%(cat))
                await ctx.channel.send(new)
                await ctx.channel.send("<@!180884209030791169> <@!163135868448538624> <@!228632650049519616>")
                break

    if isbroken==False:
        await ctx.channel.send("no records have been broken since %s" %(ogcontent[20]))

    Original.close()
    New.close()

    if isbroken==True:
        os.remove("C:\\Users\\Parker\\Documents\\python bot\\speedrun.txt")
        os.rename("C:\\Users\\Parker\\Documents\\python bot\\speedruncheck.txt","C:\\Users\\Parker\\Documents\\python bot\\speedrun.txt")

@bot.command()
async def covid(ctx,borough):

    dic={}
    areas=['arrondissement ou ville liee', 'ahuntsic–cartierville', 'anjou', "baie d'urfe", 'beaconsfield', 'cote-des-neiges–notre-dame-de-grace', 'cote-saint-luc', 'dollard-des-ormeaux', 'dorval', 'hampstead', 'kirkland', 'lachine', 'lasalle', "l'ile-bizard–sainte-genevieve", 'mercier–hochelaga-maisonneuve', 'montreal est', 'montreal-nord', 'montreal-ouest', 'mont-royal', 'outremont', 'pierrefonds–roxboro', 'plateau mont-royal', 'pointe-claire', 'riviere-des-prairies–pointe-aux-trembles', 'rosemont–la petite patrie', 'sainte-anne-de-bellevue', 'saint-laurent', 'saint-leonard', 'senneville', 'sud-ouest', 'verdun', 'ville-marie', 'villeray–saint-michel–parc-extension', 'westmount']


    if borough.lower()=="montreal":
        req=requests.get("https://santemontreal.qc.ca/en/public/coronavirus-covid-19/situation-of-the-coronavirus-covid-19-in-montreal/#c43674")

        soup=bs4.BeautifulSoup(req.text,"html.parser")

        closer=soup.find("div", { "id" : "c43669" })
        mydivs = closer.find("p", {"class": "bodytext"})
        date=mydivs.text

        htmltable = soup.find('table', { 'class' : 'contenttable' })
        headingtags=["h3","h4"]

        data=[]

        for tags in htmltable.find_all(headingtags):
            data.append(tags.text.strip())

        for i in range(4):
            key=data[i+1+i]
            key = key.replace(u'\xa0', u' ')
            dic[key]=data[i*2]

        output="Montreal %s : \n"%(date)
        for i in dic:
            output+=("%s : %s\n"%(i,dic[i]))
        
        await ctx.channel.send(output)

    elif borough.lower() in areas:

        csvstuff=requests.get("https://santemontreal.qc.ca/fileadmin/fichiers/Campagnes/coronavirus/situation-montreal/municipal.csv",allow_redirects=True)
        open('boroughs.txt', 'wb').write(csvstuff.content)

        dic["borough"]={}

        with open('boroughs.txt','r') as csvfile:
            csvreader=csv.reader(csvfile, delimiter=';')
            for row in csvreader:
                
                dic["borough"][row[0].lower()]={}
                dic["borough"][row[0].lower()]["Cases in the past 24 hours"]=row[1]
                dic["borough"][row[0].lower()]["Cases in the past 2 weeks"]=row[2]
                dic["borough"][row[0].lower()]["cases per 100,000 in the past 2 weeks"]=row[3]
                dic["borough"][row[0].lower()]["Cumulative cases since start of pandemic"]=row[4]
                dic["borough"][row[0].lower()]["cases per 100,000 since start ofpandemic"]=row[5]

        output="%s : \n\n"%(borough.lower())
        for i in dic["borough"][borough]:
            output+="%s : %s\n"%(i,dic["borough"][borough][i])
        
        await ctx.channel.send(output)

    elif borough.lower()=="quebec":
        driver = webdriver.Chrome()
        driver.get("https://www.quebec.ca/en/health/health-issues/a-z/2019-coronavirus")

        elem = driver.find_elements_by_id("date-situation")
        y=(elem[0].text)

        y=y.split('\n')

        date=",".join(y)

        elem = driver.find_elements_by_id("donnees-situation")
        x=(elem[0].text)

        x=x.split('\n')

        driver.close()

        output=""

        confcase= x[0]+" : %s %s \n"%(x[1],x[2])

        hospi=x[3]+" : %s  %s \n"%(x[4],x[5])

        deaths=x[6]+" : %s  %s \n"%(x[7],x[8])

        output=date+"  :\n\n"+confcase+hospi+deaths

        await ctx.channel.send(output)

    else:
        await ctx.channel.send("Not a place, nerd")

@bot.command()
async def logs(ctx):

    if str(ctx.author)=="Treemonkey#5384":
        print('yo')
        req=requests.get("https://logs.tf/profile/76561198088171353")
        today = date.today() + timedelta(1)
        soup=bs4.BeautifulSoup(req.text,"html.parser")



        body=soup.find("tbody")

        tr=body.find_all("tr")

        for i in tr:
            days=i.find('td', {"class": "datefield"})
            current = today.strftime("%d-%b-%Y")

            if current==days.text.split(" ")[0]:
                link=i.find("a")
                output="https://logs.tf%s" %(link.get('href'))
                await ctx.channel.send(output)
            else :
                print("no more")
                break     
    else:
        pass

bot.run(TOKEN)