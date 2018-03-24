
from g0x import *

def test_generar_poblacion():
	assert generar_poblacion() == 0
def test_generar_muestra_pais():
	assert len(generar_muestra_pais(5)) > 2

def test_generar_muestra_provincia():
	assert len(generar_muestra_provincia(5,"LIMON")) > 2

