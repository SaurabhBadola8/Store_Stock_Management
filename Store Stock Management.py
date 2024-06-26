from tkinter import *
from pymysql import *
from tkinter import messagebox as msg
from stock2 import cdata
class stock(Frame):
    def __init__(self,master):
        super().__init__(master)

        self.l0= Label(self,text="ONE MALL",fg="black",font=("Times new roman", 30, 'bold'))
        self.l0.grid(columnspan=6)
        
        self.l1=Label(self,text='Enter Item',bg='light blue',fg='black',font=('Arial',25))
        self.l2=Label(self,text='Enter Price',bg='light blue',fg='black',font=('Arial',25))
        self.l3=Label(self,text='Enter Quantity',bg='light blue',fg='black',font=('Arial',25))
        self.l4=Label(self,text='Enter DISCPUNT',bg='light blue',fg='black',font=('Arial',25))
        self.l5=Label(self,text='Enter CATEGORY',bg='light blue',fg='black',font=('Arial',25))

        self.t1=Entry(self,bg='light blue',fg='black',font=('Arial',16),bd=6,insertwidth=4,justify='center')
        self.t2=Entry(self,bg='light blue',fg='black',font=('Arial',16),bd=6,insertwidth=4,justify='center')
        self.t3=Entry(self,bg='light blue',fg='black',font=('Arial',16),bd=6,insertwidth=4,justify='center')
        self.t4=Entry(self,bg='light blue',fg='black',font=('Arial',16),bd=6,insertwidth=4,justify='center')
        self.t5=Entry(self,bg='light blue',fg='black',font=('Arial',16),bd=6,insertwidth=4,justify='center')
        self.t6=Entry(self,bg='blue',fg='white',font=('Arial',16),bd=6,insertwidth=4,justify='center')

        self.b1=Button(self,text='ADD ITEM',bg='green',fg='black',font=('Arial',16),bd=6,justify='center',command=self.add)
        self.b2=Button(self,text='DELETE ITEM',bg='maroon',fg='white',font=('Arial',16),bd=6,justify='center',command=self.dele)
        self.b3=Button(self,text='SEARCH ITEM',bg='blue',fg='white',font=('Arial',16),bd=6,justify='center',command=self.search)
        self.b4=Button(self,text='ALL ITEM',bg='green',fg='white',font=('Arial',18,"bold"),bd=6,justify='center',command=self.display)
        self.b6=Button(self,text='UPDATE ITEM',bg='limegreen',fg='white',font=('Arial',16),bd=6,justify='center',command=self.modify)
        self.b6['state']=DISABLED
        self.b5=Button(self,text='EXIT',bg='red',fg='black',font=('Arial',16),bd=6,justify='center',command=self.close)
        
        self.b1.grid(row=6,column=1)
        self.b2.grid(row=6,column=0)
        self.b3.grid(row=2,column=3)
        self.b6.grid(row=3,column=3)
        self.b5.grid(row=6,column=3)
        self.b4.grid(row=4,column=3)
                
        self.rowconfigure(index=0,pad=10)
        self.rowconfigure(index=1,pad=10)
        self.rowconfigure(index=2,pad=10)
        self.rowconfigure(index=3,pad=10)
        self.rowconfigure(index=4,pad=10)
        self.rowconfigure(index=5,pad=10)
        self.rowconfigure(index=5,pad=10)

        self.columnconfigure(index=0,pad=10)
        self.columnconfigure(index=1,pad=10)
        self.columnconfigure(index=2,pad=10)
     
        self.l1.grid(row=1,column=0)
        self.t1.grid(row=1,column=1)

        self.l2.grid(row=2,column=0)
        self.t2.grid(row=2,column=1)

        self.l3.grid(row=3,column=0)
        self.t3.grid(row=3,column=1)

        self.l4.grid(row=4,column=0)
        self.t4.grid(row=4,column=1)

        self.l5.grid(row=5,column=0)
        self.t5.grid(row=5,column=1)

        self.t6.grid(row=1,column=3)

        self.pack()

    def add(self):
        con=connect(db='badola',user='root',password='system',host='localhost')
        cur=con.cursor()
        iname=self.t1.get()
        price=float(self.t2.get())
        quan=int(self.t3.get())
        dis=int(self.t4.get())
        cat=self.t5.get()

        i=cur.execute("insert into stock values('%s',%d,%d,%d,'%s')"%(iname,price,quan,dis,cat))
        if(i==1):
            msg.showinfo('Save Information','Record Saved')
            con.commit()
            self.t1.delete(0,'end')
            self.t2.delete(0,'end')
            self.t3.delete(0,'end')
            self.t4.delete(0,'end')
            self.t5.delete(0,'end')
            self.t1.focus()
        else:
            print('error')

    def dele(self):
        con=connect(db='badola',user='root',password='root',host='localhost')
        cur=con.cursor()
        iname=self.t1.get()
        i=cur.execute("delete from stock where item='%s'"%(iname))
        if(i==1):
            msg.showinfo('Delete','Record Deleted')
            con.commit()
            self.t1.delete(0,'end')
        else:
            msg.showerror('Error Box','Record Not Found')
        
    def search(self):
        con=connect(db='badola',user='root',password='system',host='localhost')
        cur=con.cursor()
        iname=self.t6.get()
        cur.execute("select * from stock where item='%s'"%(iname))
        data=cur.fetchone()
        if(len(data)>0):
            self.t1.insert(0,data[0])
            self.t2.insert(0,data[1])
            self.t3.insert(0,data[2])
            self.t4.insert(0,data[3])
            self.t5.insert(0,data[4])
            self.b6['state']=NORMAL
        else:
            msg.showerror('Error Box','Record Not Found')
    
    def display(self):
        root1=Tk()
        ob=cdata(root1)
        root1.title("All stock Record")
        root1.geometry("450x600")
        root.mainloop()
    
    def close(self):
        exit()

    def modify(self):
        con=connect(db='badola',user='root',password='system',host='localhost')
        cur=con.cursor()
        iname=self.t1.get()
        price=int(self.t2.get())
        quan=int(self.t3.get())
        dis=int(self.t4.get())
        cat=self.t5.get()
        i=cur.execute("update stock set price=%d,quantity=%d,discount=%d,category='%s' where item='%s'"%(price,quan,dis,cat,iname))
        if(i==1):
            con.commit()
            msg.showinfo('Update Information','Record Updated')
        else:
            msg.showerror('Error Box','Record Not Found')
        self.t1.delete(0,'end')
        self.t2.delete(0,'end')
        self.t3.delete(0,'end')
        self.t4.delete(0,'end')
        self.t5.delete(0,'end')
        self.t1.focus()

root=Tk()
ob=stock(root)
root.title("ONE MALL")
root.state("zoomed")
root.mainloop()
