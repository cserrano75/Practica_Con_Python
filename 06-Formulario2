import tkinter
from tkinter import messagebox

ventana = tkinter.Tk()
ventana.title("Mi Formulario")

def saludo():
    print("Hola " + entry_nombre.get() + " " + entry_apellido.get())

label_nombre = tkinter.Label(ventana, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=10, pady=5)

entry_nombre = tkinter.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

label_apellido=tkinter.Label(ventana,text="Apellido:")
label_apellido.grid(row=1, column=0, padx=10, pady=5)

entry_apellido = tkinter.Entry(ventana)
entry_apellido.grid(row=1, column=1, padx=10, pady=5)

boton_enviar = tkinter.Button(ventana, text="Enviar",command=saludo)
boton_enviar.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# 1. Mensaje de Información
messagebox.showinfo("Título","Este es un mensaje de información")

# 2. Mensaje de Advertencia
#messagebox.showwarning("Advertencia","Esto es una advertencia")

# 3. Mensaje de Error
#messagebox.showerror("Error","Ocurrió un error crítico")

'''respuesta = messagebox.askyesno("Pregunta","¿Desea continuar?")
if respuesta:
    print("El usuario dijo sí")
else:
    print("El usuario dijo no")

ventana.mainloop()'''