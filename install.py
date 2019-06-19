import os
import time

class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    OKBLUE = '\033[94m'
    
print ('\033[94m[1] for kali')
print ('\033[94m[2] for termux')
tool = raw_input('\033[1mprotocol ==> ')
if tool == "1" or tool == "01":
    os.system('apt-get update')
    os.system('apt-get install nmap')
    os.system('apt-get install python-pip')
    os.system('pip install requests')
    os.system('pip install BeautifulSoup')
    os.system('pip install tabulate')
    os.system('pip install pandas')
    os.system('pip install bs4')
    print ("\033[92m##done##")
     
     
elif tool == "2" or tool == "02":
    os.system('pkg update')
    os.system('pkg upgrade')
    os.system('pkg install nmap')
    os.system('pkg install python')
    os.system('pkg install python-pip')
    os.system('pip install requests')
    os.system('pip install BeautifulSoup')
    os.system('pip install tabulate')
    os.system('pip install pandas')
    os.system('pip install bs4')
    print ("\033[92m##done##")
 
     
