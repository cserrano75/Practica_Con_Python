#Genero formulario con TKinter
import tkinter

ventana=tkinter.Tk()
ventana.title("Principal")

def create_widget(parent, widget_type, **options):
    return widget_type(parent, **options)

def saludo():
    print("Hola... ")

#Creo un primer Frame
frame1 = tkinter.LabelFrame(ventana, text="Datos Proyecto", padx=150, pady=150)
# Displaying the frame1 in row 0 and column 0
frame1.grid(row=0, column=0)

# Agrego un boton
b1 = tkinter.Button(frame1, text="Apple")

# Displaying the button b1
b1.pack()

#Creo un segundo Frame
frame2 = tkinter.LabelFrame(ventana, text="Datos Cotización", padx=150, pady=150)
# Displaying the frame1 in row 0 and column 0
frame2.grid(row=0, column=1)

# Agrego un boton
b2 = tkinter.Button(frame2, text="Apple")

# Displaying the button b1
b2.pack()

ventana.mainloop()