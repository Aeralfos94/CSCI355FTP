__author__ = 'Dave Schreck'

import tkinter
import ftplib
from ftplib import FTP
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def login(*args):
    if len(server.get()) != 0 and len(username.get()) != 0 and len(password.get()) != 0:
        try:
            global ftp
            ftp = FTP(server.get())
            ftp.login(username.get(), password.get())
            print(ftp.getwelcome())
            mainGUI()
        except ftplib.all_errors:
            messagebox.showerror("Login Failed", "Incorrect login credentials.")
    else:
         messagebox.showerror("Login Failed", "Make sure to enter in a server, username, and password.")


def winLogin():
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    root.title("Login To Server")

    # Entry Field String Variables
    global server
    global username
    global password

    server = StringVar()
    username = StringVar()
    password = StringVar()

    # Sets up the input fields
    server_entry = ttk.Entry(mainframe, width=20, textvariable=server)
    server_entry.grid(column=2, row=1, sticky=(W, E))
    server_entry.delete(0, 'end')

    username_entry = ttk.Entry(mainframe, width=20, textvariable=username)
    username_entry.grid(column=2, row=2, sticky=(W, E))

    password_entry = ttk.Entry(mainframe, width=20, show="*", textvariable=password)
    password_entry.grid(column=2, row=3, sticky=(W, E))

    # Sets up the Labels
    ttk.Label(mainframe, text="Server: ").grid(column=1, row=1, sticky=W)
    ttk.Label(mainframe, text="Username: ").grid(column=1, row=2, sticky=W)
    ttk.Label(mainframe, text="Password: ").grid(column=1, row=3, sticky=W)

    # Sets up the Login Button
    ttk.Button(mainframe, text="Login", command=login).grid(column=2, row=4, sticky=(W, E))

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    # Gives server_entry the blinking cursor
    server_entry.focus()
    # Binds the "Enter" key to the login method
    root.bind('<Return>', login)

    root.mainloop()


def mainGUI():
    root.withdraw()

    new = Toplevel()
    new.title(server.get())

    mainframe = ttk.Frame(new, padding='3 3 12 12')
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    menubar = Menu(new)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Add Directory", command=addDir)
    filemenu.add_command(label="Delete Directory", command=delDir)
    filemenu.add_command(label="Browse Files", command=browse)
    filemenu.add_command(label="Delete File", command=deleteFile)
    filemenu.add_command(label="Change File Permissions", command=changeFilePerm)
    filemenu.add_command(label="Upload", command=upload)
    filemenu.add_command(label="Download", command=download)
    filemenu.add_command(label="Real-time File Transfer", command=realTime)

    menubar.add_cascade(label="File", menu=filemenu)

    connectmenu = Menu(menubar, tearoff=0)
    connectmenu.add_command(label="Login", command=lambda: showLoginWin(new))
    connectmenu.entryconfig(0, state=DISABLED)
    connectmenu.add_command(label="Disconnect", command=lambda: logout(connectmenu))

    menubar.add_cascade(label="Connect", menu=connectmenu)

    new.config(menu=menubar)

def showLoginWin(new):
    new.destroy()
    root.deiconify()

def logout(connectmenu):
    ftp.quit()
    if connectmenu.entrycget(1, "state")=="normal":
        connectmenu.entryconfig(1, state=DISABLED)
        connectmenu.entryconfig(0, state=NORMAL)
    else:
        connectmenu.entryconfig(1, state=NORMAL)
        connectmenu.entryconfig(0, state=DISABLED)


def addDir():
    print("addDir")

def delDir():
    print("delDir")

def changeFilePerm():
    print("changeFilePerm")

def browse():
    print("browse")

def deleteFile():
    print("deleteFile")

def upload():
    print("upload")

def download():
    print("download")

def realTime():
    print("realTime")

def addDir():
    ftp.mkd("directory") #TODO: request user for input (type in dialogue box)

def delDir():
    ftp.rmd("directory") #TODO: request user for input (click from list?)

root = Tk()
winLogin()