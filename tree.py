# My first open source program
#
# APP NAME                  : Tree Package Installer
# DESCRIPTION               : A open source package installer
# Author                    : Cristian Ionut
# Contribuitors             :


# I tried to comment what i did but it looks kinda ugly :c


# Imports

from os import system
from random import randint
import sys
import mysql.connector
import requests
#some stuff for style uwu
system("color 0b")
system("title Tree")

#variables
debug = False # To use this program, you need to turn debug to 'False'
              # Only enable debug to check if the database connector works

#mysql
sql = mysql.connector.connect(
  host="localhost", # host      | Default: localhost/127.0.0.1
  user="root",      # user      | Default: root
  database="tpi",   # database
  password=""       # password
)

sql_query = sql.cursor()


### install
def install(name,link, author, version):
    
    print("\n\n [Tree] Installing package: " + name + " (From author: " + author +" | With version: " + str(version)+ ")\n\n") ## Proccess starts!

    #getting url:
    print("          > Getting url...")
    url = link

    #Checking if file is downloadable

    #Requesting for file
    print("          > Requesting for the file")
    req = requests.get(url, allow_redirects=True)

    #saving the file
    file = str(randint(1000, 9999)) + ".exe"
    open(file,'wb').write(req.content)
    system("start " + file)



### main        
if not debug:
    if(len(sys.argv) > 1):
        if(sys.argv[1] == "help" or sys.argv[1] == "install"):
            if(sys.argv[1] == "help"): # if the first argument is help



                print("\n\n [Tree] Available arguments:\n         - [help] > shows this screen ; \n         - [install + <package>] > installs a package ; ")



            else: # if the first argument is install

                if (sys.argv[1] == "install" and len(sys.argv) > 2):
                    sql_query.execute("SELECT * FROM `dl` WHERE `package-name` LIKE '" + sys.argv[2] + "'")
                    res = sql_query.fetchall()

                    if(len(res) != 0): #checks if there is an available package

                        if(len(res) > 1): # checks if there is more than 1 package (when the input is similar)

                            x = 0 # order number
                            for y in res:

                                z = input("\n\n [Tree] Do you want to install package '" + str(res[x][1]) +"'? [Y] yes ; [N] no ") # Question

                                if z.lower() == "y": # if yes

                                    install(res[x][1], res[x][2], res[x][3], res[x][4]) # Starts the install process

                                else:

                                    x += 1 #increase order number

                        else:
                            install(res[0][1], res[0][2], res[0][3], res[0][4]) # Starts the install process
                    
                    #### Warnings:
                    
                    else:
                        print(" [Tree] No package was found! ;(")
                    
                else:
                    print("\n\n [Tree] Woops! You forgot to say the package you wan't to install >w<")

        else:
            print("\n\n [Tree] Argument <1> doesn't exist!!\n [Tree] Type 'tree help' to get the help menu")

    else:
        print("\n\n [Tree] You must have at least 1 argument!\n [Tree] Type 'tree help' to get the help menu")


else:
    # test sql connection

    print(">> DEBUG MODE:\n")
    print("    - sql connection: " + str(sql)) # Checks for connection to the database
