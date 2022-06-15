#################################
#Elaborado por: Marbel Brenes y Samuel Garces
#Fecha de creación: 05/06/2022 15:35 p.m
#Última Modificación: 17/06/22 11:00 p.m
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
retirados=[]
cedulas=[]

#Ventana Principal
ventana = Tk()
ventana.resizable(0,0)
ventana.title("Tarea Porgramada Tres Marbel y Samuel")

#Función Para Limpiar
def clean():
    cedula.set('')
    nombre.set('')
    genero.set(True)
    personalidadCaja.set('')
    estado.set('')
    cantidad.set('')

#Cargar Bases de Datos
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

    #Ocultar Botones de Personas

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
    #Ocultar Botones de N Personas
    tituloAñadirN.grid_remove()
    cantidadLabel.grid_remove()
    cantidadEntrada.grid_remove()
    insertarBotonN.grid_remove()
    limpiarBotonN.grid_remove()
    
    #Ocultar Botones de Eliminar Personas
    tituloEliminar.grid_remove()
    solititarCedula.grid_remove()
    eliminarBoton.grid_remove()
    confirmarBoton.grid_remove()
    cedulaEntradaE.grid_remove()

#Ventana Añadir Participantes
def ventanaAnhadirPersona():
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
    
#Insertar Participante - Función
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
    persoA = personalidadCaja.get()
    if validarCedula(cedulaA):
        if validarNombre(nombreA):
            persona=Persona(cedulaA,nombreA,generoA,paisA,persoA) #Hacer función alambrada con las personalidades
            baseDeDatos.append(persona)
            print(persona.getCedula())
            print(persona.getNombre())
            print(persona.getGenero())
            print(persona.getPais())
            print(persona.getPersonalidad())
            print(persona.getEstado())
            mb.showinfo("PPersona Incertada", "Se realizó el ingreso del participante satisfactoriamente.")
        else:
            mb.showinfo("Nombre Incorrecto", "El formato del nombre debe empezar con el nombre, un espacio, el primer apelido seguido del segundo con un guión\nEjemplo: Ana Li-Fuentes")    
    else:
        mb.showinfo("Formato de Cédula Incorrecto", "El formato debe de ser de la forma: #-####-####")
    return ventanaPrincipal()

#Insertar  N  Paersonas
def ventanaAnhadirNPersonas():
    """
    Funcionamiento: Crea la ventanta para añadir n participantes
    Entrada: N/D
    Salida: Ventanta para añadir n participantes
    """
    ventana.geometry("400x120")
    tituloAñadirN.grid(row=0, column=0, sticky=W, columnspan=2)
    cantidadLabel.grid(row=1, column=0)
    cantidadEntrada.grid(row=1, column=1)
    insertarBotonN.config(width=12, height=2)
    insertarBotonN.grid(row=2, column=0, sticky=E, pady=15)
    limpiarBotonN.config(width=12, height=2)
    limpiarBotonN.grid(row=2, column=1, pady=15)
    botonRegresarPequeño.grid(row=2, column=2, sticky=E, pady=15)

    #Ocultar botones de ventana principal
    titulo.grid_remove()
    cargarBD.grid_remove()
    insertarPart.grid_remove()
    insertarNPart.grid_remove()
    modificar.grid_remove()
    eliminar.grid_remove()
    xml.grid_remove()
    reportes.grid_remove()
    salir.grid_remove()

def anhadirNPersonas():
    """
    Funcionamiento: Inserta N personas creadas
    Entrada: N/D
    Salida: Inserta participantes
    """
    if validarCantidad(cantidad.get()):
        mb.showinfo("Personas Registradas", "Los participantes se crearon satisfactoriamente.")
        return ventanaAnhadirNPersonas()
    else:
        clean()
        mb.showerror('Caracter Incorrecto',"Ingrese únicamente valores numéricos mayores o iguales a 25.")
        return ventanaAnhadirNPersonas()

#Eliminar los datos de una persona
def ventanaModificarAux():
    """
    Funcionamiento: Crea la ventanta para escribir el motivo de darse de baja
    Entrada: N/D
    Salida: Ventanta para escribir motivo
    """
    if validarCedula(cedula.get()):
        if not validarEnCedulas(cedula.get()):
            ventana.geometry("600x420")
            print('a')
        else:
            mb.showinfo("Cédula desconocida", "La cédula no se encuentra en la base de datos.")
            return ventanaModificarAux()
    else:
        mb.showerror("Formato Incorrecto", "Ingrese la cédula con el formato de la forma: #-####-####")
        return ventanaModificarAux()
        
def eliminarPersona():
    """
    Funcionamiento: Elimina una persona de la BD
    Entrada: N/D
    Salida: 
    """

def confirmarEliminar():
    """
    Funcionamiento: Pide una confirmación antes de eliminar a una persona de la BD
    Entrada: N/D
    Salida: 
    """
    'cedulaA = cedula.get()'
    ventanaModificarAux()
    

    ventana.geometry("400x320")
    confirmarBoton.config(width=12, height=2)
    confirmarBoton.grid(row=6, column=0, sticky=E, pady=15)
    solititarJustificacion.grid(row=4, column=0, sticky=W)

   #Ocultar botones de Eliminar Persona
    solititarCedula.grid_remove()
    cedulaEntrada.grid_remove()
    eliminarBoton.grid_remove()

def ventanaEliminarPersona():
    """
    Funcionamiento: Crea la ventanta para eliminar una persona de la BD
    Entrada: N/D
    Salida: 
    """
    ventana.geometry("400x320")
    tituloEliminar.grid(row=0, column=0, sticky=W, columnspan=2)
    solititarCedula.grid(row=4, column=0, sticky=W)
    cedulaEntrada.grid(row=4, column=1, sticky=W)
    eliminarBoton.config(width=12, height=2)
    eliminarBoton.grid(row=6, column=0, sticky=E, pady=15)
    limpiarBotonN.config(width=12, height=2)
    limpiarBotonN.grid(row=6, column=1, pady=15)
    botonRegresarPequeño.grid(row=6, column=2, sticky=E, pady=15)

    #Ocultar botones de ventana principal
    titulo.grid_remove()
    cargarBD.grid_remove()
    insertarPart.grid_remove()
    insertarNPart.grid_remove()
    modificar.grid_remove()
    eliminar.grid_remove()
    xml.grid_remove()
    reportes.grid_remove()
    salir.grid_remove()
    confirmarBoton.grid_remove()

#Botones Ventana Principal
titulo=Label(ventana, text="Personalidades", font=("Imprint MT Shadow", 40),bg='#FCF8E8')
cargarBD=Button(ventana, text="Cargar Bases de Datos",height=3, width=65,font=("Arial",12), bd=5,bg='#94B49F',command=lambda:[cargarBaseDatosPaises(), cargarBaseDatosPerso()])
insertarPart = Button(ventana, text="Insertar un participante",height=2, width=65,font=("Arial",12),bd=5, bg='#94B49F',command=ventanaAnhadirPersona,state=DISABLED)
insertarNPart = Button(ventana, text="Insertar N participantes",height=2, width=65,font=("Arial",12),bd=5,bg='#94B49F', command=ventanaAnhadirNPersonas,state=DISABLED)
modificar= Button(ventana, text="Modificar Participante",height=2, width=65,font=("Arial",12),bd=5, bg='#ECB390',state=DISABLED,)
eliminar = Button(ventana, text="Eliminar Datos de una Persona",height=2, width=65,font=("Arial",12),bd=5, bg='#ECB390', command=ventanaEliminarPersona,state=DISABLED)
xml= Button(ventana, text="Crear XML",height=2, width=65,font=("Arial",12),bd=5, bg='#ECB390',state=DISABLED,)
reportes = Button(ventana, text="Reportes",height=2, width=65,font=("Arial",12),bd=5,bg='#DF7861',state=DISABLED)
salir = Button(ventana, text="Salir",height=2, width=65,font=("Arial",12),bd=5,bg='#DF7861', command=ventana.quit)

#Botones para insertar Participante
cedula = StringVar()
nombre = StringVar()
genero = BooleanVar()
personalidadCaja=StringVar()  
pais=StringVar()
estado= StringVar()

####Botones Añadir Participante
tituloAñadir = Label(ventana, text="Insertar una persona", font=("Times", 20),bg='#FCF8E8')
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
botonRegresarPequeño = Button(ventana, text="Regresar", command=ventanaPrincipal, width=12, height=2)

#Botones Añadir  N  Personas
tituloAñadirN = Label(ventana, text="Insertar N Personas", font=("Times", 20))
cantidadLabel = Label(ventana, text="Cantidad a generar")
cantidad = StringVar()
cantidadEntrada = Entry(ventana, textvariable=cantidad)
insertarBotonN = Button(ventana, text="Insertar", command=anhadirNPersonas)
limpiarBotonN = Button(ventana, text="Limpiar", command=clean)

#Botones Eliminar Datos Persona
tituloEliminar = Label(ventana, text="Eliminando Persona", font=("Times", 20))
solititarCedula = Label(ventana, text="Digite una cédula: ")
cedulaEntradaE = Entry(ventana, textvariable=cedula)
eliminarBoton = Button(ventana, text="Eliminar", command=confirmarEliminar)
solititarJustificacion = Label(ventana, text="Justifique: ")
confirmarBoton = Button(ventana, text="Confirmar", command=eliminarPersona)











































#Función para Limpiar










#PP
ventanaPrincipal()
ventana.mainloop()
