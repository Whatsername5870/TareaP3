#################################
#Elaborado por: Marbel Brenes y Samuel Garces
#Fecha de creación: 5/6/2022 15:35 p.m
#Última Modificación: 
#Versión: 3.10.4
########################

#Importación de librerías
import re
from datetime import datetime
import random

#Bases de Datos
baseDeDatos=[] #Será la base de datos principal, una lista de objetos
paises=[] #Base de Datos de los paises
personalidades={}
tip=[]

#Funciones para Cargar Bases de Datos
def esPar(pnum):
    """
    Funcionamiento: Determina si un número es par o impar
    Entrada: digito(int)
    Salida: True False
    """
    if pnum % 2 == 1:
        return False
    else:
        return True

def fechaYHoraActual():
    """
    Funcionamiento: Genera en el formato deseado dela hora actual
    Entrada: N/D
    Salida: fechaTexto(str)
    """
    fechaYHora = datetime.now()
    fechaYHoraTexto = fechaYHora.strftime('%d-%m-%Y-%H-%M-%S')
    return fechaYHoraTexto

def fechaActual():
    """
    Funcionamiento: Genera en el formato deseado la fecha del día en que se ejecuta.
    Entrada: N/D
    Salida: Fecha del día.
    """
    fecha = datetime.now()
    fechaTexto = fecha.strftime('%d/%m/%Y')
    return fechaTexto

def generarPais(baseDatos):
    pais=random.choice(baseDatos)
    return pais

def generarPerso(DictPerso):
    opciones=[]
    for i in list(DictPerso.values()):
        for categ in i:
            opciones.append(categ[0])
    return opciones

def obtenerPersonalidad(pers):
    cont=0
    for i in personalidades:
        cont2=0
        for tup in personalidades[i]:
            if (tup[0])==str(pers):
                return cont,cont2
            cont2+=1
        cont+=1
    return 
    
def validarCantidad(cantidad):
    if type(cantidad)!=int:
        return False
    if int(cantidad)<25:
        return False
    return True

def generarTipos(personali):
    """
    Funcionamiento: Saca los tipos de personalidad y los mete a una lista
    Entrada: N/D
    Salida: 
    """
    tip=[]
    for i in personali.keys():
        tip.append(i)
    return tip


