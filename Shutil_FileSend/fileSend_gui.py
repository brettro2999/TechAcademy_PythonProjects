

import shutil
import os
from datetime import datetime, timedelta
from threading import Timer
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import sqlite3
import fileSend_shutil
import fileSend_func



def fileSendGUI(self):



    self.labelOne = tk.Label(self.master, bg="lightgray", text="Send all files modified within the last day:")
    self.labelOne.grid(column=0, row=0, sticky=N+W)
    
    self.txt_browseSource = tk.Entry(self.master, text='', width=75)
    self.txt_browseSource.grid(row=1, column=1, rowspan=1, columnspan=1, padx=(30,40), pady=(40,0), sticky=N+W)
    self.txt_browseDest = tk.Entry(self.master, text='', width=75)
    self.txt_browseDest.grid(row=2, column=1, rowspan=1, columnspan=1, padx=(30,40), pady=(0,0), sticky=N+W)

    self.btn_brws = tk.Button(self.master, width=20, height=1, text='Browse Sending Folder:', command = fileSend_func.browseSource(self))
    self.btn_brws.grid(row=1, column=0, padx=(5,0), pady=(40,0), sticky=W)
    self.btn_brws = tk.Button(self.master, width=20, height=1, text='Browse Receiving Folder:', command = lambda:fileSend_func.browseDest(self))
    self.btn_brws.grid(row=2,column=0,padx=(5,0),pady=(5,0),sticky=W)
    self.btn_run = tk.Button(self.master,width=16,height=2,text='Run', command = lambda:fileSend_func.SendFiles(self))
    self.btn_run.grid(row=3,column=1,padx=(5,0),pady=(5,0),sticky=W)




if __name__ == "__main__":
    pass
