from tkinter import *
root=Tk()
root.title("Calculator")
root.geometry('280x250+100+200')
img=PhotoImage(file="C:\\Users\\91895\\Downloads\\image.png")
root.iconphoto(root,img)
root['bg']='#CAFF70'
root.resizable(False,False)
def divide():
    e3.config(fg="red")
    try:
        e3.delete(0,END)
        fno=int(e1.get())
        sno=int(e2.get())
        result=fno/sno
        e3.insert(0,str(result))
    except ZeroDivisionError:
        e3.insert(0,"Denominator should not be 0")
    except ValueError:
        e3.insert(0,"Please input digits only")
    else:
        e3.config(fg="green")
        def multiply():
            e3.config(fg="red")
            try:
                e3.delete(0, END)
                fno = int(e1.get())
                sno = int(e2.get())
                result = fno * sno
                e3.insert(0, str(result))
            except ValueError:
                e3.insert(0, "Please input digits only")
            else:
                e3.config(fg="green")
def multiply():
    e3.config(fg="red")
    try:
          e3.delete(0, END)
          fno = int(e1.get())
          sno = int(e2.get())
          result = fno * sno
          e3.insert(0, str(result))
    except ValueError:
          e3.insert(0, "Please input digits only")
    else:
          e3.config(fg="green")

def addition():
    e3.config(fg="red")
    try:
        e3.delete(0, END)
        fno = int(e1.get())
        sno = int(e2.get())
        result = fno + sno
        e3.insert(0, str(result))
    except ValueError:
        e3.insert(0, "Please input digits only")
    else:
        e3.config(fg="green")
def substraction():
    e3.config(fg="red")
    try:
        e3.delete(0, END)
        fno = int(e1.get())
        sno = int(e2.get())
        result = fno - sno
        e3.insert(0, str(result))
    except ValueError:
        e3.insert(0, "Please input digits only")
    else:
        e3.config(fg="green")
def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e1.focus()
def finish():
    root.destroy()
l1=Label(root,text="Simple Calulator",font="Arial 18 bold",anchor=NE)
l1['bg']="white"
l2=Label(root,text="First no :",font="Arial 13 bold")
l2.config(fg="white",bg="#CDB79E",width=12,height=1,relief="groove")
l3=Label(root,text="Second no :",font="Arial 13 bold")
l3.config(fg="white",bg="#CDB79E",width=12,height=1,relief="groove")
l4=Label(root,text="Result :",font="Arial 12 bold")
l4.config(fg="white",bg="#CDB79E",width=12,height=1,relief="groove")
e1=Entry(root)
e2=Entry(root)
e3=Entry(root)

b1=Button(root,text="Divide",command=divide)
b1.config(bg="#3D59AB",fg="white",borderwidth=6,relief="raised")
b2=Button(root,text="Multiply",command=multiply)
b2.config(bg="#3D59AB",fg="white",borderwidth=6,relief="raised")
b3=Button(root,text="Addition",command=addition)
b3.config(bg="#3D59AB",fg="white",borderwidth=6,relief="raised")
b4=Button(root,text="Subtraction",command=substraction)
b4.config(bg="#3D59AB",fg="white",borderwidth=6,relief="raised")
b5=Button(root,text="Clear",command=clear)
b5.config(bg="#3D59AB",fg="white",borderwidth=6,relief="raised")
b6=Button(root,text="Quit",command=finish)
b6.config(bg="#3D59AB",fg="white",borderwidth=6,relief="raised")

l1.grid(row=0,column=0,columnspan=4)
l2.grid(row=1,column=0,sticky=W)
l3.grid(row=2,column=0,sticky=W)
e1.grid(row=1,column=1)
e1.config(width=20)
e2.grid(row=2,column=1,padx=4)
e3.grid(row=3,column=1)
b1.grid(row=4,column=0,sticky=E+W,pady=5,padx=5)
b2.grid(row=4,column=1,sticky=W+E,pady=5,padx=5)
b3.grid(row=5,column=0,sticky=E+W,pady=5,padx=5)
b4.grid(row=5,column=1,sticky=E+W,pady=5,padx=5)
b5.grid(row=6,column=0,sticky=E+W,pady=5,padx=5)
b6.grid(row=6,column=1,sticky=E+W,pady=5,padx=5)
l4.grid(row=3,column=0,sticky=E+W)
root.mainloop()
