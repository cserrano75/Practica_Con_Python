#Genero formulario con TKinter
import tkinter

ventana=tkinter.Tk()
ventana.title("Principal")

def create_widget(parent, widget_type, **options):
    return widget_type(parent, **options)

frame = create_widget(
    ventana, tkinter.Frame,
    bg='grey', bd=3, cursor='hand2',
    height=100, width=200,
    highlightcolor='red',
    highlightbackground='black',
    highlightthickness=2,
    relief=tkinter.RAISED
)
frame.grid(row=0, column=0, padx=100, pady=100)

label = create_widget(
    frame, tkinter.Label,
    text='GeeksForGeeks',
    font='50', bg='grey',
    bd=3, cursor='hand2',
    highlightcolor='red',
    highlightbackground='black',
    highlightthickness=1,
    relief=tkinter.RAISED
)
label.grid(row=0, column=1, padx=10, pady=5)

ventana.mainloop()