import tkinter
from tkinter import filedialog
from tkinter import *
import os.path
import sqlite3
from sqlite3 import Error
import fileinput
import sys

globalSeed = 0
scrapMechanicDir = "\\Steam\\steamapps\\common\\Scrap Mechanic\\"

#Setup gui so every non-programmer can use this software
m=tkinter.Tk(screenName='ScrapMechanicSeedTool',  baseName='SMST',  className='smst',  useTk=1)

#set title
m.title('Scrap Mechanic Seed Tool by FX')

#Set output above so everyone can use it
output = Label(m, text="Ready")
output.grid(row=6,columnspan=3,sticky=NW,padx=6)

#My trustly sqlite functions
def connectDB(file):
    global output
    db = None
    try:
        db = sqlite3.connect(file)
    except Error as e:
        print(e)
        output.config(text=str(e))
    return db

#simple sqlite query to get seed
def getSeed(conn):
    global output
    seed = 0
    try:
        cur = conn.cursor()
        cur.execute("SELECT seed FROM Game")
        seed = cur.fetchone()[0]
        output.config(text="Seed was successfully extracted from save")
    except Error as e:
        print(e)
        output.config(text=str(e))
    finally:
        if (conn):
            conn.close()
    return seed
#simple sqlite query to set seed
def setSeed(conn):
    global output
    global globalSeed
    try:
        cur = conn.cursor()
        cur.execute("UPDATE Game set seed = "+str(globalSeed))
        conn.commit()
        cur.close()
        output.config(text="Seed was successfully injected into save")
    except Error as e:
        print(e)
        output.config(text=str(e))
    finally:
        if (conn):
            conn.close()

def getSaveFile():
    #Get save file location
    homedir = homedir = os.path.expanduser("~")
    savefileloc = homedir+"\\AppData\\Roaming\\Axolot Games\\Scrap Mechanic\\User\\"

    #Using scandir is the fastest method!
    listUsers = [f.path for f in os.scandir(savefileloc) if f.is_dir()]

    #If only one scrap mechanic user folder, we obv want to check the seed from that
    #user, plus we can bring the user directly to the save folder
    if len(listUsers) == 1:
        savefileloc = listUsers[0]+"\\Save\\Survival"

    #Setup a file dialog so that the user can choose the exact file they want to get the seed from
    return filedialog.askopenfilename(initialdir = savefileloc,title = "Select file",filetypes = (("sm save files","*.db"),))

def extractSeed():
    global globalSeed
    #Execute sqlite to obtain seed from file
    globalSeed = getSeed(connectDB(getSaveFile()))
    curSeed.config(text=str(globalSeed))

def injectSeed():
    #Execute sqlite to obtain seed from file
    setSeed(connectDB(getSaveFile()))

def fileSeedMod(default,file):
    global output
    global globalSeed
    if os.path.isfile(file):
        for line in fileinput.input(file, inplace = 1):
            if "--[TAG]" in line or "852772513" in line:
                if default:
                    sys.stdout.write("	--seed = "+str(globalSeed)+" --[TAG]\n")
                    output.config(text="World gen was reset to default state")
                else:
                    sys.stdout.write("	seed = "+str(globalSeed)+" --[TAG]\n")
                    output.config(text="World gen will now use '"+str(globalSeed)+"' as its seed")
            else:
                sys.stdout.write(line)

def constDefSeed(default):
    global scrapMechanicDir
    if os.path.isdir(os.environ["ProgramFiles"]+"\\Steam\\") and os.path.isdir(os.environ["ProgramFiles"]+scrapMechanicDir):
        file = os.environ["ProgramFiles"]+scrapMechanicDir+"Survival\\Scripts\\game\\terrain\\terrain_overworld.lua"
        fileSeedMod(default,file)
    elif os.path.isdir(os.environ["ProgramFiles(x86)"]+"\\Steam\\") and os.path.isdir(os.environ["ProgramFiles(x86)"]+scrapMechanicDir):
        file = os.environ["ProgramFiles(x86)"]+scrapMechanicDir+"Survival\\Scripts\\game\\terrain\\terrain_overworld.lua"
        fileSeedMod(default,file)

def constSeed():
    constDefSeed(False)

def defaultSeed():
    constDefSeed(True)

#Create label which specific current seed being used
Label(m, text='Current Seed: ').grid(row=0,column=0,padx=6, pady=5)
curSeed = Label(m, text=str(globalSeed))
curSeed.grid(row=0,column=1,padx=6, pady=5)

#Entry where user enters new seed
Label(m, text='Seed to use:').grid(row=1,padx=2)

#Add textbox for new seed
useSeed = Entry(m)
useSeed.grid(row=1, column=1,padx=2)

#Set the seed from the entry value
def setGlobalSeed():
    global output
    global globalSeed
    globalSeed = useSeed.get()
    curSeed.config(text=str(globalSeed))
    output.config(text="Current Seed set to: "+str(globalSeed))

#Set seed button
E = Button(m, text ="Set seed", command = setGlobalSeed)
E.grid(row=1, column=2, padx=6)

#Add a line break
Frame(m).grid(row=2, columnspan=3,pady=10)

Menu = Frame(m)
Menu.grid(row=3, columnspan=3)
B = Button(Menu, text ="Extract seed from save file", command = extractSeed)
B.pack()
C = Button(Menu, text ="Inject seed into save file", command = injectSeed)
C.pack()
D = Button(Menu, text ="Modify world gen seed to be constant", command = constSeed)
D.pack()
E = Button(Menu, text ="Reset world gen to default", command = defaultSeed)
E.pack()

#Add a line break
Frame(m).grid(row=4, columnspan=3,pady=10)


Label(m, text='Output: ').grid(row=5,columnspan=3,sticky=NW,padx=6)

m.mainloop()
