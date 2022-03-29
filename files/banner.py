import os
from files.colors import *


logo = f"""
   ▄████████    ▄████████    ▄█   ▄█▄    ▄████████    ▄████████ 
  ███    ███   ███    ███   ███ ▄███▀   ███    ███   ███    ███ 
  ███    █▀    ███    ███   ███▐██▀     ███    █▀    ███    ███ 
 ▄███▄▄▄       ███    ███  ▄█████▀     ▄███▄▄▄      ▄███▄▄▄▄██▀ 
▀▀███▀▀▀     ▀███████████ ▀▀█████▄    ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
  ███          ███    ███   ███▐██▄     ███    █▄  ▀███████████ 
  ███          ███    ███   ███ ▀███▄   ███    ███   ███    ███ 
  ███          ███    █▀    ███   ▀█▀   ██████████   ███    ███ 
                            ▀                        ███    ███ 
   ▄██████▄     ▄████████ ███▄▄▄▄                               
  ███    ███   ███    ███ ███▀▀▀██▄                             
  ███    █▀    ███    █▀  ███   ███                             
 ▄███         ▄███▄▄▄     ███   ███                             
▀▀███ ████▄  ▀▀███▀▀▀     ███   ███                             
  ███    ███   ███    █▄  ███   ███                             
  ███    ███   ███    ███ ███   ███                             
  ████████▀    ██████████  ▀█   █▀   

            {c}<{w}/{c}> {y}Author: {g}Saad Khan {r}| {g}Cyber-Dioxide


{ran}[ + ] Instagram @cyber_dioxide
{c}[ + ] Coding Instagram @cyber_dioxide_
{y}[ + ] Github: Cyber-Dioxide                                                                                                          
"""




def banner():
    print(ran + logo)

def banner2():

    print(ran + "\n","|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX,  "- " * 4, " [+] Follow me on Instagram @cyber_dioxide ", "- " * 4 + ran + "|")
    print(ran + "\n","|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, " [+] Follow me on Instagram @cyber_dioxide_ ", "- " * 4+ran + "|")
    print(ran + "\n","|"+ Style.BRIGHT + Fore.LIGHTRED_EX,  "- " * 4, "[+] Github: https://github.com/Cyber-Dioxide/ ", "- " * 3+ran + "|")

def clear():
    os.system("clear")