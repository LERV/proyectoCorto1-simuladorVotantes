
from g09 import *

def test_generar_poblacion():
	assert generar_poblacion() == 0
	
def test_generar_muestra_pais():
	assert len(generar_muestra_pais(5)) > 2

def test_generar_muestra_provincia():
	assert len(generar_muestra_provincia(5,"LIMON")) > 2

def test_generar_random():
	assert generar_random(100) <= 100 and generar_random(100)>=0

def test_generar_estado_vivienda():
	assert (generar_estado_vivienda(50) == "Vivienda en buen estado" or generar_estado_vivienda(50) == "Vivienda en mal estado")

def test_generar_edad():
	assert (generar_edad() > 1 and generar_edad() < 110) 
