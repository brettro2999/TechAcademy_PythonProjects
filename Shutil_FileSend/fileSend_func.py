

import shutil
import os
from datetime import datetime, timedelta
from threading import Timer
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import sqlite3
import fileSend_shutil
import fileSend_gui





#select sending folder
def browseSource(self):
    path = filedialog.askdirectory()
    print (self.txt_browseSource.insert(INSERT, path))


#select receiving folder
def browseDest(self):
    path = filedialog.askdirectory()
    print (self.txt_browseDest.insert(INSERT, path))



#send files if modified within the last 24 hours
def SendFiles(self):
    source = self.txt_browseSource.get()
    files = os.listdir(source)
    destination = self.txt_browseDest.get()

    for i in files:


        modDate = datetime.fromtimestamp(os.path.getmtime(source))
        date = datetime.today()

        dayMark = modDate + timedelta(days = 1)

        
        if i.endswith(".txt") and dayMark > date:
            absPath = os.path.join(source, i)
            time = os.path.getmtime(absPath)
            print(i, time)
            shutil.copy(absPath, destination)
            print(destination)

            
            

            conn = sqlite3.connect('fileSend.db')
            with conn:
                cur = conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
                    ID INTEGER PRIMARY KEY, \
                    col_fileName TEXT,\
                    col_date TEXT\
                    )")
                conn.commit()
            conn.close()


            conn = sqlite3.connect('fileSend.db')
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_files(col_fileName, col_date) VALUES (?,?)", \
                [files, time])
                
            conn.close()




#midnight auto send

def AutoSend():
    x = datetime.today()
    y = x.replace(day=x.day, hour=0, minute=0, second=1, microsecond=0) + timedelta(days=1)
    delta_t=y-x

    secs=delta_t.total_seconds()


    t = Timer(secs, SendFiles)
    t.start()













if __name__ == "__main__":
    pass
