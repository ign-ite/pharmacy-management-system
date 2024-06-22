from tkinter import *
from tkinter import messagebox
import os
f=open("database_proj",'a+')
root = Tk()
root.title("Simple Pharmacy Managment System")
root.configure(width=1500,height=600,bg='BLACK')
var=-1

def additem():
    global var
    num_lines = 0
    with open("database_proj", 'r') as f10:
        for line in f10:
            num_lines += 1
    var=num_lines-1
    e1= entry1.get()
    e2=entry2.get()
    e3=entry3.get()
    e4=entry4.get()
    e5=entry5.get()
    f.write('{0} {1} {2} {3} {4}\n'.format(str(e1),e2,e3,str(e4),e5))
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)


def deleteitem():
    e1=entry1.get()
    with open(r"database_proj") as f, open(r"database_proj1", "w") as working:
        for line in f:
            if str(e1) not in line:
                working.write(line)
    os.remove(r"database_proj")
    os.rename(r"database_proj1", r"database_proj")
    f.close()
    working.close()
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)



label0= Label(root,text="PHARMACY MANAGEMENT SYSTEM ",bg="black",fg="white",font=("Times", 30))
label1=Label(root,text="ENTER ITEM NAME",bg="red",relief="ridge",fg="white",font=("Times", 12),width=25)
entry1=Entry(root , font=("Times", 12))
label2=Label(root, text="ENTER ITEM PRICE",bd="2",relief="ridge",height="1",bg="red",fg="white", font=("Times", 12),width=25)
entry2= Entry(root, font=("Times", 12))
label3=Label(root, text="ENTER ITEM QUANTITY",bd="2",relief="ridge",bg="red",fg="white", font=("Times", 12),width=25)
entry3= Entry(root, font=("Times", 12))
label4=Label(root, text="ENTER ITEM CATEGORY",bd="2",relief="ridge",bg="red",fg="white", font=("Times", 12),width=25)
entry4= Entry(root, font=("Times", 12))
label5=Label(root, text="ENTER ITEM DISCOUNT",bg="red",relief="ridge",fg="white", font=("Times", 12),width=25)
entry5= Entry(root, font=("Times", 12))
button1= Button(root, text="ADD ITEM", bg="white", fg="black", width=20, font=("Times", 12),command=additem)
button2= Button(root, text="DELETE ITEM", bg="white", fg="black", width =20, font=("Times", 12),command=deleteitem)
button3= Button(root, text="VIEW FIRST ITEM" , bg="white", fg="black", width =20, font=("Times", 12),command=firstitem)
button4= Button(root, text="VIEW NEXT ITEM" , bg="white", fg="black", width =20, font=("Times", 12), command=nextitem)
button5= Button(root, text="VIEW PREVIOUS ITEM", bg="white", fg="black", width =20, font=("Times", 12),command=previousitem)
button6= Button(root, text="VIEW LAST ITEM", bg="white", fg="black", width =20, font=("Times", 12),command=lastitem)
button7= Button(root, text="UPDATE ITEM", bg="white", fg="black", width =20, font=("Times", 12),command=updateitem)
button8= Button(root, text="SEARCH ITEM", bg="white", fg="black", width =20, font=("Times", 12),command=searchitem)
button9= Button(root, text="CLEAR SCREEN", bg="white", fg="black", width=20, font=("Times", 12),command=clearitem)