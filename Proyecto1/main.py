from tkinter import Tk
from tkinter import *
from tkinter import filedialog

def bt():
    lbl.configure(text="ME PRESIONAROOON")

def clearTextInput():
    txt.delete("1.0","end")

def leerForm():
    Tk().withdraw() #Pido Archivo
    archivo = filedialog.askopenfile(
        title= "Seleccione un archivo",
        initialdir='./Practica1',
        filetypes=(('Archivos de data','*.form*'),)
    )  
    if archivo is not None: #Comienza analisis
        lectura = archivo.read()
        txt.insert('insert',lectura)

def analizar():
    texto = txt.get("1.0", "end-1c")
    print(texto)


if __name__ == '__main__':

    window = Tk()
    window.geometry('800x565')
    window.title("Proyecto 1 LFP")
    window.config(bg='CadetBlue')
    aux2 = ['Reporte de Tokens','Reporte de Errores','Manual de Usuario','Manual Tecnico']
    aux3 = StringVar()
    aux3.set('-REPORTES-')
    aux = OptionMenu(window,aux3,*aux2)
    aux.configure(width=15,height=2,bg='#f39c12',borderwidth=3,font='Arial 11 bold')
    aux.place(x=635,y=0)
    lbl_menu = Label(window,text='INICIO (:',bg='#f39c12',width=10,borderwidth=2,relief='raised',foreground='white',font='Arial 12 bold',height=2).place(x=0,y=0)
    btn_carga = Button(window,text='Cargar Archivo',command=leerForm,bg='#f39c12',width=11,borderwidth=4,relief='raised',foreground='black',font='Arial 11 bold',height=2).place(x=0,y=44.5)
    lbl= Label(window,text='ANALIZADOR DE TEXTOS \'.FORM\'',bg='#d4ac0d',borderwidth=5,relief='raised',foreground='black',font='Arial 12 bold',height=2).place(x=260,y=10)
    btn = Button(window, text="ANALIZAR",bg='#2980b9',borderwidth=5,fg='white',font='Arial 10 bold',command=analizar,height=2)
    btn.place(x=350,y=480)

    btnClear = Button(window, text="LIMPIAR",bg='#b3b300',borderwidth=5,fg='white',font='Arial 10 bold',command=clearTextInput,height=2)
    btnClear.place(x=200,y=500)

    btnExit = Button(window, text="EXIT",bg='red',borderwidth=5,fg='white',font='Arial 10 bold',command=window.destroy,height=2,width=7)
    btnExit.place(x=500,y=500)

    txt = Text(window,height=19,width=80,font='Arial 11',foreground='white')
    txt.config(bg='#2E2E2E')
    txt.place(x=90,y=120)
    window.mainloop()