import discord
import colorama
from colorama import Fore
from colorama import Back
from colorama import Style
import os
os.system("mode con cols=77 lines=27")
import requests
import time
import random
import init
import sys
import subprocess

client = discord.Client()

def Clear():
    os.system('')
Clear()

print(f"""{Fore.GREEN}{Style.BRIGHT}
          .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'  {Fore.WHITE}{Fore.GREEN}{Style.BRIGHT}{Fore.GREEN}{Style.BRIGHT}   `98v8P' {Fore.WHITE}{Fore.GREEN}{Style.BRIGHT} `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
          {Fore.WHITE}MASS{Fore.GREEN}{Style.BRIGHT}        dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb        {Fore.WHITE}BY{Fore.GREEN}{Style.BRIGHT} 
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
          {Fore.WHITE}DM{Fore.GREEN}{Style.BRIGHT}                   XXXX X.`v'.X XXXX                 {Fore.WHITE}NAX{Fore.GREEN}{Style.BRIGHT} 
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d' 


""")  

token = input(f"{Fore.GREEN}{Style.BRIGHT}~input{Fore.WHITE}@{Fore.GREEN}{Style.BRIGHT}token{Fore.WHITE}> ")
head = {'Authorization': str(token)}
headers = {'Authorization': token, 'Content-Type': 'application/json'} 
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head) 

if src.status_code == 401:
        print(f"{Fore.GREEN}{Style.BRIGHT}~token{Fore.WHITE}@{Fore.GREEN}{Style.BRIGHT}invalid{Fore.WHITE}... ")
        exit()
elif src.status_code == 200:
        print(f"{Fore.GREEN}{Style.BRIGHT}~token{Fore.WHITE}@{Fore.GREEN}{Style.BRIGHT}accepted{Fore.WHITE}... ")
else:
        print(f"{Fore.GREEN}{Style.BRIGHT}~internal{Fore.WHITE}@{Fore.GREEN}{Style.BRIGHT}error{Fore.WHITE}: ")
        input()
        exit()

while True:
    T = input(f"{Fore.GREEN}{Style.BRIGHT}~input{Fore.WHITE}@{Fore.GREEN}{Style.BRIGHT}message{Fore.WHITE}> ")
    if T=="text":
        exit(0)
    else:
        print(f"{Fore.GREEN}{Style.BRIGHT}~tbk{Fore.WHITE}@{Fore.GREEN}{Style.BRIGHT}loading{Fore.WHITE}... ")
        break

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send (T)
      print(f"{Fore.GREEN}{Style.BRIGHT}~tbk{Fore.WHITE}@{Fore.GREEN}{Style.BRIGHT}sentmsg{Fore.WHITE}: {user.name}")
    except:
       print(f"{Fore.GREEN}{Style.BRIGHT}~tbk{Fore.WHITE}@{Fore.GREEN}{Style.BRIGHT}failedmsg{Fore.WHITE}: {user.name}")

client.run(token, bot=False)