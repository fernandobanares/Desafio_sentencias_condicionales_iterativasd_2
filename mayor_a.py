""" Se solicita devolver un informe resumido que exponga los meses que superan un cierto
umbral. El programa mayor_a.py debe retornar un diccionario con el mes y el valor
asociado siempre y cuando superen el umbral especificado.
 """

import sys

umbral = int(sys.argv[1])

ventas = {
"Enero": 15000,
"Febrero": 22000,
"Marzo": 12000,
"Abril": 17000,
"Mayo": 81000,
"Junio": 13000,
"Julio": 21000,
"Agosto": 41200,
"Septiembre": 25000,
"Octubre": 21500,
"Noviembre": 91000,
"Diciembre": 21000,
}

def mayor_a(umbral):
    resultado = {}
    for x, y in ventas.items():
        if y > umbral:
            resultado[x] = y
    return resultado

resultado = mayor_a(umbral)
print(resultado)