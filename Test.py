__author__ = 'Dave Schreck'

import tkinter
from ftplib import FTP
from tkinter import *
from tkinter import ttk

def login(*args):
    try:
        ftp = FTP(server.get())
        ftp.login(username.get(), password.get())
        print(ftp.getwelcome())
    except ValueError:
        pass

root = Tk()
root.title("Login To Server")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

server = StringVar()
username = StringVar()
password = StringVar()

server_entry = ttk.Entry(mainframe, width=20, textvariable=server)
server_entry.grid(column=2, row=1, sticky=(W, E))

username_entry = ttk.Entry(mainframe, width=20, textvariable=username)
username_entry.grid(column=2, row=2, sticky=(W, E))

password_entry = ttk.Entry(mainframe, width=20, textvariable=password)
password_entry.grid(column=2, row=3, sticky=(W, E))

ttk.Label(mainframe, text="Server: ").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Username: ").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Password: ").grid(column=1, row=3, sticky=W)

ttk.Button(mainframe, text="Login", command=login).grid(column=2, row=4, sticky=(W, E))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

server_entry.focus()
root.bind('<Return>', login)

root.mainloop()
