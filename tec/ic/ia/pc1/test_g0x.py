
from g0x import *

#def test_open_file_CSV():
#	assert open_file_CSV()

def test_generar_muestra_pais():
	assert len(generar_muestra_pais(5)) > 2

def test_generar_muestra_provincia():
	assert len(generar_muestra_provincia(5,"LIMON")) > 2

