#Genero formulario con TKinter
import tkinter

ventana=tkinter.Tk()
ventana.title("Principal")
ventana.geometry('500x500')

etiqueta=tkinter.Label(ventana,text="Hola Mundo")
etiqueta.pack(side=tkinter.BOTTOM)

ventana.mainloop()
