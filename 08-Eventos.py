import tkinter

#Defino mis variables
ventana = tkinter.Tk()
ventana.title("Mi Formulario")

def on_key_press(event):
    print(f"Key pressed: {event.keysym}")
def on_left_click(event):
    print(f"Left click at ({event.x}, {event.y})")

def on_right_click(event):
    print(f"Right click at ({event.x}, {event.y})")

def on_mouse_motion(event):
    print(f"Mouse moved to ({event.x}, {event.y})")

ventana.bind("<KeyPress>", on_key_press)
ventana.bind("<Button-1>", on_left_click)
ventana.bind("<Button-3>", on_right_click)
ventana.bind("<Motion>", on_mouse_motion)

ventana.mainloop()