""" Se requiere la construcción de una aplicación interactiva primeros_auxilios.py que
entregue los distintos pasos a seguir dependiendo de las respuestas que el usuario entrega
en tiempo real. """

def emergencia():
    respuesta1 = input("El paciente responde a estímulos? Responda si o no: ").lower()
    if respuesta1 == "si":
        print("Valorar la necesidad de llevarlo al hospital más cercano")
    else:
        print("Abrir la vía Aérea")
        respuesta2 = input("El paciente respira? Responda si o no: ").lower()
        if respuesta2 == "si":
            print("Permitirle posición de suficiente ventilación")
            return
        else:
            print("Administrar 5 Ventilaciones y llamar a Ambulancia")
            
            while True:
                respuesta3 = input("El paciente tiene signos de vida? Responda si o no: ").lower()
                if respuesta3 == "si":
                    print("Reevaluar a la espera de la Ambulancia")
                else:
                    print("Administrar Compresiones Torácicas hasta que llegue ambulancia")
                respuesta4 = input("Llego la ambulancia? Responda si o no: ").lower()
                if respuesta4 == "si":
                    break
emergencia()            