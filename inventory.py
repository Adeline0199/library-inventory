'''
Created on 19-Jul-2019

@author: user 6
'''
import mysql.connector
from tkinter import *
import tkinter
class database_application:
    def new_record(self):
        self.b_new['state']=DISABLED
        self.populate_blank()
    def save_record(self):
        catalogid=int(self.entry_catalogid.get())
        title=self.entry_title.get()
        author=self.entry_author.get()
        price=float(self.entry_price.get())
        if self.b_new['state']==DISABLED:
            sql="insert into library(catalogid,title,author,price) values('%d','%s','%s','%f')"%(catalogid,title,author,price)
        else:
            sql="update library set title='%s',author='%s',price='%f' where catalogid like '%d' "%(title,author,price,catalogid)
            
        try:
            self.cursor.execute(sql)
            self.db.commit()
            self.cursor.execute(sql)
            self.results=self.cursor.fetchall()
        except:
            self.db.rollback()
        self.b_new['state']=NORMAL
    
    
    def delete_record(self):
        catalogid=self.entry_catalogid.get()
        sql="delete from library where catalogid like '%d'"%catalogid
        try:
            self.cursor.execute(sql)
            self.db.commit()
            sql="select * from library"
            self.cursor.execute(sql)
            self.results=self.cursor.fetchall()
            self.populate_blank()
            self.previous_record()
        except:
            self.db.rollback()
            
    def exit_form(self):
        self.root.destroy()
        
        
    def first_record(self):
        if len(self.results)>0:
            self.current_record=0
            self.populate_record()
    def next_record(self):
        if len(self.results)>0:
            self.current_record+=1
            if self.current_record>=len(self.results):
                self.current_record=0
            self.populate_record()
            
            
    def previous_record(self):
        if len(self.results)>0:
            self.current_record-=1
            if self.current_record<0:
                self.current_record=len(self.results)-1
            self.populate_record()
            
    def last_record(self):
        if len(self.results)>0:
            self.current_record=len(self.results)-1
            self.populate_record()
        
        
            
            
             
                
    def __init__(self):
        self.root=Tk()
        self.root.title("Library records")
        self.root.geometry("225x270")
        catalogid=Label(self.root,text="CATALOG ID:",anchor=tkinter.E)
        self.entry_catalogid=Entry(self.root,bg="yellow")
        title=Label(self.root,text="TITLE:",anchor=tkinter.E)
        self.entry_title=Entry(self.root,bg="yellow")
        author=Label(self.root,text="AUTHOR:",anchor=tkinter.E)
        self.entry_author=Entry(self.root,bg="yellow")
        price=Label(self.root,text="PRICE:",anchor=tkinter.E)
        self.entry_price=Entry(self.root,bg="yellow")
        self.b_new=Button(self.root,text="New",command=self.new_record,bg="pink")
        b_save=Button(self.root,text="Save",command=self.save_record,bg="pink")
        b_delete=Button(self.root,text="Delete",command=self.delete_record,bg="pink")
        b_exit=Button(self.root,text="Exit",command=self.exit_form,bg="pink")
        b_first=Button(self.root,text="First",command=self.first_record,bg="pink")
        b_next=Button(self.root,text="Next",command=self.next_record,bg="pink")
        b_previous=Button(self.root,text="Prev",command=self.previous_record,bg="pink")
        b_last=Button(self.root,text="Last",command=self.last_record,bg="pink")
        catalogid.place(x=20,y=20,width=60,height=25)
        self.entry_catalogid.place(x=90,y=20,width=100,height=25)
        title.place(x=20,y=55,width=60,height=25)
        self.entry_title.place(x=90,y=55,width=100,height=25)
        author.place(x=20,y=90,width=60,height=25)
        self.entry_author.place(x=90,y=90,width=100,height=25)
        price.place(x=20,y=125,width=60,height=25)
        self.entry_price.place(x=90,y=125,width=100,height=25)
        self.b_new.place(x=20,y=195,width=40,height=25)
        b_save.place(x=70,y=195,width=40,height=25)
        b_delete.place(x=120,y=195,width=40,height=25)
        b_exit.place(x=170,y=195,width=40,height=25)
        
        b_first.place(x=20,y=230,width=40,height=25)
        b_next.place(x=70,y=230,width=40,height=25)
        b_previous.place(x=120,y=230,width=40,height=25)
        b_last.place(x=170,y=230,width=40,height=25)
        
        config={'user':'adeline','password':'mice','host':'localhost','database':'adelinefernandes','raise_on_warnings':True}
        self.db=mysql.connector.connect(**config)
        try:
            self.cursor=self.db.cursor()
            sql="Select * from library"
            self.cursor.execute(sql)
            self.results=self.cursor.fetchall()
            self.current_record=0
        except:
            print("error fetching data")
        self.first_record()
        self.root.mainloop()
        
    def populate_record(self):
        row=self.results[self.current_record]
        self.entry_catalogid.delete(0,END)
        self.entry_catalogid.insert(0,row[0])
        self.entry_title.delete(0,END)
        self.entry_title.insert(0,row[1])
        self.entry_author.delete(0,END)
        self.entry_author.insert(0,row[2])
        self.entry_price.delete(0,END)
        self.entry_price.insert(0,row[3])
        
        
    def  populate_blank(self):
        self.entry_catalogid.delete(0,END)
        self.entry_title.delete(0,END)
        self.entry_author.delete(0,END)
        self.entry_price.delete(0,END)
        
        
d=database_application()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
