import os
import platform
import dropbox


cwd = os.getcwd()
system = platform.system()


# Colors for text
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# -------------------------------------------------FUNCTION APART----------------------------------------------------------


def selec_path(give_path):

    if give_path == " ":

        return cwd


def download_files():

    print(bcolors.WARNING + "From the next options what is your Cloud"+bcolors.ENDC)
    print("1)"+bcolors.FAIL + " Mega.nz" + bcolors.ENDC)
    print("2)"+bcolors.OKGREEN+" Goo" + bcolors.ENDC + bcolors.WARNING +
          "gle Dr"+bcolors.ENDC+bcolors.OKCYAN+"ive"+bcolors.ENDC)
    print("3)" + bcolors.OKBLUE + " DropBox"+bcolors.ENDC)

    cloud_selected = input(cwd+"> ")
    second_loop = True

    while second_loop == True:

        if cloud_selected == "1":
            print("Mega")

            second_loop = False
        elif cloud_selected == "2":
            print("Google Drive")
            second_loop = False
        elif cloud_selected == "3":
            print("DropBox")
            second_loop = False
        else:
            cloud_selected = input(
                bcolors.WARNING+"You should select one of the given clouds \n"+bcolors.ENDC)
            second_loop = True


def fix_files():

    print(cwd)


# ---------------------------------------------END FUNCTION APART----------------------------------------------------------


print(bcolors.WARNING+"Please select the action that you wish to do \n" + bcolors.ENDC +
      "1) Dowload files from some clouds (You need the Link(s)) \n2) Change the name from all files to (Season)x(Chapter)")

serieName = input(
    bcolors.WARNING+"Select one from the options above \n"+bcolors.ENDC + cwd + "> ")

loop = True

while loop == True:

    if serieName == "1":

        download_files()
        loop = False

    elif serieName == "2":

        fix_files()
        loop = False

    else:
        serieName = input("You shuold select one of the options \n")
        loop = True
