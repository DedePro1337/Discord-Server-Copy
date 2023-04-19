mytitle = "Discord Sunucu Kopyalama Dede"
from os import system
system("title "+mytitle)
import psutil
from pypresence import Presence
import time
import sys
client_id = 'Hesabının ID'
import discord
import time
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from serverclone import Clone

client = discord.Client(intents=discord.Intents.default())
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.RED}

 > {Fore.RED}Dede {Fore.RESET}Pro &{Fore.RED} Sum 

                                                                      
{Style.RESET_ALL}
{Fore.RED} > Discord {Fore.RESET} Sunucumuz {Fore.RED} discord.gg/ticaret {Style.RESET_ALL}
        """)

time.sleep(2)
token = input(f'{Fore.RED} > Token {Fore.RESET} Giriniz:\n{Fore.RED} >')
time.sleep(2)
guild_s = input(f'{Fore.RED} >{Fore.RESET} Kopyalanmasını İstediğiniz {Fore.RED} Sunucunun {Fore.RESET} ID:\n{Fore.RED} >')
time.sleep(5)
guild = input(f'{Fore.RED} > {Fore.RESET}Kopyalanıp {Fore.RED} Aktarılmasını {Fore.RESET} İstediğiniz {Fore.RED} Sunucunun {Fore.RESET} ID:\n{Fore.RED} >')
input_guild_id = guild_s  # <-- input guild id
output_guild_id = guild  # <-- output guild id
token = token  # <-- your Account token


print("  ")
print("  ")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"{Fore.RED} > Giriş Yapılan Hesap: {client.user}")
    print(f"{Fore.RED}> Sunucu {Fore.RESET} Kopyalanıyor!")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN} > Sunucu Kopyalanmıştır İyi Günler!
                                                                               
    {Style.RESET_ALL}""")
    await asyncio.sleep(5)
    client.close()

client.run(token, bot=False)
