import os
import re
try:
	import requests
except:
    os.system("pip3 install requests")
    if (os.name) == 'nt':
      os.system("cls")
    else:
      os.system("clear")
      print("\33[101mNow restart the program")
      exit()
import threading
print('\033[1;33;40m------------[+] Tomcat default directory finder by Rc  [+]----------\n')
fname = input('\033[1;37;40mEnter The File Name Which Contains The Subdomains \n\n\033[1;32;40mroot@rc #~ ')
try:
    global f
    f = open(fname)
    g = open(fname)
except:
	import os
	os.system('clear')
	print("\033[1;34;40m[+] File Not Found [+]")
	quit
def dirfinder(webs):
	res = []
	src = requests.get(f"{webs}/examples/")
	src_code = src.text
	if re.search('Servlets examples', src_code):
		print("\033[1;32;40m[+] Found /examples/servlets on the website [+]")
		res.append('ser')
	else:
		print("\033[1;37;40m[*] Unable to find /examples/servlets on the website [*]")
	if re.search('JSP Examples', src_code):
		print("\033[1;32;40m[+] Found /examples/jsp on the website [+]")
		res.append('jsp')
	else:
		print("\033[1;37;40m[*] Unable to find /examples/jsp on the website [*]")
	if re.search('WebSocket Examples', src_code):
		print("\033[1;32;40m[+] Found /examples/websocket/index.xhtml on the website [+]")
		res.append('webs')
	else:
		print("\033[1;37;40m[*] Unable to find /examples/websocket/index.xhtml on the website [*]")
	print("Results : ")
	if 'ser' in res:
		print(f"\033[1;32;40m[+] URL : {webs}/examples/servlets [+]")
	else:
		pass
	if 'jsp' in res:
		print(f"\033[1;32;40m[+] URL : {webs}/examples/jsp [+]")
	else:
		pass
	if 'webs' in res:
		print(f"\033[1;32;40m[+] URL : {webs}/examples/websocket/index.xhtml [+]")
	else:
		pass
def checkdir(site):
	print("\033[1;30;40m[+] Checking if the example directory exits or not [+]")
	try:
		webs = requests.get(f"{site}/examples/")
		txt = webs.text
		if re.search("Apache Tomcat Examples", txt):
			print("\033[1;31;40m[*] Example Directory Exits [*]")
			chck = input("\033[1;32;40mDo you want to search all the available example files (y/N) : ")
			chck.lower
			if chck == 'y':
				dirfinder(site)
			else:
				pass
		else :
			print("\033[1;31;40m[?] Example directory doesnt exits [?]")
	except:
		pass
def full(i):
	i = i.replace('\n', '')
	print(f"\n[+] URL : {i} [+]")
	print("\033[1;33;40m[+] Testing connection... [+]")
	try:
		resp = requests.get(i)
		if resp.status_code == 200:
			print(f"\033[1;32;40m[+] Connection successful [+]\n")
			checkdir(i)
#print(j)
		elif resp.status_code == 301:
  			print(f'\033[1;32;40m;;[-] Redirected 301 [-]')
		elif resp.status_code == 404:
  			print(f'\033[1;31;40m[-] 404 Not Found [-]')
		elif resp.status_code == 403:
  			print(f"\033[1;36;40m[-] 403 Forbidden/Redirecting[-]")
		elif resp.status_code == 400:
  			print(f'\033[1;30;40m[-] 400 Bad Request [-]')
		else :
  			print(f"\033[1;34;40m[@] Status : {resp.status_code} [@]")
	except requests.ConnectionError:
  		print("\033[1;31;40m[!] Unable to connect [!]")
global i
for i in f:
	full(i)