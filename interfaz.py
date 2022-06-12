#################################
#Elaborado por: Marbel Brenes y Samuel Garces
#Fecha de creación: 5/6/2022 15:35 p.m
#Última Modificación: 
#Versión: 3.10.4
########################
#Importación de Librerías
from optparse import Values
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox as mb
from funciones import*
from validaciones import *
from Clase import *
#Bases de Datos
baseDeDatos=[] #Será la base de datos principal, una lista de objetos
paises=[] #Base de Datos de los paises
personalidades={}
#Ventana Principal
ventana = Tk()
ventana.resizable(0,0)
ventana.title("Tarea Porgramada Tres Marbel y Samuel")


def cargarBaseDatosPaises():
    """
    Funcionamiento: Carga la base de datos de un archivo de texto de paises
    Entrada: N/D
    Salida: Base de datos de los paises en un diccionario
    """
    f = open("paises.txt", "r")
    base = f.read()
    e = base.split("\n")
    for i in e:
        paises.append(i)
    print(paises)
    return paises





def cargarBaseDatosPerso():
    """
    Funcionamiento: Carga la base de datos de un archivo de texto de personalidades
    Entrada: N/D
    Salida: Base de datos de los paises en un diccionario
    """
    f = open("personalidades.txt", "r",encoding="utf8")
    base = f.read()
    e = base.split("\n")
    cont=0
    for i in e:
        if cont!=1 and cont!=7 and cont!=13 and cont!=19:
            if cont==0:
                tipo=[tuple((e[2].split(':')[0][1::],e[2].split(':')[1])),
                tuple((e[3].split(':')[0][1::],e[3].split(':')[1])),
                tuple((e[4].split(':')[0][1::],e[4].split(':')[1])),
                tuple((e[5].split(':')[0][1::],e[5].split(':')[1]))]
                personalidades[i[1::]]=tipo
            elif cont==6:
                tipo=[tuple((e[8].split(':')[0][1::],e[8].split(':')[1])),
                tuple((e[9].split(':')[0][1::],e[9].split(':')[1])),
                tuple((e[10].split(':')[0][1::],e[10].split(':')[1])),
                tuple((e[11].split(':')[0][1::],e[11].split(':')[1]))]
                personalidades[i[1::]]=tipo
            elif cont==12:
                tipo=[tuple((e[14].split(':')[0][1::],e[14].split(':')[1])),
                tuple((e[15].split(':')[0][1::],e[15].split(':')[1])),
                tuple((e[16].split(':')[0][1::],e[16].split(':')[1])),
                tuple((e[17].split(':')[0][1::],e[17].split(':')[1]))]
                personalidades[i[1::]]=tipo
            elif cont==18:
                tipo=[tuple((e[20].split(':')[0][1::],e[20].split(':')[1])),
                tuple((e[21].split(':')[0][1::],e[21].split(':')[1])),
                tuple((e[22].split(':')[0][1::],e[22].split(':')[1])),
                tuple((e[23].split(':')[0][1::],e[23].split(':')[1]))]
                personalidades[i[1::]]=tipo
            cont+=1
        else: 
            cont+=1
    if len(paises)>0:
        print(personalidades)
        insertarPart.config(state=ACTIVE)
        insertarNPart.config(state=ACTIVE)
    return personalidades



#Frame Principal
def ventanaPrincipal():
    """
    Funcionamiento: Crea la ventanta principal
    Entrada: N/D
    Salida: Ventana principal
    """
    clean()
    ventana.geometry("650x850")
    ventana['bg']='#FCF8E8'
    titulo.grid(row=0, column=0, pady=20)
    cargarBD.grid(row=1, column=0, padx=15, pady=15)    
    insertarPart.grid(row=2, column=0, padx=15) 
    insertarNPart.grid(row=3, column=0, padx=15, pady=15)
    modificar.grid(row=4, column=0, padx=15)
    eliminar.grid(row=5, column=0, padx=15, pady=15)
    xml.grid(row=6, column=0, padx=20)
    reportes.grid(row=7, column=0, padx=15, pady=15)
    salir.grid(row=8, column=0, padx=20)
    if len(baseDeDatos)>0:
        modificar.config(state=ACTIVE)
        eliminar.config(state=ACTIVE)

    #Ocultar Botones de Participantes
    tituloAñadir.grid_remove()
    cedulaTitulo.grid_remove()
    cedulaEntrada.grid_remove()
    nombreTitulo.grid_remove()
    nombreEntrada.grid_remove()
    generotitulo.grid_remove()
    generoM.grid_remove()
    generoF.grid_remove()
    personalidadTitulo.grid_remove()
    personalidadEntrada.grid_remove()
    estadoTitulo.grid_remove()
    estadoEntrada.grid_remove()
    paisTitulo.grid_remove()
    paisEntrada.grid_remove()
    
#Ventana Añadir Participantes

def ventanaAnhadirPart():
    ventana.geometry("500x450")
    tituloAñadir.grid(row=0, column=0, sticky=W, columnspan=2)
    cedulaTitulo.grid(row=1, column=0, sticky=W)
    cedulaEntrada.grid(row=1, column=1, sticky=W)
    nombreTitulo.grid(row=2, column=0, sticky=W)
    nombreEntrada.grid(row=2, column=1, sticky=W)
    generotitulo.grid(row=3, column=0, sticky=W)
    generoM.grid(row=3, column=1, sticky=W)
    generoF.grid(row=4, column=1, sticky=W)
    personalidadTitulo.grid(row=5, column=0, sticky=W)
    personalidadEntrada.grid(row=5, column=1, sticky=W)
    paisTitulo.grid(row=6, column=0, sticky=W)
    paisEntrada.grid(row=6, column=1, sticky=W)
    estadoTitulo.grid(row=7,column=0,sticky=W)
    estadoEntrada.grid(row=7,column=1,sticky=W)
    insertar.grid(row=12, column=0, sticky=E, pady=15)
    insertar.config(width=15, height=2)
    botonRegresarPequeño.config(width=15, height=2)
    botonRegresarPequeño.grid(row=12, column=2, sticky=E,pady=15)
    pais.set(generarPais(paises))
    estado.set('Activo')
    titulo.grid_remove()
    cargarBD.grid_remove()
    insertarPart.grid_remove()
    insertarNPart.grid_remove()
    modificar.grid_remove()
    eliminar.grid_remove()
    xml.grid_remove()
    reportes.grid_remove()
    salir.grid_remove()



#Botones Ventana Principal
titulo=Label(ventana, text="Personalidades", font=("Imprint MT Shadow", 40),bg='#FCF8E8')
cargarBD=Button(ventana, text="Cargar Bases de Datos",height=3, width=65,font=("Arial",12), bd=5,bg='#94B49F',command=lambda:[cargarBaseDatosPaises(), cargarBaseDatosPerso()])
insertarPart = Button(ventana, text="Insertar un participante",height=2, width=65,font=("Arial",12),bd=5, bg='#94B49F',command=ventanaAnhadirPart,state=DISABLED)
insertarNPart = Button(ventana, text="Insertar N participantes",height=2, width=65,font=("Arial",12),bd=5,bg='#94B49F', state=DISABLED)
modificar= Button(ventana, text="Modificar Participante",height=2, width=65,font=("Arial",12),bd=5, bg='#ECB390',state=DISABLED,)
eliminar = Button(ventana, text="Eliminar Datos de una Persona",height=2, width=65,font=("Arial",12),bd=5, bg='#ECB390',state=DISABLED)
xml= Button(ventana, text="Crear XML",height=2, width=65,font=("Arial",12),bd=5, bg='#ECB390',state=DISABLED,)
reportes = Button(ventana, text="Reportes",height=2, width=65,font=("Arial",12),bd=5,bg='#DF7861',state=DISABLED)
salir = Button(ventana, text="Salir",height=2, width=65,font=("Arial",12),bd=5,bg='#DF7861', command=ventana.quit)


#Botones para insertar Participante
cedula = StringVar()
nombre = StringVar()
genero = BooleanVar()
personalidadCaja=StringVar()   #Estaba embaixo
pais=StringVar()
estado= StringVar()


#Insertar Participante
def insertarParti():
    """
    Funcionamiento: Inserta un participante
    Entrada: N/D
    Salida: Inserta participante
    """
    cedulaA = cedula.get()
    nombreA = nombre.get()
    generoA= genero.get()
    paisA = pais.get()
    if validarCedula(cedulaA):
        if validarNombre(nombreA):
            persona=Persona(cedulaA,nombreA,generoA,paisA)
            persona.asignarPersonalidad(personalidadCaja.get())
            baseDeDatos.append(persona)
            print(persona.getCedula())
            print(persona.getNombre())
            print(persona.getGenero())
            print(persona.getPais())
            print(persona.getPersonalidad())
            print(persona.getEstado())
            mb.showinfo("Participante Insertado", "Se realizó el ingreso del participante satisfactoriamente.")
        else:
            mb.showinfo("Nombre Incorrecto", "El formato del nombre debe empezar con el nombre, un espacio, el primer apelido seguido del segundo con un guión\nEjemplo: Ana Li-Fuentes")    
    else:
        mb.showinfo("Formato de Cédula Incorrecto", "El formato debe de ser de la forma: #-####-####")
    return ventanaPrincipal()

tituloAñadir = Label(ventana, text="Insertar un participante", font=("Times", 20),bg='#FCF8E8')
cedulaTitulo = Label(ventana, text="Cédula")
cedulaEntrada = Entry(ventana, textvariable=cedula)
nombreTitulo = Label(ventana, text="Nombre")
nombreEntrada = Entry(ventana, textvariable=nombre)
generotitulo = Label(ventana, text="Genero")
generoM = Radiobutton(ventana, text='Masculino', value=True, variable=genero)
generoF = Radiobutton(ventana, text="Femenino", value=False, variable=genero)
personalidadTitulo = Label(ventana, text="Tipo de Personalidad")
opciones=generarPerso(cargarBaseDatosPerso())
personalidadEntrada = Combobox(ventana, state='readonly',values=[opciones[0],opciones[1],opciones[2],opciones[3],opciones[4],
opciones[5],opciones[6],opciones[7],opciones[8],opciones[9],opciones[10],opciones[11],opciones[12],opciones[13],opciones[14],
opciones[15]],textvariable=personalidadCaja)
paisTitulo = Label(ventana, text="Pais")
paisEntrada = Entry(ventana,state=DISABLED, textvariable=pais)
estadoTitulo = Label(ventana, text="Estado")
estadoEntrada=Entry(ventana,state=DISABLED,textvariable=estado)
insertar = Button(ventana, text="Insertar", command=insertarParti)
    #clean = Button(ventana, text="Limpiar", command=limpiar)
botonRegresarPequeño = Button(ventana, text="Regresar", command=ventanaPrincipal, width=12, height=2)
#Botones añadir Participante
def clean():
    cedula.set('')
    nombre.set('')
    genero.set(True)
    personalidadCaja.set('')
    estado.set('')

ventanaPrincipal()
ventana.mainloop()