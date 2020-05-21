from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from cx_Oracle import *
import socket
import requests
import matplotlib.pyplot as plt
import bs4
import sys
import tkinter as tk
 




def f1():
	root.withdraw()
	adst.deiconify()
def f2():
	adst.withdraw()
	root.deiconify()
def f4():
	vist.withdraw()
	root.deiconify()
def f3():
	stdata.delete(1.0,END)
	root.withdraw()
	vist.deiconify()
	con=None
	try:
		con=connect("system/abc123")
		cursor=con.cursor()
		sql="select rno,name,marks from students"
		cursor.execute(sql)
		data=cursor.fetchall()
		msg=""
		for d in data:
			msg=msg+"rno="+str(d[0])+ "name="+str(d[1])+ "marks="+str(d[2])+"\n"
		stdata.insert(INSERT,msg)
		
	except DatabaseError as e:
		messagebox.showerror("IT's WRONG",e)
	finally:
		if con is not None:
			con.close()
def f5():
	con=None
	cursor=None
	try:
		con=connect("system/abc123")
		rno=entAddRno.get()
		name=entAddName.get()
		Marks=entAddMarks.get()
		rno1=int(rno)
		marks1=int(Marks)
		try:
			if rno.isalpha()==True:
				con.rollback()
				entAddRno.delete(0,END)
				entAddRno.focus()
		except ValueError:
			con.rollback()
			messagebox.showerror("Error","Roll no should be integer")
		try:
			if rno1<0:
				con.rollback()
				entAddRno.delete(0,END)
				entAddRno.focus()
		except ValueError:
			con.rollback()
			messagebox.showerror("Error","Roll no should be positive")
		try:
			if name.isalpha()==False:
				con.rollback()
				entAddName.delete(0,END)
				entAddName.focus()
		except ValueError:
			con.rollback()
			messagebox.showerror("Error","Name should be alphabets")
		try:
			if Marks.isalpha()==True:
				con.rollback()
				entAddMarks.delete(0,END)
				entAddMarks.focus()
		except ValueError:
			con.rollback()
			messagebox.showerror("Error","Marks should be integer")
		try:
			if marks1>100 or marks1<0:
				con.rollback()
				entAddMarks.delete(0,END)
				entAddMarks.focus()
		except ValueError:
			con.rollback()
			messagebox.showerror("Error","Marks should be between 0 and 100")
		else:
			cursor=con.cursor()
			sql="insert into students values('%d','%s','%d')"
			args=(rno1,name,marks1)
			cursor.execute(sql%args)
			con.commit()
			msg= str(cursor.rowcount)+"record inserted"
			messagebox.showinfo("GOOD JOB", msg)
		
		
	except DatabaseError:
		con.rollback()
		messagebox.showerror("IT's WRONG","Roll no already exist")
		entAddRno.delete(0,END)
		entAddName.delete(0,END)
		entAddMarks.delete(0,END)
		entAddRno.focus()
		entAddName.focus()
		entAddMarks.focus()
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
def f7():
	root.withdraw()
	upst.deiconify()

def f8():
	con=None
	cursor=None
	try:
		con=connect("system/abc123")
		rno=entUpdateRno.get()
		name=entUpdateName.get()
		marks=entUpdateMarks.get()
		rno1=int(rno)
		marks1=int(marks)
		
		
		if rno.isalpha()==True:
			con.rollback()
			messagebox.showerror("Error","Roll no should be integer")
			entAddRno.delete(0,END)
			entAddRno.focus()
		elif rno1<0:
			con.rollback()
			messagebox.showerror("Error","Roll no should be greater than 0")
			entAddRno.delete(0,END)
			entAddRno.focus()		
		elif name.isalpha()==False:
			messagebox.showerror("Error","Name should be only alphabets")
			con.rollback()
			entAddName.delete(0,END)
			entAddName.focus()
		elif marks.isalpha()==True:
			messagebox.showerror("Error","Marks should be only integer")
			con.rollback()
			entAddMarks.delete(0,END)
			entAddMarks.focus()
		elif marks1>100 or marks1<0:
			messagebox.showerror("Error","Marks should be between 0 and 100")
			con.rollback()
			entAddMarks.delete(0,END)
			entAddMarks.focus()
		else:
			cursor=con.cursor()
			sql="update students set NAME='%s',MARKS='%d' where RNO='%d'"
			data=(name,marks1,rno1)
			cursor.execute(sql %data)
			con.commit()		
			msg=str(cursor.rowcount)+" record updated "
			if cursor.rowcount==0:
				messagebox.showerror("ERROR!!!","Roll no not present in Database")
			else:
				messagebox.showinfo("GOOD JOB", msg)
				entUpdateRno.delete(0,END)
				entUpdateRname.delete(0,END)
				entUpdateMarks.delete(0,END)
				entUpdateRno.focus()
				
	except ValueError:
		messagebox.showerror("Error","Roll or Marks Should be an integer")
	except DatabaseError as e:
		con.rollback
		messagebox.showerror("GADBAD HAI",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
def f9():
	upst.withdraw()
	root.deiconify()
def f10():
	con=None
	cursor=None
	try:
		con=connect("system/abc123")
		rno=int(entDeleteRno.get())
		cursor=con.cursor()
		sql="delete from students where RNO=%d"
		cursor.execute(sql %rno)
		con.commit()
		if cursor.rowcount==0:
			messagebox.showwarning("Error","Try another roll no, it does not exists")
		else:		
			msg=str(cursor.rowcount)+" record deleted "
			messagebox.showinfo("Bohot Hard HAI",msg)
	except ValueError:
		messagebox.showerror("Error","Roll or Marks Should be an integer")
	except DatabaseError as e:
		con.rollback
		messagebox.showerror("GADBAD HAI",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
def f11():
	root.withdraw()
	dest.deiconify()
def f12():
	dest.withdraw()
	root.deiconify()
	msg=''
	entDeleteRno.delete(0,END)
def f13():
	con=None
	cursor=None
	try:
		import numpy as np
		import pandas as pd
		
		con=connect("system/abc123")
		cursor=con.cursor()
		sql = "SELECT NAME FROM(SELECT NAME FROM students ORDER BY Marks DESC)WHERE ROWNUM<6"
		
		cursor.execute(sql)
		x = cursor.fetchall()
		

		sql1 = "SELECT MARKS FROM(SELECT MARKS FROM students ORDER BY Marks DESC)WHERE ROWNUM<6"
		
		cursor.execute(sql1)
		y = cursor.fetchall()
		
		
		x1=list(zip(*x))[0]
		y1=list(zip(*y))[0]
		sql=np.arange(len(x))
		plt.bar(x1,y1,width=0.5,label='Name',color='blue')
		
		plt.xticks(x1,fontsize=10)
		plt.title(' Exam Score')
		plt.xlabel('Students',fontsize=10)

		plt.ylabel('Marks',fontsize=10)
		plt.grid()
		plt.show()

	except DatabaseError as e:
		con.rollback
		messagebox.showerror("Error!!!!",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()

	

def f14():
	gst.withdraw()
	root.deiconify()
root=Tk()
root.title("S.M.S.")
root.geometry("1200x700+500+300")

try:
	city = "Mumbai"
	socket.create_connection(("www.google.com",80))
	a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2 = "&q=" + city
	a3 = "&appid=c6e315d09197cec231495138183954bd"
	api_address = a1 + a2 + a3 
	res1 = requests.get(api_address)
	data = res1.json()
	temp1 = data['main']['temp']
	area=("Mumbai - ")
	final=(temp1)
	res = requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
	print(res)
	
	soup = bs4.BeautifulSoup(res.text,'lxml')

	quote = soup.find('img',{"class":"p-qotd"})
	
	quotes = quote['alt']
	
except OSError:
	messagebox.showerror("Error!",("check network!!"))




btnAdd=Button(root,text="Add",width=10,font=('arial',18,'bold'),command=f1)
btnView=Button(root,text="View",width=10,font=('arial',18,'bold'),command=f3)
lblinfo = Label(root,text=(area+str(final)+"\u2103"+"\n"+quotes),width=150,height=20,font=('arial',18,'bold'))

btnAdd.pack(pady=10)
btnView.pack(pady=10)


adst=Toplevel(root)
adst.title("Add Stu.")
adst.geometry("500x500+300+100")
adst.withdraw()

lblAddRno=Label(adst,text="enter rno",font=('arial',18,'bold'))
lblAddName=Label(adst,text="enter name",font=('arial',18,'bold'))
lblAddMarks=Label(adst,text="enter marks",font=('arial',18,'bold'))
entAddRno=Entry(adst,bd=5,font=('arial',18,'bold'))
entAddName=Entry(adst,bd=5,font=('arial',18,'bold'))
entAddMarks=Entry(adst,bd=5,font=('arial',18,'bold'))
btnAddSave=Button(adst,text="Save",font=('arial',18,'bold'),command=f5)
btnAddBack=Button(adst,text="Back",font=('arial',18,'bold'),command=f2)

lblAddRno.pack(pady=5)
entAddRno.pack(pady=5)
lblAddName.pack(pady=5)
entAddName.pack(pady=5)
lblAddMarks.pack(pady=5)
entAddMarks.pack(pady=5)
btnAddSave.pack(pady=5)
btnAddBack.pack(pady=5)

vist=Toplevel(root)
vist.title("View stu.")
vist.geometry("500x500+300+100")
vist.withdraw()

stdata=scrolledtext.ScrolledText(vist,width=30,height=20)
btnViewBack=Button(vist,text="Back",font=('arial',18,'bold'),command=f4)

stdata.pack(pady=10)
btnViewBack.pack(pady=10)


btnUpdate=Button(root,text="Update",font=('arial',18,'bold'),width=10,command=f7)

upst=Toplevel(root)
upst.title("Update Student")
upst.geometry("500x500+300+100")
upst.withdraw()

lblRno=Label(upst,text="Enter Roll No U Want to Update",font=('arial',18,'bold'))
lblName=Label(upst,text="Enter Name",font=('arial',18,'bold'))
lblMarks=Label(upst,text="Enter Marks",font=('arial',18,'bold'))
entUpdateRno=Entry(upst,bd=5)
entUpdateName=Entry(upst,bd=5)
entUpdateMarks=Entry(upst,bd=5)



btnUpdateBack=Button(upst,text="Back",font=('arial',18,'bold'),command=f9)
btnUpdateSave=Button(upst,text="Save",font=('arial',18),width=10,command=f8)

btnUpdate.pack(pady=10)
lblRno.pack(pady=10)
entUpdateRno.pack(pady=10)
lblName.pack(pady=10)
entUpdateName.pack(pady=10)
lblMarks.pack(pady=10)
entUpdateMarks.pack(pady=10)
btnUpdateSave.pack(pady=10)
btnUpdateBack.pack(pady=10)

dest=Toplevel(root)
dest.title("Delete Student")
dest.geometry("500x550+300+100")
dest.withdraw()

btnDelete=Button(root,text="Delete",font=('arial',18,'bold'),width=10,command=f11)
lblRno=Label(dest,text="Enter Roll No",font=('arial',18,'bold'))
entDeleteRno=Entry(dest,bd=5)
btnDeleteSave=Button(dest,text="Save",font=('arial',18,'bold'),width=10,command=f10)
btnDeleteBack=Button(dest,text='Back',font=('arial',18,'bold'),width=10,command=f12)


btnDelete.pack(pady=10)
lblRno.pack(pady=10)
entDeleteRno.pack(pady=10)
entDeleteRno.focus()
btnDeleteSave.pack(pady=10)
btnDeleteBack.pack(pady=10)

gst=Toplevel(root)
gst.title("Top 5 students")
gst.geometry("500x500+300+100")
gst.withdraw()

btnGraph=Button(root,text="Graph",font=('arial',18,'bold'),width=10,command=f13)
btnGraphBack=Button(gst,text='Back',font=('arial',18,'bold'),width=10,command=f14)

btnGraph.pack(pady=10)
btnGraphBack.pack(pady=10)
lblinfo.pack(pady=50)













root.mainloop()

