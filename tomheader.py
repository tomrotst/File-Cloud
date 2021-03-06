#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Apr 21, 2020 12:46:14 PM +0300  platform: Windows NT


try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

import tomupload
import tomdownload
from os import path
import config
import os
import peer
import socket
import tomheader_support

# Vars
value = []
HOST = config.HOST
port = config.PORT
w = None

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

first_time = False
PASSED_FILE = ""


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    newpath = "files"
    # Create library path
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    root = tk.Tk()
    top = Toplevel1(root)
    root.resizable(width=False, height=False)
    tomheader_support.init(root, top)
    root.mainloop()


def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    tomheader_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


def keep_alive():
    while True:
        update_root()


def update_root():
    global val, w, root
    try:
        root.update()
    except:
        return
    root.update()


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x337+370+153")
        top.minsize(120, 1)
        top.maxsize(1364, 749)
        top.resizable(1, 1)
        top.title("Filecloud")
        top.configure(background="#0A3252")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.117, rely=0.0, height=71, width=454)
        self.Label1.configure(activebackground="#2d3436")
        self.Label1.configure(activeforeground="white")
        self.Label1.configure(activeforeground="#2d3436")
        self.Label1.configure(background="#0A3252")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Bahnschrift Light} -size 48")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Filecloud''')

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.583, rely=0.55, height=54, width=187)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#EA9A19")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Yu Gothic UI Semibold} -size 22 -weight bold")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(overrelief="flat")
        self.Button1.configure(pady="0")
        self.Button1.configure(relief="flat")
        self.Button1.configure(text='''DOWNLOAD''')
        self.Button1.configure(command=launch_download)

        self.Button1_1 = tk.Button(top)
        self.Button1_1.place(relx=0.1, rely=0.55, height=54, width=187)
        self.Button1_1.configure(activebackground="#ececec")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#34D03C")
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(font="-family {Verdana} -size 24")
        self.Button1_1.configure(foreground="#ffffff")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(overrelief="flat")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(relief="flat")
        self.Button1_1.configure(text='''UPLOAD''')
        self.Button1_1.configure(command=launch_upload)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.13, rely=0.236, height=31, width=434)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#0A3252")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {System} -size 10 -weight bold")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Welcome to Filecloud!''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label2_1 = tk.Label(top)
        self.Label2_1.place(relx=0.533, rely=0.74, height=21, width=244)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(background="#0A3252")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font="-family {System} -size 10 -weight bold")
        self.Label2_1.configure(foreground="#ffffff")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''Download a file from the server''')

        self.Label2_2 = tk.Label(top)
        self.Label2_2.place(relx=0.05, rely=0.74, height=21, width=244)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(background="#0A3252")
        self.Label2_2.configure(disabledforeground="#a3a3a3")
        self.Label2_2.configure(font="-family {System} -size 10 -weight bold")
        self.Label2_2.configure(foreground="#ffffff")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(text='''Upload a local file to the cloud''')

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.233, rely=0.861, height=44, width=317)
        self.Button2.configure(activebackground="#6c6c6c")
        self.Button2.configure(activeforeground="white")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#0a3252")
        self.Button2.configure(disabledforeground="#0a3252")
        self.Button2.configure(font="-family {Arial} -size 14")
        self.Button2.configure(foreground="#ffffff")
        self.Button2.configure(highlightbackground="#0a3252")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(relief="flat")
        self.Button2.configure(text='''BROWSE DOWNLOAD LIBRARY''')
        self.Button2.configure(command=launch_explorer)

    def update_output(self, output, colour):
        self.Label2.configure(text=output)
        self.Label2.configure(foreground=colour)
        update_root()


def launch_explorer():
    os.startfile("files")


def launch_upload():
    global first_time
    root.withdraw()
    # Start upload window gui and receive the user selection
    file_path = tomupload.vp_start_gui(first_time)
    try:
        file_path = file_path.replace("/", "\\")
    except:
        file_path = ''
    if first_time:
        first_time = False
    root.deiconify()
    print("GOT FILE PATH " + file_path)
    if not path.exists(file_path):
        tomheader_support.update_feedback('The file does not exist', '#D5212E')
        return
    else:
        tomheader_support.update_feedback('The selected file is being uploaded', '#34d03c')
    # Start uploading
    server_manage_upload(file_path)


def launch_download():
    global first_time
    global PASSED_FILE
    root.withdraw()
    try:
        # Start second gui window and get the selection back
        PASSED_FILE, s = tomdownload.vp_start_gui(first_time)
    except:
        return
    if first_time:
        first_time = False
    root.deiconify()
    # Letting tomdownload know file has been passed to this program
    tomdownload.has_files_been_passed = False
    if first_time:
        first_time = False
    if PASSED_FILE != "empty":
        # If file is valid start download
        print("GOT FILE SELECTED " + PASSED_FILE)
        tomheader_support.update_feedback(PASSED_FILE + ' is being downloaded', '#34d03c')
        peer.new_download(s, PASSED_FILE)
        PASSED_FILE = ""
    else:
        # If no files in the cloud right now
        s.close()
        tomheader_support.update_feedback('no files uploaded yet', '#34d03c')
        PASSED_FILE = ""


def server_manage_upload(f_path):
    # Establishing connection before starting the server
    s = socket.socket()
    try:
        s.connect((HOST, port))
    except:
        print("connection aborted")
        exit()
    peer.main_new(s, 'u', f_path)


def server_manage_download(w_file):
    return


if __name__ == '__main__':
    vp_start_gui()





