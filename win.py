import os

def ver():
    print("Windows For Linux 1.0.0 , Created by Holia")

def xcopy(src, dird):
    os.system('cp --update ' + src + ' ' + dird + '')
    os.system("echo '\033[0;32m'All File has bein copied ! && echo '\033[1;37m'")

def cls():
    os.system("clear")

def cmddir():
    os.system("pwd")

def ext():
    os.system("echo '\033[0;36m'Shutdown")
    exit()

def cmd():
    cls()
    ver()

def cd(ssssss):
    os.system("cd " + ssssss)
    print("Dir : " + ssssss)

def set():
    os.system('set')