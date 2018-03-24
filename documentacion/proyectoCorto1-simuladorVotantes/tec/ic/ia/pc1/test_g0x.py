
from g0x import *

#def test_open_file_CSV():
#	assert open_file_CSV()

def test_generar_muestra():
	assert generar_muestra_pais(5) == 5

def test_generar_muestra_provincia():
	assert generar_muestra_provincia(5, "LIMON") == 4

def test_inc():
	assert inc(4) == 5