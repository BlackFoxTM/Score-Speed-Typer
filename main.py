from random import randint as rand
from time import sleep
import os , sys
try:
    from colorama import Fore 
    from pyfiglet import Figlet
    import requests
except:
    print ("[-] Installing Requirements Progress ....")
    if "win" in sys.platform:
        os.system("pip install requests pyfiglet colorama & cls")
    else:
        os.system("pip3 install colorama requests pyfiglet && clear")
    from pyfiglet import Figlet
    from colorama import Fore
    import requests

def score_hack(username,score):
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.62 Safari/537.36","Content-Type":"application/x-www-form-urlencoded","Cookie":"temp=typingspeed; disable_cookie_msg=1; text-language_cookie=en; __gads=ID=13feff942d86fb8f-220fc23958ce008f:T=1666846696:RT=1666846696:S=ALNI_Mbaewfm1-A1oNLbVKxYKRTcAkYYTw; __gpi=UID=00000b78aef701ec:T=1666846696:RT=1666846696:S=ALNI_Mbl9lRdb_T0IclQ5vJz5vZ6-smZWw"}
    payload = f'key_strokes={score}&letters_correct={score}&letters_half_correct=0&letters_wrong=0&words_correct=47&words_half_correct=0&words_wrong=0&corrections=21&max_speed=9&text_lang=en&keyboard_type=standard&countdown_minutes=1&v="Kos"&t=182376000b7ae1ceaf32d8d0c4f3f1aa'
    url = "https://typing-speed.net/score"
    req = requests.post(url , headers=header , data=payload)
    if req.status_code == 200:
        text_js_id = req.text
        rs = text_js_id.split(",")[1].split("'")[1]
        payload_no = f"score_id={rs}&name={username}"
        resp = requests.post(url,headers=header,data=payload_no)
        return (Fore.YELLOW + "[+] The Operation has been successfully\n[+] Check Rank to be Show !" + Fore.WHITE)
    else:
        return (Fore.RED + "[#] Failed :( , Try Again Later !" + Fore.WHITE)

print (Fore.BLUE + Figlet(font="small").renderText("Fox Hk Typer"))
print (Fore.RED + "\t[$] Hack Score Speed of Typing Tool ")
print (Fore.RED + "\t[$] Author ~ > Maximum Radikali")
print (Fore.RED + "\t[$] Telegram Channel : @BlackFoxSecurityTeam")

username = input(Fore.MAGENTA + "[-] Enter Your Name that be show on rank list : ")
score = input(Fore.GREEN + "[-] Enter your desired Score : ")
print (score_hack(username,score))



