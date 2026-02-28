import tkinter
from tkinter import ttk
from tkinter import Spinbox

#Defino mis variables
ventana = tkinter.Tk()
ventana.title("Mi Formulario")

var1 = tkinter.IntVar()
var2 = tkinter.IntVar()
v = tkinter.IntVar()

#Creo un listbox
spinbox = Spinbox(ventana, from_=0, to=10)
spinbox.grid(row=0, column=4, padx=10, pady=5)

#Combobox
def select(event):
    selected_item = combo_box.get()
    label.config(text="Selected Item: " + selected_item)

label = tkinter.Label(ventana, text="Selected Item:")
label.grid(row=0, column=0, padx=10, pady=5)

combo_box = ttk.Combobox(
    ventana,
    values=["Option 1", "Option 2", "Option 3"],
    state="readonly"
)
combo_box.grid(row=0, sticky=tkinter.W)

combo_box.set("Option 1")

combo_box.bind("<<ComboboxSelected>>", select)



#Agrego un menu en la ventana
menu = tkinter.Menu(ventana)
ventana.config(menu=menu)

filemenu = tkinter.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Open...")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=ventana.quit)

helpmenu = tkinter.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About")

#Checkbutton
tkinter.Checkbutton(ventana, text="Male", variable=var1).grid(row=1, sticky=tkinter.W)
tkinter.Checkbutton(ventana, text="Female", variable=var2).grid(row=2, sticky=tkinter.W)

#Radiobutton
tkinter.Radiobutton(ventana, text="A", variable=v, value=1).grid(row=3, sticky=tkinter.W)
tkinter.Radiobutton(ventana, text="B", variable=v, value=2).grid(row=4, sticky=tkinter.W)

ventana.mainloop()