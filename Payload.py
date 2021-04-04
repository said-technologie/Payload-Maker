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
from connection_cheeker import connection
###########cheking the  modules#########
required = {'socket', 'webbrowser'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
############the programme############
def payload():
    os.system("clear")
    banner_front()
    print("\033[36m                 ["+"\033[31m?"+"\033[36m]"+"\033[33m this version work only for linux systems")
    print("\033[33m                                        type "+"\033[32m start "+"\033[33mto initialized the programme")
    while True:
        options = ['start']
        p = input(" \033[36m  \n PaMake]=>> "+"\033[37m")
        if p in options :
            print("\033[32m starting...")
            time.sleep(3)
            start()
        elif p == "exit":
            sys.exit()
        else :
            print("\033[35m ["+"\033[31m?"+"\033[35m]"+"\033[31m Wrong Input the "+"\033[33m"+p+"\033[31m it not found")
            print("\033[36m ["+"\033[32m+"+"\033[36m]"+"\033[33m"+"\033[33m type "+"\033[32m start "+"\033[33mto initialized the programme")
if __name__ == "__main__":
    payload()
