#################################
#Elaborado por: Marbel Brenes y Samuel Garces
#Fecha de creación: 5/6/2022 15:35 p.m
#Última Modificación: 
#Versión: 3.10.4
########################
#Importación de librerías
from datetime import datetime
import random
import names
import pickle
#Bases de Datos
 #Será la base de datos principal, una lista de objetos
paises=[] #Base de Datos de los paises
personalidades={}
cedulas=[]
retirados=[]
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

def traducirPais(opcion):
    pais=paises.index(opcion)
    return pais
    
def traducirGenero(gen):
    if gen==True:
        return 'Masculino'
    else:
        return 'Femenino'

def traducirPaisSTR(num):
    f = open("paises.txt", "r")
    base = f.read()
    e = base.split("\n")
    return e[num]


def traducirPersonalidad(tupla):
    tipos=list(personalidades.keys())
    tipo=tipos[tupla[0]]
    subtipos=personalidades[tipo]
    subtipo=subtipos[tupla[1]][0]
    return str(tipo)+'-'+str(subtipo)

def traducirPersonalidadSi(tupla):
    tipos=list(personalidades.keys())
    tipo=tipos[tupla[0]]
    subtipos=personalidades[tipo]
    subtipo=subtipos[tupla[1]][0]
    return str(subtipo)

def traducirEstado(estado):
    if estado[0]==True:
        return 'Activo'
    return 'Inactivo'
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
    try:
        if int(cantidad)<25:
            return False
        return True
    except ValueError:
        return False

def generarCedulasRandom():
    cedula=str(random.randint(1,9))+'-'+str(random.randint(1000,9999))+'-'+str(random.randint(1000,9999))
    if cedula in cedulas:
        return generarCedulasRandom()
    cedulas.append(cedula)
    return cedula

def generarNombresRandom():
    """
    Funcionalidad: Genera nombres aleatorios en el formato establecido
    Entrada: N/D
    Salida: Tupla con el nombre
    """
    return names.get_full_name()+'-'+names.get_last_name()

def generarPaisRandom():
    pais=random.choice(paises)
    paisInt=paises.index(pais)
    return paisInt



def generarPersoRandom():
    tipo=random.randint(0,3)
    subtipo=random.randint(0,3)
    return tipo,subtipo


def graba(nomArchGrabar,dato):
    #Función que graba un archivo con una lista de estudiantes
    try:
        f=open(nomArchGrabar,"wb")
        pickle.dump(dato,f)
        f.close()
    except:
        print("Error al grabar el archivo: ", nomArchGrabar)

def leerArchivo(nombreArchivo):
    """
    Funcionamiento: Lee archivo en el disco duro
    Entrada: Nombre del archivo en el disco
    Salida N/D
    """
    baseDatos = []
    try:
        f=open(nombreArchivo, "rb")
        baseDatos = pickle.load(f)
        f.close()
    except:
        "No se encuentra."
    return baseDatos











    #Samuel




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


def generarTipos(personali):
    """
    Funcionamiento: Saca los tipos de personalidad y los mete a una lista
    Entrada: N/D
    Salida: tip(list)
    """
    tip=[]
    for i in personali.keys():
        tip.append(i)
    return tip

def generarCedulas(base):
    """
    Funcionamiento: Saca als cédulas y los mete a una lista
    Entrada: N/D
    Salida: ced(list)
    """
    ced=[]
    for i in base:
        aux = i.getCedula()
        ced.append(aux)
    return ced