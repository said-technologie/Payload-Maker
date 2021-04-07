#payload maker
#creat by RaMsY
#payload v1.0
###############modules################
import os
import time
import sys
from core.Paycore import *
from core.banner import *
import subprocess
import pkg_resources

############the programme############
def payload():
    os.system("clear")
    banner_front()
    print("\033[36m                 ["+"\033[31m?"+"\033[36m]"+"\033[33m this version work only for linux systems")
    print("\033[33m                                        type "+"\033[32mstart "+"\033[33mto initialized the programme")
    while True:
        options = ['start']
        p = input(" \033[36m  \n PaMake]=>> "+"\033[37m")
        if p in options :
            print("\033[32m starting...")
            time.sleep(3)
            start()
        elif p == "exit":
            print("\033[36m  ["+"\033[31m!"+"\033[36m]" +"\033[33m exiting...  "+"\033[37m")
            time.sleep(3)
            print("\033[36m  ["+"\033[32m+"+"\033[36m]"+"\033[32m Thanks for using Payload-Maker"+"\033[37m")
            sys.exit()
        else :
            print("\033[35m ["+"\033[31m?"+"\033[35m]"+"\033[31m Wrong Input the "+"\033[33m"+p+"\033[31m it not found")
            print("\033[36m ["+"\033[32m+"+"\033[36m]"+"\033[33m"+"\033[33m type "+"\033[32m start "+"\033[33mto initialized the programme")
if __name__ == "__main__":
    payload()
