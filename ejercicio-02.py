"""
Ejercicio 2 – Bucle while
Realizar un programa que pida una contraseña al usuario.
La contraseña correcta será:
python123
El programa debe volver a pedir la contraseña hasta que el usuario la ingrese
correctamente.
Cuando la contraseña sea correcta, debe mostrar:
Acceso permitido
"""

# Solicitar al usuario que ingrese la contraseña
contrasenia = input("Contraseña: ")

contrasenia_correcta = "python123"

# Bucle while para verificar la contraseña
while contrasenia != contrasenia_correcta:
    print("Contraseña incorrecta. Inténtalo de nuevo.")
    contrasenia = input("Contraseña: ")

print("Acceso permitido")
