
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
    def __init__(self,cedula,nombre,genero,pais,pers):
        self.cedula=cedula
        self.nombre=nombre
        self.genero=genero
        self.personalidad=pers
        self.pais=pais
        self.estado=[True,"",""]

    def asignarCedula(self,cedula):
        self.cedula=cedula
        return 

    def asignarNombre(self,nombre):
        self.nombre=nombre
        return 

    def asignarGenero(self,genero):
        if int(genero)==1:
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
        
    def asignarEstado(self,estado):
        self.estado=estado
        return 
    def getCedula(self):
        return self.cedula
    def getNombre(self):
        return self.nombre
    def getGenero(self):
        return self.genero
    def getPersonalidad(self):
        return self.personalidad
    def getPais(self):
        return self.pais
    def getEstado(self):
        return self.estado


def solicitarDatos():
    cedula=input('Ingrese su cédula con el formato #-####-####: ')
    if validarCedula(cedula):
        nombre=input('Ingrese su nombre con el formato Nombre Apellido1-Apellido2: ')
        if validarNombre(nombre):
            genero=input('Ingrese el genero.\n1- Hombre\n2- Mujer\nEscoga la opciÃ³n: ')
            if validarGenero(genero):
                persona=Persona(cedula,nombre,genero)
                baseDeDatos.append(persona) 
                return 'Registro Excitoso'
            return solicitarDatos()
        return solicitarDatos()
    return solicitarDatos()




'''for i in baseDeDatos:
    print(i.getNombre())

'''






















