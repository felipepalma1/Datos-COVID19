<<<<<<< HEAD
import csv

with open('output/productos/producto2/2020-07-01-CasosConfirmados.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
=======
# Los guiones son instrucciones entregadas a python para que lea y escriba información sobre los bancos de datos (conocidos en este sistema como 'productos')


# -- Python, conéctate con el archivo 2020-07-01-CasosConfirmados.csv - Muestra lo que ves
import csv
with open('output/producto2/2020-07-01-CasosConfirmados.csv', newline="") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)

>>>>>>> 664ddf90e0769d6256d673438e3780047167f920
