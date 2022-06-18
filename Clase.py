
#################################
#Elaborado por: Marbel Brenes y Samuel Garces
#Fecha de creación: 5/6/2022 15:35 p.m
#Última Modificación: 
#Versión: 3.10.4
########################
#Importación de Librerías

import random
from datetime import datetime
from validaciones import *
from funciones import *
#Bases de Datos

#Definiciónnd de Funciones


class Persona:
    def __init__(self):
        self.cedula=""
        self.nombre=""
        self.genero=True
        self.personalidad=(0,0)
        self.pais=0
        self.estado=[True,"",""]

    def asignarCedula(self,cedula):
        self.cedula=cedula
        return 
    def asignarNombre(self,nombre):
        self.nombre=nombre
        return 

    def asignarGenero(self,genero):
        if genero==True:
            self.genero=True
        else:
            self.genero=False
        return 

    def asignarPersonalidad(self,pers):
        self.personalidad=pers
        return
    def asignarPais(self,pais):
        self.pais=pais
        return 
    def asignarEstado(self,comen,fecha):#Si se asigna es porque cambia a False
        self.estado=[False,comen,fecha] 
        return
    def getCedula(self):
        return self.cedula
    def getNombre(self):
        return self.nombre
    def getGenero(self):
        if self.genero==True:
            return True
        return self.genero
    def getPersonalidad(self):
        return self.personalidad
    def getPais(self):
        return self.pais
    def getEstado(self):
        return self.estado
    def getAll(self):
        return 'Cédula: '+self.cedula+'\nNombre: '+self.nombre+'\nGénero: '+\
        str(traducirGenero(self.genero))+'\nPaís: '+str(traducirPaisSTR(self.pais))\
        +'\nPersonalidad: '+str(traducirPersonalidad(self.personalidad))+'\nEstado: '+str(traducirEstado(self.estado))+'\n'


'''for i in baseDeDatos:
    print(i.getNombre())

'''






















