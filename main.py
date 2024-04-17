from socket import socket , AF_INET , SOCK_STREAM , setdefaulttimeout
from colorama import Fore , init
from pystyle import Colorate , Colors
from sys import exit
from os import system , name
from threading import Thread

init()

red = Fore.LIGHTRED_EX; green = Fore.LIGHTGREEN_EX; blue = Fore.LIGHTBLUE_EX; yellow = Fore.LIGHTYELLOW_EX; cyan = Fore.LIGHTCYAN_EX; white = Fore.LIGHTWHITE_EX; magenta = Fore.LIGHTMAGENTA_EX;

system('cls' if name == 'nt' else 'clear')

try:
    system('title The Nun Scan - Port Scan - Created By John Wick - Team Pytho Learn')
except:
    pass

banner = '''
                                                                       
            ooooo 8               o    o                .oPYo.                     
            8   8               8b   8                8                          
            8   8oPYo. .oPYo.   8`b  8 o    o odYo.   `Yooo. .oPYo. .oPYo. odYo. 
            8   8    8 8oooo8   8 `b 8 8    8 8' `8       `8 8    ' .oooo8 8' `8 
            8   8    8 8.       8  `b8 8    8 8   8        8 8    . 8    8 8   8 
            8   8    8 `Yooo'   8   `8 `YooP' 8   8   `YooP' `YooP' `YooP8 8   8 
            ::..::..:::..:.....:::..:::..:.....:..::..:::.....::.....::.....:..::..
            :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
            :::::::::::::::::::::::: Created By John Wick ::::::::::::::::::::::::::
'''

print(Colorate.Horizontal(Colors.red_to_blue,banner,2))

target = input(f'\n {red}[{yellow}+{red}]{green} Enter Your Target {red}:{blue} ')

def main():
    try:
        for port in range(20 , 65535):
            s = socket(AF_INET , SOCK_STREAM)
            setdefaulttimeout(0.1)
            r = s.connect_ex((target,port))
            if r == 0:
                print(Colorate.Horizontal(Colors.green_to_cyan,f'\n  [+] Host : {target} | Open_Port : {port} | xD',2))
    except KeyboardInterrupt:
        exit()
    except socket.timeout:
        print(f'Close {port}')

Thread(target=main).start()
