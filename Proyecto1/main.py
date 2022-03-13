from tkinter import *
from tkinter import ttk
from tkinter import Tk
from tkinter import messagebox

def clicked():

    messagebox.showinfo('Message title', 'Message content')
    print("ŚUPPPPPPPP")
root = Tk()
root.title('Proyecto 1')
root.geometry('700x500')
root.config(background="#f3b00b")
ttk.Label(root,text=' ANALIZADOR DE TEXTOS ',foreground='black',background='#f3b00b',font=('Arial',16,'bold')).place(x=220,y=20)
frame = Frame(root)
frame.pack(padx=40,pady=50)
frame.config(bg="lightblue")     
frame.config(width=550,height=500) 
ttk.Label(root,text='Cargar archivo ".form"',foreground='black',background='#ffd062',font=('Arial',13,'bold')).place(x=252,y=70)
s = ttk.Style()
s.configure('a.TButton',foreground='magenta')

ttk.Button(frame,text="CARGAR ARCHIVO",style='a.TButton',command=clicked).place(x=214,y=60)
ttk.Button(frame,text="CARGAR ").place(x=214,y=100)

root.mainloop()
