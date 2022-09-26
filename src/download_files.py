from Media_Tool_By_Terminal import selec_path
from src.bcolors import bcolors

class DownloadFiles():
    
    def __init__(self, cwd):
        self.cwd = cwd 

    def print_clouds_options(self):
        print(bcolors.WARNING + "From the next options what is your Cloud"+bcolors.ENDC)
        print("1)"+bcolors.FAIL + " Mega.nz" + bcolors.ENDC)
        print("2)"+bcolors.OKGREEN+" Goo" + bcolors.ENDC + bcolors.WARNING +
            "gle Dr"+bcolors.ENDC+bcolors.OKCYAN+"ive"+bcolors.ENDC)
        print("3)" + bcolors.OKBLUE + " DropBox"+bcolors.ENDC)
        return self.cloud_selection()

    def cloud_selection(self):
        
        cloud_selected = input(self.cwd + "> ")
        
        if cloud_selected == "1":
            return self.cloud_mega()
        if cloud_selected == "2":
            return self.cloud_google_drive()
        if cloud_selected == "3":
            return self.cloud_dropbox()
        else:
            print(bcolors.WARNING+"You should select one of the given clouds \n"+bcolors.ENDC)
            cloud_selected(self)

    
    def cloud_mega(self):
        print("Mega")
    
    def cloud_google_drive(self):
        print("Google Drive")
    
    def cloud_dropbox(self):
        print("DropBox")
