try:
    divisor = int(input("Introduce un número: "))
    resultado = 10 / divisor
except ZeroDivisionError:
    print("Error: No puedes dividir por cero.")
except ValueError:
    print("Error: Debes introducir un número válido.")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Operación finalizada.")