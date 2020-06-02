
import sqlite3

conn = sqlite3.connect('list.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtFiles( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_name TEXT \
        )")
    conn.commit()
conn.close()



conn = sqlite3.connect('list.db')

with conn:
    cur = conn.cursor()
    fileList = ('information.docx','Hello.txt','myImage.png', \
                'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
    for tFile in fileList:
        if tFile.endswith(".txt"):
            cur.execute("INSERT INTO tbl_txtFiles(file_name) VALUES (?)", \
                        (tFile,))
    conn.commit()
conn.close()

conn = sqlite3.connect('list.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT file_name FROM tbl_txtFiles")
    files = cur.fetchall()
    print(files)
