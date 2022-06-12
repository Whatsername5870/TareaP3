#################################
#Elaborado por: Marbel Brenes y Samuel Garces
#Fecha de creación: 5/6/2022 15:35 p.m
#Última Modificación: 
#Versión: 3.10.4
########################
#Validaciones
import re

def validarCedula(cedula):
    if re.match('^\d{1}\-{1}\d{4}\-{1}\d{4}$',cedula):
        return True
    return False

def validarNombre(nom):
    '''Funcionalidad: Validar que el nombre esté correcto
    Entradas: nom(tuple), tupla con el nombre y apellidos a validar 
    Salidas: Valores boolenaos en caso de cumplirse la condición.'''
    if len(nom) < 2:
        return False   
    if not re.match('^[A-Z]{1}[a-z]+\s[A-Z]{1}[a-z]+\-[A-Z]{1}[a-z]+$',nom):
        return False
    return True
    
def validarGenero(genero):
    if int(genero)== 1 or int(genero)==2:
        return True
    return False