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
bdRespaldo={}

#Funciones para Cargar Bases de Datos
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
    for i in personali.keys():
        tip.append(i)
        print(i)
    bdRespaldo = personali
    return tip

def generarHtmlPersonalidades():
    """
    Funcionamiento: Crea el archivo HTML para ReportePersonalidades
    Entrada: N/D
    Salida: N/D
    """
    tabla=""
    f = open('PersonalidadesHTML.html','w')
    tipAux = generarTipos(personalidades)

    mensajeInicio = "<html><head></head><body><h1>"
            
    titulo = "Reporte Personalidades"

    mensajeMedio="</h1>"

    tabla+= "<table border='1'><tbody><tr>"

    #Crea los encabezados agarrando las llaves del diccionario
    for n in tipAux:
        encabezadosTabla1="<td colspan='2'>"
        tabla+= encabezadosTabla1+str(n)
        encabezadosTabla2="</td>"
        tabla+= encabezadosTabla2
    tabla+="</tr><tr>"

    cant=0
    for m in bdRespaldo:
        contenidotabla1="<td>"
        tabla+= contenidotabla1+str(bdRespaldo[m])
        tabla+="</td>"
        cant+=1
    
    tabla+="</tr></table></tbody>"
    print(tabla)
    mensajeFinal = "</body></html>"

    mensajeCompleto = mensajeInicio + titulo + mensajeMedio + tabla + mensajeFinal

    f.write(mensajeCompleto)
    f.close()
    
    return ''
