# bot.py
from http import client
import json
import os
from pydoc import cli
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
from requests import get
import requests
import asyncio
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_ready():
    # (name='test'))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="cene ETH"))
    guild = discord.utils.find(lambda g: g.name == GUILD, bot.guilds)
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})')
    while not bot.is_closed():
        channel = bot.get_channel(542748371912491049)
        url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ethereum&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h"
        response = requests.get(url)
        data = response.json()
        eth_price = data[0]['current_price']
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"ETH {eth_price}$"))
        # await channel.send(data[0]['price_change_percentage_1h_in_currency'])
        await asyncio.sleep(60)


@ bot.command()
async def pis(ctx):
    autor_full = str(ctx.author)
    await ctx.send(f'{autor_full[0:-5]}, jebac pis')


@ bot.command()
async def zloto(ctx):
    url = f'http://api.nbp.pl/api/cenyzlota/'
    resp = get(url)
    data = resp.json()
    exchange_rate = data[0]['cena']
    await ctx.send(f"zloto kosztuje {exchange_rate}")


@ bot.command()
async def eur(ctx):
    url = f'http://api.nbp.pl/api/exchangerates/rates/a/EUR/'
    resp = get(url)
    data = resp.json()
    exchange_rate = data['rates'][0]['mid']
    await ctx.send(f"Ostatni kurs euro to {exchange_rate} PLN")


@ bot.command()
async def usd(ctx):
    url = f'http://api.nbp.pl/api/exchangerates/rates/a/usd/'
    resp = get(url)
    data = resp.json()
    exchange_rate = data['rates'][0]['mid']
    await ctx.send(f"Ostatni kurs dulara to {exchange_rate} PLN")


@ bot.command()
async def covid(ctx):
    url = "https://api.apify.com/v2/key-value-stores/3Po6TV7wTht4vIEid/records/LATEST"
    resp = get(url)
    data = resp.json()
    infected = data['infected']
    deceased = data['deceased']
    recovered = data['recovered']
    dailyInfected = data['dailyInfected']
    dailyTested = data['dailyTested']
    dailyPositiveTests = data['dailyPositiveTests']
    dailyDeceased = data['dailyDeceased']
    dailyRecovered = data['dailyRecovered']
    dailyQuarantine = data['dailyQuarantine']
    txtDate = data['txtDate']
    await ctx.send(f"Dane z dnia {txtDate}, umarło w sumie {deceased} \nnowych: {dailyInfected}, pozytywnych: {dailyPositiveTests}")


@ bot.command()
async def chf(ctx):
    url = f'http://api.nbp.pl/api/exchangerates/rates/a/chf/'
    resp = get(url)
    data = resp.json()
    exchange_rate = data['rates'][0]['mid']
    await ctx.send(f"Ostatni kurs franka to {exchange_rate} PLN")


@ bot.command()
async def quad(ctx):
    await ctx.send('Q   N\nU   A\nA   B\nD')


@bot.event
async def on_member_update(before, after):
    if str(after.status) == "online":
        print(f"{after.name} has gone {after.status}.")


@ bot.command()
async def eth(ctx):
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ethereum&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h"
    response = requests.get(url)
    data = response.json()
    await ctx.send(f'''
aktualna cena: {data[0]['current_price']}$
zmiana w 24h: {data[0]['price_change_percentage_24h']}
max w 24h: {data[0]['high_24h']}$
min w 24h: {data[0]['low_24h']}$
    ''')


# dziala tylko na moje ID
@ bot.command()
async def hello(ctx):
    if ctx.message.author.id == (690628563296059462):
        await ctx.send('co tam? jak mija dzien?')
    elif ctx.message.author.id != (690628563296059462):
        await ctx.send('czego chcesz biedaku?')


@ bot.command()
async def pomoc(ctx):
    await ctx.send('jeb sie, nie ma zadnej pomocy')
    await ctx.send(ctx.author)


@ bot.command()
async def rofl(ctx):

    rofl = ['https://tenor.com/view/laughing-laugh-funny-hilarious-drunk-gif-9612213',
            'https://tenor.com/view/lol-laughing-hysterically-laughing-out-loud-funny-steve-carell-gif-22904325']

    response = random.choice(rofl)
    await ctx.send(response)


@ bot.event
async def on_message(message):

    if message.author == bot.user:
        return
    if "rip" in message.content:
        gifs = ['https://tenor.com/view/rip-coffin-black-ghana-celebrating-gif-16743302',
                'https://tenor.com/view/dance-coffin-meme-rip-gif-16909625',
                'https://tenor.com/view/mati-bodoh-bangang-keranda-menari-gif-16794396',
                'https://tenor.com/view/coffin-dance-dancing-pallbearers-meme-funeral-dancers-gif-17562712',
                'https://tenor.com/view/coffin-dance-meme-gif-16984862',
                ]
        await message.channel.send(random.choice(gifs))
    if "lol" in message.content:
        gifs = ['https://tenor.com/view/laughing-laugh-funny-hilarious-drunk-gif-9612213',
                'https://tenor.com/view/dana-change-lol-miinions-laughing-gif-17467543',
                'https://tenor.com/view/atg-capa-stucapa-studiocapa-pandu-gif-24944581',
                'https://tenor.com/view/laugh-funny-rire-laughing-haha-gif-17070112',
                'https://tenor.com/view/laughing-lol-ha-ha-happy-gif-15717831',
                'https://tenor.com/view/el-risitas-juan-joya-borja-ratones-coloraos-laugh-meme-laughing-man-gif-24899295']
        await message.channel.send(random.choice(gifs))
    if 'gramy?' in message.content:
        await message.channel.send("w <:lostarkcentral:989259285361983498>?")
    if 'quad ' in message.content:
        await message.channel.send("<:quadnab:989258196428398622>")
    if "papiez " in message.content:
        gifs = ['https://tenor.com/view/jp2gmd-pope-john-paul-gif-11713430',
                'https://tenor.com/view/jp2gmd-pope-dance-gif-8448985',
                'https://tenor.com/view/rare-pope-jp2-moving-gif-14675228',
                'https://tenor.com/view/pope-john-paul-ii-pope-easter-gif-4001771',
                'https://tenor.com/view/papaj-jp2gmd-2137-pope-vatican-gif-7339313',
                'https://tenor.com/view/papiez-jp2-papaj-2137-tso-gif-12732593',
                'https://tenor.com/view/2137-gif-21926722'
                ]
        await message.channel.send(random.choice(gifs))
    if 'dzey' in message.content:
        await message.channel.send('dzey dzey\nwacha kley')
    if 'tusk' in message.content:
        await message.channel.send('https://tenor.com/view/tusk-deautschland-gif-22190125')
    if 'reddit.com' in message.content:
        await message.channel.send('https://tenor.com/view/monkey-read-old-news-gif-9870921')
    if ' pis ' in message.content:
        await message.channel.send('https://tenor.com/view/jebacpis-gif-19980630')
    if 'asmond' in message.content:
        await message.channel.send('Asmond? Chyba ASSmrond')
    if 'lost ark' in message.content:
        await message.channel.send('https://tenor.com/view/hasbulla-lost-ark-gaming-hasbulla-magomedov-lost-ark-time-gif-24873159')
    if 'mateusz' in message.content:
        await message.channel.send('Ktos coś pisał o vateuszu?')
        await message.channel.send('https://tenor.com/view/morawiecki-ryz-pis-explain-they-have-to-pay-for-a-bowl-of-rice-gif-17432276')
    await bot.process_commands(message)

on_member_update('offline', 'online')
bot.run(TOKEN)
