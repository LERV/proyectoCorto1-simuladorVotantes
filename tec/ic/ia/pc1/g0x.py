import csv, operator
import random

csvURL = 'tec/ic/ia/pc1/datos.csv'
poblacion = []
def generar_muestra_pais(n):
    numeros = []
    resultado = []
    i = 0
    while(i<n):
    	rand = generar_random(len(poblacion)-1)
    	if(not(rand in numeros)):
    		resultado.append(poblacion[rand])
    		numeros.append(rand)
    		i+=1
    return resultado

def generar_muestra_provincia(n,nombre_provincia):
	subpoblacion = []
	for x in poblacion:
		if(x[1]==nombre_provincia):
			subpoblacion.append(x)
	numeros = []
	resultado = []
	i = 0
	while(i<n):
		rand = generar_random(len(subpoblacion)-1)
		if(not(rand in numeros)):
			resultado.append(subpoblacion[rand])
			numeros.append(rand)
			i+=1
	return resultado

	


def generar_random(max):
    return int(random.random() * max)


def generar_poblacion():
    with open(csvURL) as csvarchivo:
        entrada = csv.reader(csvarchivo)
        for reg in entrada:
            for x in range (int(reg[1])):
                hombre = 0
                individuo = []
                individuo.append(reg[0])    #Partido
                individuo.append(reg[2])    #Provincia
                individuo.append(reg[3])    #Canton
                individuo.append(reg[4])    #Poblacion
                individuo.append(reg[5])    #Superficie
                individuo.append(reg[6])    #Densidad
                if(generar_random(100)<int(float(reg[7]))): #Urbano vs Rural
                    individuo.append("Urbana")
                else:
                    individuo.append("Rural")
                if(generar_random(100)<int(float(reg[8]))*100/(int(float(reg[8]))+100)): #Hombre vs Mujer
                    individuo.append("Hombre")
                    hombre = 1
                else:
                    individuo.append("Mujer")
                individuo.append(reg[9])    #Promedio de ocupantes por vivienda
                individuo.append(reg[10])    #Promedio de ocupantes por vivienda
                if(generar_random(100)<int(float(reg[11]))): #Vivienda en buen estado vs Vivienda en mal estado
                    individuo.append("Vivienda en buen estado")
                else:
                    individuo.append("Vivienda en mal estado")
                if(generar_random(100)<int(float(reg[12]))): #Vivienda hacinada vs Vivienda no hacinada
                    individuo.append("Vivienda hacinada")
                else:
                    individuo.append("Vivienda no hacinada")
                if(generar_random(100)<int(float(reg[13]))): #No analfabeta vs Analfabeta
                    individuo.append("No analfabeta")
                else:
                    individuo.append("Analfabeta")
                individuo.append(reg[14])    #Escolaridad promedio    
                if(generar_random(100)<int(float(reg[15]))): #Asistencia de educacion regular vs No asistencia a la educacion regular
                    individuo.append("Asiste a educacion regular")
                else:
                    individuo.append("No asiste a educacion regular")
                if(hombre):
                    if(generar_random(100)<int(float(reg[16]))): #En la fuerza de trabajo hombres vs Fuera de la fuerza de trabajo hombres
                        individuo.append("En la fuerza de trabajo")
                    else:
                        individuo.append("Fuera de la fuerza de trabajo")
                else:
                    if(generar_random(100)<int(float(reg[17]))): #En la fuerza de trabajo mujeres vs Fuera de la fuerza de trabajo mujeres
                        individuo.append("En la fuerza de trabajo")
                    else:
                        individuo.append("Fuera de la fuerza de trabajo")
                if(generar_random(100)<int(float(reg[18]))): #Trabaja sin seguro vs Trabaja con seguro
                    individuo.append("Trabaja sin seguro")
                else:
                    individuo.append("Trabaja con seguro")
                if(generar_random(100)<int(float(reg[19]))): #Nacido en el extranjero vs No nacido en el extranjero
                    individuo.append("Nacido en el extranjero")
                else:
                    individuo.append("No nacido en el extranjero")
                if(generar_random(100)<int(float(reg[20]))): #Discapacitado vs No discapacitado
                    individuo.append("Discapacitado")
                else:
                    individuo.append("No discapacitado")
                if(generar_random(100)<int(float(reg[21]))): #No asegurado vs Asegurado
                    individuo.append("No asegurado")
                else:
                    individuo.append("Asegurado")
                if(generar_random(100)<int(float(reg[22]))): #Hogar con jefatura femenina vs Hogar sin jefatura femenina
                    individuo.append("Hogar con jefatura femenina")
                else:
                    individuo.append("Hogar sin jefatura femenina")
                if(generar_random(100)<int(float(reg[23]))): #Hogar con jefatura compartida vs Hogar sin jefatura compartida
                    individuo.append("Hogar con jefatura compartida")
                else:
                    individuo.append("Hogar sin jefatura compartida")
                poblacion.append(individuo)

generar_poblacion()
