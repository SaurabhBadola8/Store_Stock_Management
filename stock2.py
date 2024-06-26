from tkinter import *
from pymysql import *
from tkinter import messagebox as msg
class cdata(Frame):
    def __init__(self,master):
        super().__init__(master)
       
        self.ta=Text(self)
        self.ta.grid(row=0,column=0)
       
        con=connect(db='badola',user='root',password='root',host='localhost')
        cur=con.cursor()
        cur.execute("select * from stock")
        data=cur.fetchall()
        txt=""
        for xdata in data:
            for x in xdata:
                txt+=str(x)+"\t"
            txt+="\n"
        self.ta.insert(END,txt)
        self.pack()
