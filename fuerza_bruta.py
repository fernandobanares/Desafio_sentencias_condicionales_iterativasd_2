""" Determinar cuántos intentos son necesarios para encontrar combinaciones numéricas en
minúscula. El programa fuerza_bruta.py debe intentar todas las combinaciones de letras
posibles, en orden alfabético, hasta que la combinación de letras sea igual a la de la
contraseña indicada. Deberá hacer este proceso letra por letra, de izquierda a derecha. """

import getpass
from string import ascii_lowercase

password = getpass.getpass("Ingrese la clave secreta:").lower()
intentos = 0

for a in password:
    for b in ascii_lowercase:
        intentos += 1
        if a == b:
            break
        
print (f"La contraseña fue forzada en {intentos} intentos")
        


