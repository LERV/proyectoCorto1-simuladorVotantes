import csv, operator

csvURL = 'datos.csv'

def open_file_CSV():
	with open(csvURL) as csvarchivo:
		entrada = csv.reader(csvarchivo)
		for reg in entrada:
			print(reg)


def generar_muestra_pais(n):

	return 5
	#print("func1")

def generar_muestra_provincia(n,nombre_provincia):
	return 4
	#print("func2")


def inc(n):
	n = n +1
	return n


