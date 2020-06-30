

import shutil
import os
from datetime import datetime, timedelta
from threading import Timer
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import sqlite3
import fileSend_func
import fileSend_gui




class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        
        self.master = master
        self.master.minsize(610,180)
        self.master.maxsize(610,180)
        self.master.title("Simple File Send 24")
        self.master.configure(bg="lightgray")

        arg = self.master

        fileSend_gui.fileSendGUI(self)





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
