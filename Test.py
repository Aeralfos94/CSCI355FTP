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
    new.title('Main GUI')

    mainframe = ttk.Frame(new, padding='3 3 12 12')
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    menubar = Menu(new)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Login", command=lambda: showLoginWin(new))
    filemenu.entryconfig(0, state=DISABLED)
    filemenu.add_command(label="Disconnect", command=lambda: logout(filemenu))
    menubar.add_cascade(label="File", menu=filemenu)

<<<<<<< HEAD
    connectmenu = Menu(menubar, tearoff=0)
    connectmenu.add_command(label="Login", command=lambda: showLoginWin(new))
    connectmenu.entryconfig(0, state=DISABLED)
    connectmenu.add_command(label="Disconnect", command=lambda: logout(connectmenu))

    menubar.add_cascade(label="Connect", menu=connectmenu)

<<<<<<< HEAD
=======
<<<<<<< HEAD
# Gives server_entry the blinking cursor
server_entry.focus()
# Binds the "Enter" key to the login method
root.bind('<Return>', login)
>>>>>>> origin/master
=======
=======
>>>>>>> parent of aae2062... Added File in the menu
>>>>>>> origin/master
    new.config(menu=menubar)

def showLoginWin(new):
    new.destroy()
    root.deiconify()

def logout(filemenu):
    ftp.quit()
    if filemenu.entrycget(1, "state")=="normal":
        filemenu.entryconfig(1, state=DISABLED)
        filemenu.entryconfig(0, state=NORMAL)
    else:
        filemenu.entryconfig(1, state=NORMAL)
        filemenu.entryconfig(0, state=DISABLED)


root = Tk()
winLogin()
