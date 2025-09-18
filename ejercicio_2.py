import csv

try:
    with open('total-usuarios-por-dia.csv', 'r', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        print(lector)
except IOError:
    print('A ocurrido un error leyendo el archivo.')