import tkinter as tk

root = tk.Tk()
root.title("Ventana Responsiva")
root.geometry("400x300") # Tamaño inicial
root.minsize(300, 200) # Tamaño mínimo de seguridad

# Cambiar el icono
# Asegúrate de tener el archivo 'formulario.ico' en la misma carpeta
try:
    root.iconbitmap("formulario.ico")
except:
    print("Icono no encontrado, asegúrate de que 'formulario.ico' está en la ruta.")

# --- Opción 1: Maximizar (Windows/Linux) ---
root.state('zoomed')

# --- Configuración Responsiva (Core) ---
# Configuramos la fila 0 y columna 0 para que se expandan
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Frame principal que ocupará todo el espacio
main_frame = tk.Frame(root, bg="lightgray")
main_frame.grid(row=0, column=0, sticky="nsew") # sticky "nsew" hace que se expanda

# Widget dentro del frame que también se expande
label = tk.Label(main_frame, text="Soy responsivo", bg="white")
label.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

# Hacer que el interior del frame se expanda
main_frame.rowconfigure(0, weight=1)
main_frame.columnconfigure(0, weight=1)

root.mainloop()
