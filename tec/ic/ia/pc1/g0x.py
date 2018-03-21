import csv, operator
csvURL = 'datos.csv'
with open(csvURL) as csvarchivo:
    entrada = csv.reader(csvarchivo)
    for reg in entrada:
        print(reg)

def generar_muestra_pais(n):
	print("func1")

def generar_muestra_provincia(n,nombre_provincia):
	print("func2")


