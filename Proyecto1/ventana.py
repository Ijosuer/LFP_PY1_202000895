from tkinter import Tk
from tkinter import *
import tkinter

def bt():
    lbl.configure(text="ME PRESIONAROOON")
window = Tk()
window.geometry('800x550')
window.title("Welcome to LikeGeeks app")
window.config(bg='CadetBlue')
aux2 = ['1','2','3','4']
aux3 = StringVar()
aux3.set('-REPORTES-')
aux = OptionMenu(window,aux3,*aux2)
aux.configure(width=10,height=2,bg='#f39c12',borderwidth=3,font='Arial 11 bold')
aux.place(x=675,y=0)
lbl_menu = Label(window,text='INICIO (:',bg='#f39c12',width=10,borderwidth=2,relief='raised',foreground='white',font='Arial 12 bold',height=2).place(x=0,y=0)
btn_carga = Button(window,text='Cargar Archivo',bg='#f39c12',width=11,borderwidth=4,relief='raised',foreground='black',font='Arial 11 bold',height=2).place(x=0,y=44.5)
lbl= Label(window,text='ANALIZADOR DE TEXTOS \'.FORM\'',bg='#d4ac0d',borderwidth=5,relief='raised',foreground='black',font='Arial 12 bold',height=2).place(x=260,y=10)
btn = Button(window, text="ANALIZAR",bg='#2980b9',borderwidth=5,fg='yellow',command=bt)
btn.place(x=380,y=495)

txt = Text(window,height=19,width=80,font='Arial 11',foreground='white')
txt.config(bg='#2E2E2E')
txt.place(x=90,y=120)
window.mainloop()