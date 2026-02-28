#Pido nombre y edad y calculo cuanto le falta para cumplr 100 años
nombre_usuario = input("Ingrese su nombre: ")
print("Hola " + nombre_usuario )

edad_usuario = int(input("Ingrese su edad: "))
edad_100 = 100 - edad_usuario
print("Hola " + nombre_usuario + " tienes " + str(edad_usuario) + " años, te faltan " + str(edad_100) + " años para cumplir 100 años")
