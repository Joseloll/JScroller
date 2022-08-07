from pynput.mouse import Controller
import keyboard
import colorama
from colorama import Fore
import time
import os
import sys
os.system(f'cls & mode 85,20 & title JScroller')
def main():
   menu()



def menu():
   mouse = Controller()
   start = input(Fore.YELLOW + """
       _______                 ____         
      / / ___/______________  / / /__  _____
 __  / /\__ \/ ___/ ___/ __ \/ / / _ \/ ___/
/ /_/ /___/ / /__/ /  / /_/ / / /  __/ /    
\____//____/\___/_/   \____/_/_/\___/_/     
      
   
   Press Any Enter To Start JScroller""")
   print(Fore.GREEN + "There Will Be A 5 Second Delay Before Scrolling")
   time.sleep(5)
   print(Fore.LIGHTCYAN_EX + "Scrolling Was SucessFull")
   while(True):
      mouse.scroll(0,200000)
      exit = input(Fore.YELLOW + "Would You Like To Exit y/n:")
      if exit == "y":
          print(Fore.GREEN + "You Are Exiting Now Thank You For Using Jscroller")
          time.sleep(3)
          sys.exit()
      elif exit == "n":
            os.system('cls')
            menu()


main()
