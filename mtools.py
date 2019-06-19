
import os
import time
from core.sources import *
from time import sleep as timeout

class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    OKBLUE = '\033[94m'
    
def main():
       banner()
       check()
       print ("\033[92m------------------------------------------------")
       print ("             \033[91m[01] \033[94mtools metasploit      ")
       print ("\033[92m------------------------------------------------")
       print ("             \033[91m[02] \033[94mscan sql web          ")
       print ("\033[92m------------------------------------------------")
       print ("             \033[91m[03] \033[94mTHFN(tools hide from the net)")
       print ("\033[92m------------------------------------------------")      
       print ("             \033[91m[99] \033[94mupdate script         ")
       print ("\033[92m------------------------------------------------")
       print ("\n   \033[91m[10] \033[94mExit the MT\n")
       hide = raw_input("\033[91mprotocol ==> ")
       if hide == "3" or hide == "03":
           print ("\033[92m-----------------------------------------")
           print ("\033[92m(0) \033[94madd proxy")
           print ("\033[92m-----------------------------------------")
           print ("\033[92m(1) \033[94mcheck your location")
           print ("\033[92m-----------------------------------------")
           print ("\033[92m(2)\033[94minstall lazyfix (tool for mode anonymous from the net)")
           print ("\033[92m-----------------------------------------")
           print ("            \033[92m(1) \033[94m[11]back")
           print ("\033[92m-----------------------------------------")
           proxy = raw_input("\033[91mprotocol ==> ")
           if proxy == "0":
               sprint()
           elif proxy == "1" or proxy == "01":
               loca()
           elif proxy == "2" or proxy == "02":
               lazyfix()
           elif proxy == "100":
               restart_program()
               
       elif hide == "2" or hide == "02":
               print ("\033[92m\nckeck sql website from file type yes or no")
               ok = raw_input('Enter y/n: ')
               if ok == 'y':
                   write()
               elif ok == 'n':
                   sql_injection()
               
       elif hide == "1" or hide == "01":
           print ("\033[92m-----------------------------------------")
           print ("\033[92m(0) \033[94minstall metasploit")
           print ("\033[92m-----------------------------------------")
           print ("\033[92m(1) \033[94mmake payloads")
           print ("\033[92m-----------------------------------------")
           print ("\033[92m(2)\033[94mopen listen session with metasploit")
           print ("\033[92m-----------------------------------------")
           print ("\033[92m(3) \033[94mhack with ip")
           print ("\033[92m-----------------------------------------")
           print ("\033[92m(4) \033[94mhack with link")
           print ("\033[92m-----------------------------------------")
           
           print ("\n   [00] Back to main menu\n")
           vun = raw_input("\033[91mprotocol ==> ")
           if vun == "0":
               metasploit()
           elif vun == "1" or vun == "01":
               print ("\033[91m(1) \033[94mmanual payloads")
               print ("\033[91m(2) \033[94mpython payload")
               print ("\033[91m(3) \033[94mperl payload")
               print ("\033[91m(4) \033[94mbash payload")
               print ("\033[91m(5) \033[94mwindows payload")
               print ("\033[91m(6) \033[94mandroid payload")
               print ("\033[91m(7) \033[94mlinux payload")
               print ("\033[91m(8) \033[94mmac payload")
               lol = raw_input("\033[91mprotocol ==> ")
               if lol == "1" or lol == "01":
                   make_pylaod()
               elif lol == "2" or lol == "02":
                   python_payload()
               elif lol == "3" or lol == "03":
                   perl_payload()
               elif lol == "4" or lol == "03":
                   bash_payload()
               elif lol == "5" or lol == "03":
                   windows_payload()
               elif lol == "6" or lol == "03":
                   android_payload()
               elif lol == "7" or lol == "03":
                   linux_payload()
               elif lol == "8" or lol == "03":
                   mac_payload()  
           elif vun == "2" or vun == "02":
               start_hacking()
           elif vun == "3" or vun == "03":
               scan_ip()
           elif vun == "4" or vun == "04":    
               print ("\033[91m(1) \033[94mfirst exploit")
               print ("\033[91m(2) \033[94msecond exploit")
               print ("\033[91m(3) \033[94mthird exploit")
               tol = raw_input("\033[91mprotocol ==> ")
               if tol == "1" or tol == "01":
                   link_hack()
               elif tol == "2" or tol == "02":
                   link_hack2()
               elif tol == "3" or tol == "03":
                   link_hack3()
               elif tol == "100":
                   restart_program()
                   
           elif vun == "*":
               restart_program()
   
           elif tool == "10":
               remove()
               sys.exit()
           
if __name__ == "__main__":
        main()

