import requests
from colorama import Fore, init
import colorama
import time
import os
from pystyle import *


#Batnet'den selamlar 25/04/23 21:06 Salı

os.system("cls")
init()
intro = """

 ▄▀▀█▄▄   ▄▀▀█▄   ▄▀▀▀█▀▀▄  ▄▀▀▀▀▄   ▄▀▀▀▀▄  ▄▀▀█▀▄    ▄▀▀▄ ▀▄  ▄▀▀▀█▀▀▄ 
▐ ▄▀   █ ▐ ▄▀ ▀▄ █    █  ▐ █      █ █ █   ▐ █   █  █  █  █ █ █ █    █  ▐ 
  █▄▄▄▀    █▄▄▄█ ▐   █     █      █    ▀▄   ▐   █  ▐  ▐  █  ▀█ ▐   █     
  █   █   ▄▀   █    █      ▀▄    ▄▀ ▀▄   █      █       █   █     █      
 ▄▀▄▄▄▀  █   ▄▀   ▄▀         ▀▀▀▀    █▀▀▀    ▄▀▀▀▀▀▄  ▄▀   █    ▄▀       
█    ▐   ▐   ▐   █                   ▐      █       █ █    ▐   █         
▐                ▐                          ▐       ▐ ▐        ▐         
                          > Press Enter
"""

Anime.Fade(Center.Center(intro), Colors.black_to_red, Colorate.Vertical, interval=0.035, enter=True)

targetuser = input("Enter Target Username For Search:")
f = open("result.txt","w")
f.write("All the found elements have been sorted for you <3. \n")


urlyoutube = requests.get('https://www.youtube.com/@'+targetuser)
if urlyoutube.status_code == 200:
    print(Fore.GREEN+"+ | Found On Youtube.com -> "+targetuser)
    f.write("Found On Youtube -> https://www.youtube.com/@"+targetuser+"\n")
else:
    print(Fore.RED+"- | I Cant find "+targetuser+" on Youtube.com")

urlinsta = requests.get('https://www.instagram.com/'+targetuser)
if urlinsta.status_code == 200:
    print(Fore.GREEN+"+ | Found On Instagram.com -> "+targetuser)
    f.write("Found On Instagram -> https://www.instagram.com/"+targetuser+"\n")
else:
    print(Fore.RED+"- | I Cant find "+targetuser+" on Instagram.com")

urltiktok = requests.get('https://www.tiktok.com/@'+targetuser)
if urltiktok.status_code == 200:
    print(Fore.GREEN+"+ | Found On Tiktok.com -> "+targetuser)
    f.write("Found On Tiktok -> https://www.tiktok.com/@"+targetuser+"\n")
else:
    print(Fore.RED+"- | I Cant find "+targetuser+" on Tiktok.com")

urlfacebook = requests.get('https://www.facebook.com/'+targetuser)
if urlfacebook.status_code == 200:
    print(Fore.GREEN+"+ | Found On Facebook.com -> "+targetuser)
    f.write("Found On Facebook -> https://www.facebook.com/"+targetuser+"\n")
else:
    print(Fore.RED+"- | I Cant find "+targetuser+" on Facebook.com")

urlpinterest = requests.get('https://tr.linkedin.com/in/'+targetuser)
if urlpinterest.status_code == 200:
    print(Fore.GREEN+"+ | Found On Linkedin.com -> "+targetuser)
    f.write("Found On Linkedin -> https://tr.linkedin.com/in/"+targetuser+"\n")
else:
    print(Fore.RED+"- | I Cant find "+targetuser+" on Linkedin.com")

urltelegram = requests.get('https://t.me/'+targetuser)
if urltelegram.status_code == 200:
    print(Fore.GREEN+"+ | Found On Telegram.com -> "+targetuser)
    f.write("Found On Telegram (Maybe Not?) -> https://t.me/"+targetuser+"\n")
else:
    print(Fore.RED+"- | I Cant find "+targetuser+" on Telegram.com")

urlreddit = requests.get('https://www.reddit.com/user/'+targetuser)
if urlreddit.status_code == 200:
    print(Fore.GREEN+"+ | Found On Reddit.com -> "+targetuser)
    f.write("Found On Reddit -> https://www.reddit.com/user/"+targetuser+"\n")
else:
    print(Fore.RED+"- | I Cant find "+targetuser+" on Reddit.com")

urltwitch = requests.get('https://www.twitch.tv/'+targetuser)
if urltwitch.status_code == 200:
    print(Fore.GREEN+"+ | Found On Twitch.com -> "+targetuser)
    f.write("Found On Twitch -> https://www.twitch.tv/"+targetuser+"\n")
else:
    print(Fore.RED+"- | I Cant find "+targetuser+" on Twitch.com")

urlwattpad = requests.get('https://www.wattpad.com/user/'+targetuser)
if urlwattpad.status_code == 200:
    print(Fore.GREEN+"+ | Found On Wattpad.com -> "+targetuser)
    f.write("Found On Wattpad -> https://www.wattpad.com/user/"+targetuser+"\n")
else:
    print(Fore.RED+"- | I Cant find "+targetuser+" on Wattpad.com")

urltumbler= requests.get('https://www.tumblr.com/'+targetuser)
if urltumbler.status_code == 200:
    print(Fore.GREEN+"+ | Found On Tumblr.com -> "+targetuser)
    f.write("Found On Tumblr -> https://www.tumblr.com/"+targetuser+"\n")
else:
    print(Fore.RED+"- | I Cant find "+targetuser+" on Tumblr.com")

urlonlyfans= requests.get('https://onlyfans.com/'+targetuser)
if urlonlyfans.status_code == 200:
    print(Fore.GREEN+"+ | Found On OnlyFans.com -> "+targetuser)
    f.write("Found On OnlyFans -> https://onlyfans.com/"+targetuser+"\n")
else:
    print(Fore.RED+"- | I Cant find "+targetuser+" on OnlyFans.com")

urlvsco = requests.get('https://vsco.co/'+targetuser+'/gallery')
if urlvsco.status_code == 200:
    print(Fore.GREEN+"+ | Found On Vsco.co -> "+targetuser)
    f.write("Found On Vsco -> https://vsco.co/"+targetuser+'/gallery \n')
else:
    print(Fore.RED+"- | I Cant find "+targetuser+" on Vsco.com")

urlsoundc = requests.get('https://soundcloud.com/'+targetuser)
if urlsoundc.status_code == 200:
    print(Fore.GREEN+"+ | Found On Soundcloud.com -> "+targetuser)
    f.write("Found On Soundcloud -> https://soundcloud.com/"+targetuser+"\n")
else:
    print(Fore.RED+"- | I Cant find "+targetuser+" on Soundcloud.com")

print("All avaible results are saved in result.txt")
time.sleep(5)
exit()