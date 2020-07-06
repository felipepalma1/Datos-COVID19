import csv

with open('output/productos/producto2/2020-07-01-CasosConfirmados.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))