# Los guiones son instrucciones entregadas a python para que lea y escriba información sobre los bancos de datos (conocidos en este sistema como 'productos')


# -- Python, conéctate con el archivo 2020-07-01-CasosConfirmados.csv - Muestra lo que ves
# -- Idea, tomar salida y convertirla a archvo


import csv
import sys

with open('output/producto2/2020-07-01-CasosConfirmados.csv', newline="") as archivo:
    comunas = []
    
    lector = csv.reader(archivo)
    for fila in lector:
        comuna = [fila[2],fila[4], fila[5]]
        comunas.append(comuna)
    
    def imprimirComunas(comunas):
        for comuna in comunas:
            print('--------------------------------------\n\n')
            print('Comuna:', comuna[0])
            print('Población total:', comuna[1])
            print('Contagios confirmados:', comuna[2])
            print('\n')
            print('--------------------------------------\n\n')

    def buscarPorComuna(comuna):
        comuna = comuna
        print('Comuna seleccionada →', comuna)

    # imprimirComunas(comunas)

if __name__ == "__main__":
    main(sys.argv[1:])


    # Pasa lista a cadena -- Cadena  hacia archivo --
    # ct = str(comunas)
    # archivo = open("comunas.texto", "w")
    # archivo.write(ct)
    # archivo.close()

