Python
import os
# VULNERABILIDAD: Credenciales expuestas
DB_PASSWORD = "SuperSecretPassword123!"
def calcular_promedio(valores):
 # CODE SMELL: Comparación booleana explícita y falta de manejo de
lista vacía
 if len(valores) == 0:
 return 0

 suma = 0
 for v in valores:
 suma += v
 return suma / len(valores)
# CODE SMELL: Código no utilizado
def funcion_inutil():
 pass
