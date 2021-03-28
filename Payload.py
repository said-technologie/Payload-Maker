#payload maker 
#creat by RaMsY
#payload v1.0

###############modules################
import os 
import time 
import sys 
import socket
from core.Paycore import *
from core.banner import *
############the programme############
def payload():
    os.system("clear")
    banner_front()
    print("\033[36m                 ["+"\033[31m?"+"\033[36m]"+"\033[33m this version work only for linux systems")
    while True:
        p = input(" \033[36m  \n PaMake]=>> "+"\033[37m")
        if p == "help":
            time.sleep(3)
            print("\033[33m       "+r"  command                                          description")
            print("\033[36m  "+r"      set payload                             use this command to creat a payload")
            print("\033[36m  "+r"     show options                    it will show you what you have to do after creating a payload")
            print("\033[36m  "+r"    show cre_chann                          it will show you all the creator of this script acount")
            print("\033[32m                     subscribe to my youtube channel please")
            print("\033[36m  "+r"        help                                     it will show you this help menu")
            print("\033[36m  "+r"        clear                                       it will clear the window")
            print("\033[36m  "+r"        exit                                       it will exit the programme")
        if p == "set payload":
            paymak()
        elif p == "show options":
            command()
        elif p == "show cre_chann":
            youtube()
        elif p == "clear":
            os.system("clear")  
        elif p == "exit":
            print("\033[36m  ["+"\033[31m-"+"\033[36m]" +"\033[33m exiting...  "+"\033[37m")
            time.sleep(3)
            print("\033[36m  ["+"\033[32m+"+"\033[36m]"+"\033[32m Thanks for using Payload-Maker"+"\033[37m")
            sys.exit()

if __name__ == "__main__":
	payload()
