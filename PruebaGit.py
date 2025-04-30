# Solicitar dos números al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Sumar los números
suma = num1 + num2

# Determinar si la suma es mayor, igual o menor a 10
if suma > 10:
    print(f"La suma ({suma}) es mayor a 10.")
elif suma == 10:
    print(f"La suma ({suma}) es igual a 10.")
else:
    print(f"La suma ({suma}) es menor a 10.")

