#!/usr/bin/python3 

"IMPORTS"
import os,sys,time,getpass
from platform import system

"COLORS"
green='\033[32m'
blue='\033[34m'
red='\033[31m'
white='\033[37m'
black='\033[30m'
pink='\033[95m'
end="\033[0m"

"RESIZE"
os.system("resize -s 25 95 > /dev/null")

"Functions To Help Me Later"

def remv():
	os.system("rm -r /var/lib/dpkg/lock")
	os.system("rm -r /var/cache/apt/archives/lock")

def hit():
	input("Hit Enter to Continue Or Ctrl + C To Exit : ")

def clear():
	os.system("clear && clear")

def Connection():
	cmd = cdm = os.system('ping -c 1 google.com')
	clear()
	if cdm == 512 :
		clear()		
		print("\n")
		print(red+'[!] This Tool Need Internet Connection ')
		print("\n")		
		sys.exit(1)
	else :
		time.sleep(1)
		print("[+] Internet Connection"+green+"		[CONNECTED]"+end)
		time.sleep(1)
def root():

	Root = os.getuid()
	if Root != 0:
		clear()
		print(red+"[!] Run This Script as Root"+end)
		exit(1)
	else :
		print("Run As Root"+green+"	   [OK]")
		time.sleep(1)
		print("")

linux = system()
if linux != "Linux":
	print(red+"[!] OS = {}".format(linux()))
	print("[!] Linux / Unix Required ")
	sys.exit(1)
else:
	pass

"Logo or Banner"
def banner():
	
		clear()
		time.sleep(1)
		print(green+"""


		██╗      █████╗ ███████╗██╗   ██╗     ██████╗ ██╗   ██╗
		██║     ██╔══██╗╚══███╔╝╚██╗ ██╔╝     ██╔══██╗╚██╗ ██╔╝
		██║     ███████║  ███╔╝  ╚████╔╝█████╗██████╔╝ ╚████╔╝ 
		██║     ██╔══██║ ███╔╝    ╚██╔╝ ╚════╝██╔═══╝   ╚██╔╝  
	     	███████╗██║  ██║███████╗   ██║        ██║        ██║   
		╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝        ╚═╝        ╚═╝   
""")
            
"Time To Code and Shut UP :) "
def main():

	try:
		banner()
		print("")
		print(white+"""		
			    Coded By 	:>	 {0}
			    Date	:>	 {1}

				[1]>	Update & Upgrade
				[2]>	Install PIP
				[3]> 	Install Python-Modules
				[4]> 	Install Github Tools
				[5]> 	ABOUT ME  (black15)
					
				[0]> 	[ EXIT ]
	""".format(blue+"black15"+end+white,blue+"28/08/2018"+end+white)+end)
		lazy = str(input("	[?]#> "))

		def up():
			os.system("apt update")
			remv()
			yesono = str(input(blue+"\n[?] Do U Want To Upgrade [Y/N] #> "+end))
			if yesono == "Y" or yesono == "y":
				os.system("apt full-upgrade -y")
				print("")
				hit()
				time.sleep(1)
				remv()
				main()
			else :
				print(red+"[!] OK "+end)
				hit()
				main()

		def pip():
			os.system("apt update")
			print("")
			print(white+"Witch Version of PiP to Install :")
			print("")
			print("""
		1) PIP
		2) PIP3
	""")
			ver = str(input("		[?]#> "+end))
			if ver == "1":
				remv()
				os.system("apt install python-pip -y")
				print("")
				print("")
				hit()
				remv()
				main()
			elif ver == "2":
				os.system("apt install python3-pip -y")
				remv()
				print("")
				print("")
				hit()
				main()

			else:
				print(red+"[!] Wrong Answer")
				hit()
				main()
		def pyModules():
			logo = red+"""








_░▒███████	       	   /$$      /$$                 /$$           /$$                    
░██▓▒░░▒▓██		  | $$$    /$$$                | $$          | $$                    
██▓▒░__░▒▓██___██████	  | $$$$  /$$$$  /$$$$$$   /$$$$$$$ /$$   /$$| $$  /$$$$$$   /$$$$$$$
██▓▒░____░▓███▓__░▒▓██	  | $$ $$/$$ $$ /$$__  $$ /$$__  $$| $$  | $$| $$ /$$__  $$ /$$_____/
██▓▒░___░▓██▓_____░▒▓██	  | $$  $$$| $$| $$  \ $$| $$  | $$| $$  | $$| $$| $$$$$$$$|  $$$$$$ 
██▓▒░_______________░▒▓██ | $$\  $ | $$| $$  | $$| $$  | $$| $$  | $$| $$| $$_____/ \____  $$
_██▓▒░______________░▒▓██ | $$ \/  | $$|  $$$$$$/|  $$$$$$$|  $$$$$$/| $$|  $$$$$$$ /$$$$$$$/
__██▓▒░____________░▒▓██  |__/     |__/ \______/  \_______/ \______/ |__/ \_______/|_______/ 
___██▓▒░__________░▒▓██
____██▓▒░________░▒▓██
_____██▓▒░_____░▒▓██
______██▓▒░__░▒▓██
_______█▓▒░░▒▓██
_________░▒▓██
_______░▒▓██
_____░▒▓██                                                                   
                                                                   
                                                                   

"""+end

			print(logo)
			hit()
			clear()
			time.sleep(1)
			anon = os.path.exists("/usr/bin/pip")
			if anon == True:
				print ("")
				print ("")
				print (green+"\n	[+] pip 		[FOUND]")
				print ("")
			else :
				print (red+"\n	[!] pip 		[NOT FOUND]")
				print ("	Do U Want To Install PIP [Y/N] "+end)
				print ("")
				nigga = str(input("[?]#> "))
				if nigga == "y" or nigga == "Y":
					remv()
					pip()
				else:
					hit()
					main()
			anon2 = os.path.exists("/usr/bin/pip3")
			if anon2 == True:
				print (green+"	[+] pip3          	[FOUND]")
				print ("")
			else:
				print (red+"	[!] pip3         	[NOT FOUND]")
				print ("	Do U Want To Install PIP3 [Y/N] "+end)
				print ("")
				nigga2 = str(input("[?]#> "))
				if nigga2 == "y" or nigga2 == "Y":
					remv()
					pip()
				else:
					hit()
					main()
			print(white+"""

	1)  urllib 		[pip3,pip]		9)  Random		[pip3,pip]
	2)  Mechanize		[pip3,pip]		10) PyQT		[pip3,pip]
	3)  BeautifulSoup	[pip3,pip]		11) OptParse		[pip3,pip]
	4)  PyAutoGUI		[pip3,pip]		12) SMTPLib		[pip3,pip]
	5)  Selenium		[pip3,pip]		13) FTPLib		[pip3,pip]
	6)  PyGame		[pip3,pip]		14) PxSsh		[pip3,pip]
	7)  Tqdm		[pip3,pip]		15) Xmpppy		[pip3,pip]
	8)  Socket		[pip3,pip]		16) HashLib		[pip3,pip]
							17) Thread		[pip3,pip]
					
				    	   99) [ Back ]
	""")
			module = str(input("[?]#> "))
			if module == "1":
				os.system("pip3 install urllib3")
				os.system("pip install urllib")
				hit()
				main()
			elif module == "2":
				os.system("pip3 install mechanicalsoup")
				os.system("pip install mechanize")
				hit()
				main()
			elif module == "3":
				os.system("pip3 install bs4")
				os.system("pip install bs4")
				hit()
				main()
			elif module == "4":
				os.system("pip3 install pyautogui")
				os.system("pip install pyautogui")
				hit()
				main()
			elif module == "5":
				os.system("pip3 install selenium")
				os.system("pip install selenium")
				hit()
				main()
			elif module == "6":
				os.system("pip3 install pygame")
				os.system("pip install pygame")
				hit()
				main()
			elif module == "7":
				os.system("pip3 install tqdm")
				os.system("pip install tqdm")
				hit()
				main()
			elif module == "8":
				os.system("pip3 install socket")
				os.system("pip install socket")
				hit()
				main()
			elif module == "9":
				os.system("pip3 install random")
				os.system("pip install random")
				hit()
				main()
			elif module == "10":
				os.system("pip3 install pyqt")
				os.system("pip install pyqt")
				hit()
				main()
			elif module == "11":
				os.system("pip install optparse")
				os.system("pip3 install optparse")
				hit()
				main()
			elif module == "12":
				os.system("pip install smtplib")
				os.system("pip3 install smtplib")
				hit()
				main()
			elif module == "13":
				os.system("pip install ftplib")
				os.system("pip3 install ftplib")
				hit()
				main()
			elif module == "14":
				os.system("pip install pxssh")
				os.system("pip3 install pxssh")
				hit()
				main()
			elif module == "15":
				os.system("pip install xmppy")
				os.system("pip3 install xmppy")
				hit()
				main()
			elif module == "16":
				os.system("pip3 install hashlib")
				os.system("pip install hashlib")
				hit()
				main()
			elif module == "17":
				os.system("pip install thread")
				os.system("pip3 install thread")
				hit()
				main()
			elif module == "99":
				clear()
				main()

			else :
				print(red+"[!] Wrong Choice "+end)
				hit()
				clear()
				pyModules()
		def tools():
			clear()
			print(red+"""




			▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
			▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
			▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
			░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
			  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
			  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
			    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
			  ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
				     ░ ░      ░ ░      ░  ░      ░  
						                    

"""+end)
			hit()
			clear()
			time.sleep(1)
			print(white+"""



				   @> Programming Languages
			1) Python3.x
			2) Perl
			3) Ruby
			4) PHP
	
					@> Github Tool
			5)  Veil-Evation		12) Cupp
			6)  Empire			13) Fsociety
			7)  Shellphish			14) Backdoor-Apk
			8)  Blackeye			15) Katoolin		 
			9)  Evil-Droid			16) FaceBash
			10) Netool-SH 			17) InstaShell
			11) Deliver			18) Fluxion
	
					19)  Custom		
					99) [ BACK ]
""")
			
			git = str(input("	[?]#> "+end))
			if '1' in git or '2' in git or '3' in git or '4' in git :remv()
			if git == "1":
				os.system("apt install python3")
				hit()
				clear()
				tools()
			elif git == "2":
				os.system("apt install perl")
				hit()
				clear()
				tools()
			elif git == "3":
				os.system("apt install ruby")
				hit()
				clear()
				tools()
			elif git == "4":
				os.system("apt install php")
				hit()
				clear()
				tools()
			elif git == "5":
				os.system("git clone https://github.com/Veil-Framework/Veil-Evasion")
				hit()
				clear()
				tools()
			elif git == "6":
				os.system("git clone https://github.com/EmpireProject/Empire")
				hit()
				clear()
				tools()
			elif git == "7":
				os.system("git clone https://github.com/thelinuxchoice/shellphish")
				hit()
				clear()
				tools()
			elif git == "8":
				os.system("git clone https://github.com/thelinuxchoice/blackeye")
				hit()
				clear()
				tools()
			elif git == "9":
				os.system("git clone https://github.com/M4sc3r4n0/Evil-Droid")
				hit()
				clear()
				tools()
			elif git == "10":
				os.system("git clone https://github.com/r00t-3xp10it/netool-toolkit")
				hit()
				clear()
				tools()
			elif git == "11":
				os.system("git clone https://github.com/M4sc3r4n0/deliver")
				hit()
				clear()
				tools()
			elif git == "12":
				os.system("git clone https://github.com/Mebus/cupp")
				hit()
				clear()
				tools()
			elif git == "13":
				os.system("git clone https://github.com/Manisso/fsociety")
				hit()
				clear()
				tools()
			elif git == "14":
				os.system("git clone https://github.com/dana-at-cp/backdoor-apk")
				hit()
				clear()
				tools()
			elif git == "15":
				os.system("git clone https://github.com/LionSec/katoolin")
				hit()
				clear()
				tools()
			elif git == "16":
				os.system("git clone https://github.com/thelinuxchoice/facebash")
				hit()
				clear()
				tools()
			elif git == "17":
				os.system("git clone https://github.com/thelinuxchoice/instashell")
				hit()
				clear()
				tools()
			elif git == "18":
				os.system("git clone https://github.com/wi-fi-analyzer/fluxion")
				hit()
				clear()
				tools()
			elif git == "99":
				clear()
				main()
				tools()
			elif git == "19":
				print("What Tool You Wanna Install")
				cus = str(input("[?]#> "))
				os.system("apt install {}".format(cus))
				hit()
				clear()
				tools()
			else:
				print(red+"[!] Wrong Answer "+end)
				hit()
				clear()
				tools()
		def meSoc():

			clear()
			print("\t")
			print("\t")
			print(blue+"FACEBOOK	:->	www.facebook.com/unknownkid18")
			print(black+"GITHUB		:->	www.github.com/black15")
			print(pink+"INSTAGRAM	:->	www.instagram.com/10_oussama_01")
			print(red+"YOUTUBE		:->	https://www.youtube.com/channel/UClF7WD_UzJ1kgC_RdznfQbQ"+end)
			print("\t")
			print("\t")			
			hit()
			clear()
			main()
			print('\t')

		if lazy == "1":
			clear()
			up()
		elif lazy == "2":
			clear()
			pip()
		elif lazy == "3":
			clear()
			pyModules()
		elif lazy == "4":
			clear()
			tools()
		elif lazy == "5":
			meSoc()
		elif lazy == "0":
			time.sleep(1)
			clear()
			print(red+"[!] EXITING ")
			print("")
			sys.exit(1)
		else:
			print(red+"[!] Wrong Choice "+end)
			hit()
			clear()
			main()
	except KeyboardInterrupt:
		clear()
		print(red+"[!] Ctrl +C Was Pressed !")
		print("[!] Cleaning ..")
		os.system("apt clean")

if __name__ == "__main__":
	clear()
	root()
	Connection()
	banner()
	main()

