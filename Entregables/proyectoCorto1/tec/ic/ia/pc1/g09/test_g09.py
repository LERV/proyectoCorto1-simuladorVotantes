## Archivo de pruebas unitarias para las funciones implementadas en el archivo _init_.py


from g09 import generar_muestra_pais

def test_generar_poblacion():
	assert generar_poblacion() == 0
	
def test_generar_muestra_pais():
	assert len(generar_muestra_pais(5)) > 2

def test_generar_muestra_provincia():
	assert len(generar_muestra_provincia(5,"LIMON")) > 2

def test_generar_random():
	assert generar_random(100) <= 100

def test_generar_edad():
	assert (generar_edad() > 1) 
