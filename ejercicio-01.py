"""
Ejercicio 1 – Condicionales e input
Realizar un programa que pida al usuario su edad y muestre por pantalla:
 “Menor de edad” si tiene menos de 18 años.
 “Mayor de edad” si tiene 18 años o más.
Recordar convertir el dato ingresado a número entero.
"""

# Solicitar al usuario que ingrese su edad
edad = input("Por favor, ingrese su edad: ")
print()

# Validar que no sea un string 
while not edad.isdecimal():
    print("Error. Valor inválido.")
    edad = input("Ingrese su edad: ")
    print()
    


# Validar si es mayor o menor de edad
if int(edad) < 18:
    print("Usted es menor de edad")
else:
    print("Usted es mayor de edad")