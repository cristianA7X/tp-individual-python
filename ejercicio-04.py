"""
Ejercicio 4 – Funciones
Crear una función llamada area_rectangulo que reciba dos parámetros:
base
altura
La función debe calcular y retornar el área del rectángulo.
Luego, llamar a la función con los valores:
base = 8
altura = 5
y mostrar el resultado por pantalla.
"""

def area_rectangulo(base, altura):
    return base * altura

# Llamar a la función con los valores base = 8 y altura = 5
base = 8
altura = 5
resultado = area_rectangulo(base, altura)
print(f"El área del rectángulo es: {resultado}")
