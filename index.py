# Modules utils
import os


# My modules
from src.bcolors import bcolors
from src.download_files import DownloadFiles

cwd = os.getcwd()

def run():
    print(bcolors.WARNING+"Please select the action that you wish to do \n" + bcolors.ENDC +
      "1) Dowload files from some clouds (You need the Link(s)) \n2) Change the name from all files to (Season)x(Chapter)")
    anserwer = input(bcolors.WARNING+"Select one from the options above \n"+bcolors.ENDC + cwd + "> ")
    
    if anserwer == "1":
        download = DownloadFiles(cwd)
        download.print_clouds_options()
    
    if anserwer == "2":
        return 2
    
    if anserwer == "3":
        exit()
    
    else:
        return run()

# Incio de ejecucion
if __name__ == "__main__":
    run()

