__author__ = 'Dave Schreck'

import tkinter
from ftplib import FTP
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def login(*args):
    if len(server.get()) != 0 and len(username.get()) != 0 and len(password.get()) != 0:
        ftp = FTP(server.get())
        ftp.login(username.get(), password.get())
        print(ftp.getwelcome())
    else:
        messagebox.showerror("Login Failed", "Incorrect login credentials.", )


#GUI CODE
root = Tk()
root.title("Login To Server")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Entry Field String Variables
server = StringVar()
username = StringVar()
password = StringVar()

# Sets up the input fields
server_entry = ttk.Entry(mainframe, width=20, textvariable=server)
server_entry.grid(column=2, row=1, sticky=(W, E))

username_entry = ttk.Entry(mainframe, width=20, textvariable=username)
username_entry.grid(column=2, row=2, sticky=(W, E))

password_entry = ttk.Entry(mainframe, width=20, textvariable=password)
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
