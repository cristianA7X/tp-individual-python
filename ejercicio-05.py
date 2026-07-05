"""
Ejercicio 5 – Diccionarios y recorrido
Dado el siguiente diccionario:
alumno = {
"nombre": "Lucía",
"edad": 20,
"curso": "Python"
}
Realizar un programa que recorra el diccionario con un for y muestre por pantalla cada
clave junto con su valor.
Ejemplo esperado:
nombre : Lucía
edad : 20
curso : Python
"""

alumno = {
    "nombre": "Lucía",
    "edad": 20,
    "curso": "Python"
}

for clave in alumno:
    valor = alumno[clave]
    print(f"{clave} : {valor}")
