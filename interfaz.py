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
import xml.etree.cElementTree as ET
#Bases de Datos

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
    cedulaCod.set('')
    nuevaPersoAux.set('')
    cedulaEli.set("")
    motivo.set("")


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
        xml.config(state=ACTIVE)

    return personalidades

#Frame Principal
def ventanaPrincipal():
    """
    Funcionamiento: Crea la ventanta principal
    Entrada: N/D
    Salida: Ventana principal
    """
    global baseDeDatos
    baseDeDatos= leerArchivo("BaseDatos")
    for persona in baseDeDatos:
        cedulas.append(persona.getCedula())
    #for i in baseDeDatos:
        #print(i.getAll())
       #Para revisar que se guarda en memoria secundaria
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
        reportes.config(state=ACTIVE)
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
    botonRegresarPequeño.grid_remove()


    #Ocultar Botones Modificar
    tituloModificar.grid_remove()
    cedulaCodTitulo.grid_remove()
    cedulaCodEntrada.grid_remove()
    InsertarBoton.grid_remove()
    limpiarBoton.grid_remove()
    regresarBoton.grid_remove()

    #Ocultar Botones Modificar Aux
    modificarTitulo.grid_remove()
    cedulaAuxTitulo.grid_remove()
    cedulaAuxEntrada.grid_remove()
    nombreAuxTitulo.grid_remove()
    nombreAuxEntrada.grid_remove()
    personalidadAuxTitulo.grid_remove()
    personalidadAuxEntrada.grid_remove()
    persoListaAuxTitulo.grid_remove()
    persoListaAux.grid_remove()
    insertarModAux.grid_remove()

    #Ocultar Botones Eliminar
    eliminarTitulo.grid_remove()
    cedulaEliTitulo.grid_remove()
    cedulaEliEntrada.grid_remove()
    motivoTitulo.grid_remove()
    motivoEntrada.grid_remove()
    ingresarMotivo.grid_remove()
    limpiarMotivo.grid_remove()
    regresarMotivo.grid_remove()
    ingresarMotivoAux.grid_remove()
    #Ocultar Botones de Reportes
    tituloReportes.grid_remove()
    reportePersonalidad.grid_remove()
    reporteTipo.grid_remove()
    reportePersona.grid_remove()
    reporteBDBoton.grid_remove()
    reporteRetiradosBoton.grid_remove()
    reportePorPaisBoton.grid_remove()
#Ventana Añadir Participantes

def ventanaAnhadirPersona():
    ventana.geometry("375x250")
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
    insertar.grid(row=10, column=0)
    insertar.config(width=15, height=2)
    limpiarBotonN.config(width=15, height=2)
    limpiarBotonN.grid(row=10, column=1)
    botonRegresarPequeño.config(width=15, height=2)
    botonRegresarPequeño.grid(row=10, column=2)
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
    paisA = traducirPais(str(pais.get()))
    persoA = obtenerPersonalidad(personalidadCaja.get())
    if validarCedula(cedulaA):
        if validarEnCedulas(cedulaA):
            if validarNombre(nombreA):
                cedulas.append(cedulaA)
                persona=Persona() 
                persona.asignarCedula(cedulaA)
                persona.asignarNombre(nombreA)
                persona.asignarGenero(generoA)
                persona.asignarPais(paisA)
                persona.asignarPersonalidad(persoA)
                print(persona.getAll())
                baseDeDatos.append(persona)
                graba('BaseDatos',baseDeDatos)
                mb.showinfo("Persona Incertada", "Se realizó el ingreso del participante satisfactoriamente.")
            else:
               mb.showinfo("Nombre Incorrecto", "El formato del nombre debe empezar con el nombre, un espacio, el primer apelido seguido del segundo con un guión\nEjemplo: Ana Li-Fuentes")    
        else:
            mb.showinfo("Cédula ya registrada", "La cédula ya se encuentra registrada\nIngrese una nueva cédula.")
    else:
        mb.showinfo("Formato de Cédula Incorrecto", "Ingrese la cédula con el formato de la forma: #-####-####")
    return ventanaPrincipal()

#Insertar  N  Personas
def ventanaAnhadirNPersonas():
    """
    Funcionamiento: Crea la ventanta para añadir n participantes
    Entrada: N/D
    Salida: Ventanta para añadir n participantes
    """
    ventana.geometry("350x120")
    tituloAñadirN.grid(row=0, column=0, sticky=W, columnspan=2)
    cantidadLabel.grid(row=1, column=0)
    cantidadEntrada.grid(row=1, column=1)
    insertarBotonN.config(width=12, height=2)
    insertarBotonN.grid(row=2, column=0, sticky=E, pady=15)
    limpiarBotonN.config(width=12, height=2)
    limpiarBotonN.grid(row=2, column=1, pady=15)
    botonRegresarPequeño.grid(row=2, column=2, pady=15)

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


#N personas Función
def anhadirNProceso(cant):
    i=0
    while i!=int(cant):
        cedulaN=generarCedulasRandom()
        nombreN=generarNombresRandom()
        generoN=bool(random.getrandbits(1))
        paisN=generarPaisRandom()
        personalidadN=generarPersoRandom()
        personaN=Persona()
        personaN.asignarCedula(cedulaN)
        personaN.asignarNombre(nombreN)
        personaN.asignarGenero(generoN)
        personaN.asignarPais(paisN)
        personaN.asignarPersonalidad(personalidadN)
        baseDeDatos.append(personaN)
        print(personaN.getAll())
        graba('BaseDatos',baseDeDatos)
        i+=1
    return baseDeDatos

def anhadirNPersonas():
    """
    Funcionamiento: Inserta N personas creadas
    Entrada: N/D
    Salida: Inserta participantes
    """
    if validarCantidad(cantidad.get()):
        mb.showinfo("Personas Registradas", "Los participantes se crearon satisfactoriamente.")
        cantidadN=cantidad.get()
        anhadirNProceso(cantidadN)
        return ventanaPrincipal()
    else:
        clean()
        mb.showerror('Caracter Incorrecto',"Ingrese únicamente valores numéricos mayores o iguales a 25.")
        return ventanaAnhadirNPersonas()

def ventanaModificarDatos():
    """
    Funcionamiento: Crea la ventanta para darse de baja
    Entrada: N/D
    Salida: Ventanta para darse de baja
    """
    ventana.geometry("420x120")
    tituloModificar.grid(row=0, column=1)
    cedulaCodTitulo.grid(row=1, column=0)
    cedulaCodEntrada.grid(row=1, column=1)
    InsertarBoton.config(width=12, height=2)
    InsertarBoton.grid(row=2, column=0, sticky=E, pady=10)
    limpiarBoton.config(width=12, height=2)
    limpiarBoton.grid(row=2, column=1, pady=10)
    regresarBoton.config(width=12, height=2)
    regresarBoton.grid(row=2, column=2, pady=10)
    
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
    botonRegresarPequeño.grid_remove()
    insertar.grid_remove()
    #Ocultar Botones Modificar Aux
    modificarTitulo.grid_remove()
    cedulaAuxTitulo.grid_remove()
    cedulaAuxEntrada.grid_remove()
    nombreAuxTitulo.grid_remove()
    nombreAuxEntrada.grid_remove()
    personalidadAuxTitulo.grid_remove()
    personalidadAuxEntrada.grid_remove()
    persoListaAuxTitulo.grid_remove()
    persoListaAux.grid_remove()
    insertarModAux.grid_remove()

def ventanaModificarAux():
    """
    Funcionamiento: Crea la ventanta para escribir el motivo de darse de baja
    Entrada: N/D
    Salida: Ventanta para escribir motivo
    """
    if validarCedula(cedulaCod.get()):
        if not validarEnCedulas(cedulaCod.get()): #Que si está en cédulas
            ventana.geometry("400x250")
            modificarTitulo.grid(row=0, column=0, sticky=W, columnspan=2)
            cedulaAuxTitulo.grid(row=1, column=0)
            cedulaAuxEntrada.grid(row=1, column=1)
            nombreAuxTitulo.grid(row=2, column=0)
            nombreAuxEntrada.grid(row=2, column=1)
            personalidadAuxTitulo.grid(row=3, column=0)
            personalidadAuxEntrada.grid(row=3, column=1, pady=15)
            persoListaAuxTitulo.grid(row=4, column=0, sticky=E, pady=15)
            persoListaAux.grid(row=4, column=1, sticky=E, pady=15)
            insertarModAux.config(width=12, height=2)
            insertarModAux.grid(row=8,column=0, pady=15)
            limpiarBoton.grid(row=8,column=1, pady=15)
            limpiarBoton.config(width=12, height=2)
            botonRegresarPequeño.grid(row=8,column=2, pady=15)
            botonRegresarPequeño.config(width=12, height=2)
            for persona in baseDeDatos:
                if persona.getCedula()==cedulaCod.get():
                    cedulaAux.set(persona.getCedula())
                    nombreAux.set(persona.getNombre())
                    personalidadAux.set(traducirPersonalidad(persona.getPersonalidad()))
                    
            #Ocultar Botones de Modificar Principal
            tituloModificar.grid_remove()
            cedulaCodTitulo.grid_remove()
            cedulaCodEntrada.grid_remove()
            InsertarBoton.grid_remove()
            regresarBoton.grid_remove()
        else:
            mb.showinfo("Cédula desconocida", "La cédula no se encuentra en la base de datos.")
            return ventanaPrincipal()
    else:
        mb.showerror("Formato Incorrecto", "Ingrese la cédula con el formato de la forma: #-####-####")
        return ventanaPrincipal()
#Modificar Función
def modificarPersonalidad():
    personalidadNueva=nuevaPersoAux.get()
    cedula=cedulaCod.get()
    if mb.askyesno("Confirmación", "¿Está seguro?"):
        for persona in baseDeDatos:
            if persona.getCedula()==cedula:
                print(persona.getAll())
                persona.asignarPersonalidad(obtenerPersonalidad(personalidadNueva))
                graba('BaseDatos',baseDeDatos)
                print(persona.getAll()) #Respaldar en Memoria Secundaria
        mb.showinfo("Éxito", "Se modificaró la personalidad de la persona.")
    else:
        mb.showinfo("Cancelado", "No se modificaró la personalidad de la persona.")
    return ventanaPrincipal()
    
        
def mostrarModificarDatos():
    for persona in baseDeDatos:
        if persona.getCedula()==cedulaCod.get():
            if not persona.getPersonalidad()==obtenerPersonalidad(nuevaPersoAux.get()):
                modificarPersonalidad()
                graba('BaseDatos',baseDeDatos)
                return ventanaPrincipal()
            else:
                mb.showerror('Error',"Esta persona ya cuenta con esa personalidad.")
                return ventanaPrincipal()

def ventanaEliminar():
    ventana.geometry("320x120")
    eliminarTitulo.grid(row=0,column=0,sticky=W, columnspan=2)
    cedulaEliTitulo.grid(row=2, column=0)
    cedulaEliEntrada.grid(row=2, column=1)
    limpiarMotivo.config(width=12, height=2)
    limpiarMotivo.grid(row=3, column=1, pady=10)
    ingresarMotivo.grid(row=3, column=0, pady=10)
    ingresarMotivo.config(width=12, height=2)
    regresarMotivo.grid(row=3, column=2, pady=10)
    regresarMotivo.config(width=12, height=2)
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
    botonRegresarPequeño.grid_remove()
    insertar.grid_remove()
    #Ocultar Botones Eliminar Auxiliar
    ingresarMotivoAux.grid_remove()

def ventanaEliminarAux():
    if validarCedula(cedulaEli.get()):
        if not validarEnCedulas(cedulaEli.get()):
            ventana.geometry("320x140")
            eliminarTitulo.grid(row=0,column=0,sticky=W, columnspan=2)
            motivoTitulo.grid(row=1, column=0, pady=10)
            motivoEntrada.grid(row=1, column=1, pady=10)
            ingresarMotivoAux.config(width=12, height=2)
            ingresarMotivoAux.grid(row=2, column=0)
            limpiarMotivo.config(width=12, height=2)
            limpiarMotivo.grid(row=2, column=1)
            regresarMotivo.config(width=12, height=2)
            regresarMotivo.grid(row=2, column=2)

            #Ocultar Botones Eliminar Principal)
            cedulaEliTitulo.grid_remove()
            cedulaEliEntrada.grid_remove()
            ingresarMotivo.grid_remove()
        else:
            mb.showinfo("Cédula desconocida", "La cédula no se encuentra en la base de datos.")
            return ventanaPrincipal()
    else:
        mb.showerror("Formato Incorrecto", "Ingrese la cédula con el formato de la forma: #-####-####")
        return ventanaPrincipal()

def eliminarPersona():
    cedulaE = cedulaEli.get()
    motivoE = motivo.get()
    fecha = fechaActual()
    if mb.askyesno("Confirmación", "¿Está seguro?"):
        for persona in baseDeDatos:
            if persona.getCedula()==cedulaE:
                persona.asignarEstado(motivoE,fecha)
                print(persona.getEstado())
                print(persona.getAll())
                graba('BaseDatos',baseDeDatos)
        mb.showinfo("Éxcito", "Se le eliminó de la base de datos exitosamente.")
    else:
        mb.showinfo("Cancelado", "No se realizó el proceso de eliminarlo de la base de datos.")
    return ventanaPrincipal()
    












#Reportes Samuel
def crearXML():
    """
    Funcionamiento: Crea un archivo XML con los datos del diccionario de personalidades
    Entrada: N/D
    Salida: mensaje(showinfo)
    """
    subtipo=codigo=''
    contA=1
    aux=[]
    try:
        personalidad = ET.Element("personalidades")
        for i in personalidades:
            tipo = ET.SubElement(personalidad,i)
            aux = personalidades.get(i)
            for j in aux:
                subtipo=j[0]
                codigo=j[1]       
                ET.SubElement(tipo, "subtipo"+str(contA)).text = subtipo
                ET.SubElement(tipo, "codigo"+str(contA)).text = codigo
            contA+=1
        arbol = ET.ElementTree(personalidad)
        arbol.write("PersonalidadesXML.xml")
        mb.showinfo("Información", "Los datos de las Personalidades han sido guardadas en 'PersonalidadesXML.xml' ")
    except:
        mb.showinfo("ERROR", "No se pudo crear el archivo XML de las Personalidades")
    
#Reportes
def ventanaReportes():
    """
    Funcionamiento: Ventana donde se ubican todos los reportes
    Entrada: N/D
    Salida: N/D
    """
    ventana.geometry("650x650")
    ventana['bg']='#FCF8E8'
    tituloReportes.grid(row=0, column=0, pady=20)
    reportePersonalidad.grid(row=1, column=0, padx=15, pady=15) 
    reporteTipo.grid(row=2, column=0, padx=15) 
    reportePersona.grid(row=3, column=0, padx=15, pady=15)
    reporteBDBoton.grid(row=4, column=0, padx=15)
    reporteRetiradosBoton.grid(row=5, column=0, padx=15, pady=15)
    reportePorPaisBoton.grid(row=6, column=0, padx=20)
    botonRegresarPequeño.config(width=15, height=2)
    botonRegresarPequeño.grid(row=7, column=0, pady=15)
    
    
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
    #Botones ReporteTipos
    tituloReporteTipos.grid_remove()
    selecccionarTipo.grid_remove()
    tipoCombobox.grid_remove()
    generarBotonTipos.grid_remove()
    limpiarBotonN.grid_remove()
    regresarReportes.grid_remove()
    #Botones ReportePersona
    tituloReportePersona.grid_remove()
    introducirCedula.grid_remove()
    generarBotonPersona.grid_remove()

def generarHtmlPersonalidades():
    """
    Funcionamiento: Crea el archivo HTML para ReportePersonalidades   
    Entrada: N/D   
    Salida: N/D
    """
    tabla=""
    nombreArchivo = "personalidades-"+fechaYHoraActual()+".html"
    f = open(nombreArchivo,'w')
    tipAux = generarTipos(personalidades)

    mensajeInicio = "<html><head></head><body><h1>"      
    titulo = "Reporte Personalidades"
    mensajeMedio="</h1>"
    tabla+= "<table width='100%' border='1'><tbody><tr style='background-color: rgb(255, 127, 0);'>"

    #Crea los encabezados agarrando las llaves del diccionario
    for n in tipAux:
        encabezadosTabla1="<th colspan='2'>"
        tabla+= encabezadosTabla1+str(n)
        encabezadosTabla2="</th>"
        tabla+= encabezadosTabla2
    tabla+="</tr><tr>"

    #Crea las celdas con la información
    for m in personalidades:
        contenidotabla1="<td colspan='2' style='background-color: rgb(102, 255, 153);'>"
        tabla+= contenidotabla1+str(personalidades[m])
        contenidotabla2="</td>"
        tabla+=contenidotabla2

    tabla+="</tr></table></tbody>"
    mensajeFinal = "</body></html>"

    mensajeCompleto = mensajeInicio + titulo + mensajeMedio + tabla + mensajeFinal
    f.write(mensajeCompleto)
    f.close()
    return ''

def reportePersonalidades():
    """
    Funcionamiento: Crea un archivo HTML donde imprime un reporte del diccionario personalidades
    Entrada: N/D
    Salida: showinfo (mensaje)
    """
    try:
        generarHtmlPersonalidades()
        return mb.showinfo("Información", "Archivo 'PersonalidadesHTML' de tipo html ha sido creado")
    except:
        return mb.showinfo("Error", "El archivo HTML NO ha podido ser creado")

def generarHtmlTipo():
    """
    Funcionamiento: Crea el archivo HTML para ReporteTipos
    Entrada: N/D
    Salida:N/D
    """
    print(baseDeDatos)
    tabla=""
    BDactiva=[]
    nombreArchivo = "tipos-"+fechaYHoraActual()+".html"
    f = open(nombreArchivo,'w')
    tipoSeleccionado = tipoCombobox.get()

    for a in baseDeDatos:
        estatus = a.getEstado()
        subtype = traducirPersonalidadSi(a.getPersonalidad())
        for n in personalidades:
            aux=0
            if n == tipoSeleccionado:
                valor = personalidades[n]
                for j in valor:
                    if j[0]==subtype and estatus[0]==True:
                        BDactiva.append(a)
                    aux+=1

    mensajeInicio = "<html><head></head><body><h1>"      
    titulo = "Reporte Tipo "+tipoSeleccionado
    mensajeMedio="</h1>"
    tabla+= "<table width='100%' border='1'><tbody><tr style='background-color: rgb(255, 127, 0);'>"

    #Crea los encabezados agarrando las llaves del diccionario
    for n in range(5):
        encabezadosTabla1="<th colspan='2'>"
        if n==0:
            tabla+= encabezadosTabla1+"Cedula"
        elif n==1:
            tabla+= encabezadosTabla1+"Nombre"
        elif n==2:
            tabla+= encabezadosTabla1+"Genero"
        elif n==3:
            tabla+= encabezadosTabla1+"Subtipo"
        else:
            tabla+= encabezadosTabla1+"Pais"
        encabezadosTabla2="</th>"
        tabla+= encabezadosTabla2
    tabla+="</tr>"
    cont=0
    #Crea las celdas con la información
    for m in BDactiva:
        if esPar(cont):
            tabla+="<tr style='background-color: rgb(102, 255, 153);'>"
        else:
            tabla+="<tr style='background-color: rgb(255, 127, 0);'>"
        for dato in range(5):
            contenidotabla1="<td  colspan='2' >"
            if dato==0:
                tabla+= contenidotabla1+str(m.getCedula()) 
            elif dato==1:
                tabla+= contenidotabla1+str(m.getNombre()) 
            elif dato==2:
                tabla+= contenidotabla1+str(m.getGenero()) 
            elif dato==3:
                tabla+= contenidotabla1+str(m.getPersonalidad()) 
            else:
                tabla+= contenidotabla1+str(m.getPais()) 
            tabla+="</td>"
        cont+=1
        tabla+="</tr>"

    tabla+="</tr></table></tbody>"
    mensajeFinal = "</body></html>"

    mensajeCompleto = mensajeInicio + titulo + mensajeMedio + tabla + mensajeFinal
    f.write(mensajeCompleto)
    f.close()
    return ''

def generarReporteTipo():
    """
    Funcionamiento: Crea un archivo HTML con los datos especificados
    Entrada: N/D
    Salida: showinfo(mensaje)
    """
    try:
        if tipoCombobox.get() == "":
            return mb.showinfo("Error", "Debe elegir una opción antes de crear el archivo HTML")
        generarHtmlTipo()
        return mb.showinfo("Información", "Archivo 'PersonalidadesHTML' de tipo html ha sido creado")
    except:
        return mb.showinfo("Error", "El archivo HTML NO ha podido ser creado")

def reporteTipoPersonalidad():
    """
    Funcionamiento: Crea una ventana para elegir un tipo de personalidad y crear un archivo HTML
    Entrada: N/D
    Salida: N/D
    """
    ventana.geometry("400x120")
    tituloReporteTipos.grid(row=0, column=0, sticky=W, columnspan=2)
    selecccionarTipo.grid(row=1, column=0)
    tipoCombobox.grid(row=1, column=1)
    generarBotonTipos.config(width=12, height=2)
    generarBotonTipos.grid(row=2, column=0, sticky=E, pady=15)
    limpiarBotonN.config(width=12, height=2)
    limpiarBotonN.grid(row=2, column=1, pady=15)
    regresarReportes.grid(row=2, column=2, sticky=E, pady=15)
    
    #Ocultar botones 
    tituloReportes.grid_remove()
    reportePersonalidad.grid_remove()
    reporteTipo.grid_remove()
    reportePersona.grid_remove()
    reporteBDBoton.grid_remove()
    reporteRetiradosBoton.grid_remove()
    reportePorPaisBoton.grid_remove()
    botonRegresarPequeño.grid_remove()

def generarHtmlPersona():
    """
    Funcionamiento: Crea el archivo HTML para ReportePersonas
    Entrada: N/D
    Salida: N/D
    """
    tabla=""
    nombreArchivo = "persona-"+fechaYHoraActual()+".html"
    f = open(nombreArchivo,'w')
    personaBuscar = cedula.get()

    for a in baseDeDatos:
        ced = a.getCedula()
        if ced==personaBuscar:
            personaA = a

    mensajeInicio = "<html><head></head><body><h1>"      
    titulo = "Reporte de Persona"
    mensajeMedio="</h1>"
    tabla+= "<table width='100%' border='1'><tbody><tr style='background-color: rgb(255, 127, 0);'>"

    #Crea los encabezados agarrando las llaves del diccionario
    for n in range(5):
        encabezadosTabla1="<th colspan='2'>"
        if n==0:
            tabla+= encabezadosTabla1+"Cedula"
        elif n==1:
            tabla+= encabezadosTabla1+"Nombre"
        elif n==2:
            tabla+= encabezadosTabla1+"Genero"
        elif n==3:
            tabla+= encabezadosTabla1+"Subtipo"
        else:
            tabla+= encabezadosTabla1+"Pais"
        encabezadosTabla2="</th>"
        tabla+= encabezadosTabla2
    tabla+="</tr>"
    #Crea las celdas con la información
    tabla+="<tr style='background-color: rgb(102, 255, 153);'>"
    contenidotabla1="<td  colspan='2' >"
    for m in range(5):
        if m==0:
            tabla+= contenidotabla1+str(personaA.getCedula()) 
        elif m==1:
            tabla+= contenidotabla1+str(personaA.getNombre()) 
        elif m==2:
            tabla+= contenidotabla1+str(traducirGenero(personaA.getGenero()))
        elif m==3:
            tabla+= contenidotabla1+str(traducirPersonalidad(personaA.getPersonalidad()))
        else:
            tabla+= contenidotabla1+str(traducirPaisSTR(personaA.getPais()))
        tabla+="</td>"
    tabla+="</tr>"

    tabla+="</tr></table></tbody>"
    mensajeFinal = "</body></html>"

    mensajeCompleto = mensajeInicio + titulo + mensajeMedio + tabla + mensajeFinal
    f.write(mensajeCompleto)
    f.close()
    return ''

def generarReportePersonas():
    """
    Funcionamiento: Crea un archivo HTML con los datos especificados
    Entrada: N/D
    Salida: showinfo(mensaje)
    """
    cedulas = generarCedulas(baseDeDatos)
    try:
        if cedula.get() == "":
            return mb.showinfo("Error", "Debe digitar una cédula antes de crear el archivo HTML")
        elif validarCedula(cedula.get())==False:
            return mb.showinfo("Error", "Debe digitar un formato de cédula válido antes de crear el archivo HTML")
        for u in cedulas:
            if u==cedula.get():
                generarHtmlPersona()
                return mb.showinfo("Información", "Archivo 'PersonaHTML' de tipo html ha sido creado")
        return mb.showinfo("Error", "La cédula que digitó no se encuentra registrada")
    except:
        return mb.showinfo("Error", "El archivo HTML NO ha podido ser creado")

def reporteInfoPersona():
    """
    Funcionamiento: Crea una ventana donde se solicita la cédula, y si existe crea un archivo HTML con su información
    Entrada: N/D
    Salida: N/D
    """
    ventana.geometry("400x120")
    tituloReportePersona.grid(row=0, column=0, sticky=W, columnspan=2)
    introducirCedula.grid(row=1, column=0)
    cedulaEntrada.grid(row=1, column=1)
    generarBotonPersona.config(width=12, height=2)
    generarBotonPersona.grid(row=2, column=0, sticky=E, pady=15)
    limpiarBotonN.config(width=12, height=2)
    limpiarBotonN.grid(row=2, column=1, pady=15)
    regresarReportes.grid(row=2, column=2, sticky=E, pady=15)

    #Ocultar botones 
    tituloReportes.grid_remove()
    reportePersonalidad.grid_remove()
    reporteTipo.grid_remove()
    reportePersona.grid_remove()
    reporteBDBoton.grid_remove()
    reporteRetiradosBoton.grid_remove()
    reportePorPaisBoton.grid_remove()
    botonRegresarPequeño.grid_remove()

def generarHtmlBD():
    """
    Funcionamiento: Crea el archivo HTML para ReporteBD
    Entrada: N/D
    Salida: N/D
    """
    tabla=""
    nombreArchivo = "basedatos-"+fechaYHoraActual()+".html"
    f = open(nombreArchivo,'w')

    mensajeInicio = "<html><head></head><body><h1>"      
    titulo = "Reporte de la Base de Datos"
    mensajeMedio="</h1>"
    tabla+= "<table width='100%' border='1'><tbody><tr style='background-color: rgb(0, 152, 153);'>"

    #Crea los encabezados agarrando las llaves del diccionario
    for n in range(5):
        encabezadosTabla1="<th colspan='2'>"
        if n==0:
            tabla+= encabezadosTabla1+"Cedula"
        elif n==1:
            tabla+= encabezadosTabla1+"Nombre"
        elif n==2:
            tabla+= encabezadosTabla1+"Genero"
        elif n==3:
            tabla+= encabezadosTabla1+"Subtipo"
        else:
            tabla+= encabezadosTabla1+"Pais"
        encabezadosTabla2="</th>"
        tabla+= encabezadosTabla2
    tabla+="</tr>"

    #Crea las celdas con la información
    cont=0
    for m in baseDeDatos:
        if esPar(cont):
            tabla+="<tr style='background-color: rgb(102, 255, 153);'>"
        else:
            tabla+="<tr style='background-color: rgb(255, 127, 0);'>"
        for dato in range(5):
            contenidotabla1="<td  colspan='2' >"
            if dato==0:
                tabla+= contenidotabla1+str(m.getCedula()) 
            elif dato==1:
                tabla+= contenidotabla1+str(m.getNombre()) 
            elif dato==2:
                tabla+= contenidotabla1+str(traducirGenero(m.getGenero()))
            elif dato==3:
                tabla+= contenidotabla1+str(traducirPersonalidad(m.getPersonalidad()) )
            else:
                tabla+= contenidotabla1+str(traducirPaisSTR(m.getPais()) )
            tabla+="</td>"
        cont+=1
        tabla+="</tr>"

    tabla+="</tr></table></tbody>"
    mensajeFinal = "</body></html>"

    mensajeCompleto = mensajeInicio + titulo + mensajeMedio + tabla + mensajeFinal
    f.write(mensajeCompleto)
    f.close()
    return ''

def reporteBD():
    """
    Funcionamiento: Crea un archivo HTML donde imprime la informacion de cada persona alternando 2 colores por fila
    Entrada: N/D
    Salida: showinfo(mensaje)
    """
    try:
        if baseDeDatos==[]:
            return mb.showinfo("Error", "La Base de Datos debe tener información antes de crear el archivo HTML")
        generarHtmlBD()
        return mb.showinfo("Información", "Archivo 'BaseDatosHTML' de tipo html ha sido creado")
    except:
        return mb.showinfo("Error", "El archivo HTML NO ha podido ser creado")

def generarHtmlRetirados():
    """
    Funcionamiento: Crea el archivo HTML para ReporteRetirados
    Entrada: N/D
    Salida: N/D
    """
    tabla=""
    nombreArchivo = "retirados-"+fechaYHoraActual()+".html"
    f = open(nombreArchivo,'w')

    mensajeInicio = "<html><head></head><body><h1>"      
    titulo = "Reporte de Empleados Retirados"
    mensajeMedio="</h1>"
    tabla+= "<table width='100%' border='1'><tbody><tr style='background-color: rgb(0, 152, 153);'>"

    #Crea los encabezados agarrando las llaves del diccionario
    for n in range(4):
        encabezadosTabla1="<td colspan='2'>"
        if n==0:
            tabla+= encabezadosTabla1+"Cedula"
        elif n==1:
            tabla+= encabezadosTabla1+"Nombre"
        elif n==2:
            tabla+= encabezadosTabla1+"Fecha"
        else:
            tabla+= encabezadosTabla1+"Justificacion"
        encabezadosTabla2="</td>"
        tabla+= encabezadosTabla2
    tabla+="</tr>"

    #Crea las celdas con la información
    cont=0
    for m in retirados:
        if esPar(cont):
            tabla+="<tr style='background-color: rgb(102, 255, 153);'>"
        else:
            tabla+="<tr style='background-color: rgb(255, 127, 0);'>"
        for dato in range(4):
            contenidotabla1="<td  colspan='2' >"
            estadoRetirados = m.getEstado()
            if dato==0:
                tabla+= contenidotabla1+str(m.getCedula()) 
            elif dato==1:
                tabla+= contenidotabla1+str(m.getNombre()) 
            elif dato==2:
                tabla+= contenidotabla1+str(estadoRetirados[2]) 
            else:
                tabla+= contenidotabla1+str(estadoRetirados[1]) 
            tabla+="</td>"
        cont+=1
        tabla+="</tr>"

    tabla+="</tr></table></tbody>"
    mensajeFinal = "</body></html>"

    mensajeCompleto = mensajeInicio + titulo + mensajeMedio + tabla + mensajeFinal
    f.write(mensajeCompleto)
    f.close()
    return ''



def reporteRetirados():
    """
    Funcionamiento: Crea un archivo HTML donde imprime los reportes de las personas retiradas
    Entrada: N/D
    Salida: showinfo(mensaje)
    """
    for persona in baseDeDatos:
        if persona.getEstado()[0]==False:
            retirados.append(persona)
    try:
        if retirados==[]:
            return mb.showinfo("Error", "La Base de Datos debe tener miembros retirados antes de crear el archivo HTML")
        generarHtmlRetirados()
        return mb.showinfo("Información", "Archivo 'RetiradosHTML' de tipo html ha sido creado")
    except:
        return mb.showinfo("Error", "El archivo HTML NO ha podido ser creado")

def generarHtmlPorPais():
    """
    Funcionamiento: Crea el archivo HTML para ReportePorPais
    Entrada: N/D
    Salida: N/D
    """
    print(baseDeDatos)
    tabla=""
    nombreArchivo = "porpais-"+fechaYHoraActual()+".html"
    f = open(nombreArchivo,'w')

    mensajeInicio = "<html><head></head><body><h1>"      
    titulo = "Reporte de la BD por Pais"
    mensajeMedio="</h1>"
    tabla+= "<table width='100%' border='1'><tbody>"
    #Recorre cada pais
    for p in paises:
        for k in baseDeDatos:
            cont=0
            auxPais = traducirPaisSTR(k.getPais())
            if p==auxPais:
                tabla+="<tr> <th colspan='12' style='background-color: rgb(240, 230, 140);'>"+p+"</th> </tr>"
                #Crea los encabezados agarrando las llaves del diccionario
                tabla+="<tr>"
                for n in range(6):
                    encabezadosTabla1="<th colspan='2' style='background-color: rgb(153, 102, 204);'>"
                    if n==0:
                        tabla+= encabezadosTabla1+"Cedula"
                    elif n==1:
                        tabla+= encabezadosTabla1+"Nombre"
                    elif n==2:
                        tabla+= encabezadosTabla1+"Genero"
                    elif n==3:
                        tabla+= encabezadosTabla1+"Subtipo"
                    elif n==4:
                        tabla+= encabezadosTabla1+"Estado"
                    else:
                        tabla+= encabezadosTabla1+"Pais"
                    encabezadosTabla2="</th>"
                    tabla+= encabezadosTabla2
                tabla+="</tr><tr>"
                #Crea las celdas con la información
                estatus = k.getEstado()
                for dato in range(6):
                    if esPar(cont):
                        contenidotabla1="<td  colspan='2' style='background-color: rgb(102, 255, 153);'>"
                    else:
                        contenidotabla1="<td  colspan='2' style='background-color: rgb(255, 127, 0);'>"
                    if dato==0:
                        tabla+= contenidotabla1+str(k.getCedula()) 
                    elif dato==1:
                        tabla+= contenidotabla1+str(k.getNombre()) 
                    elif dato==2:
                        tabla+= contenidotabla1+str(k.getGenero()) 
                    elif dato==3:
                        tabla+= contenidotabla1+str(k.getPersonalidad()) 
                    elif dato==4:
                        tabla+= contenidotabla1+str(estatus[0]) 
                    else:
                        tabla+= contenidotabla1+str(k.getPais()) 
                    tabla+="</td>"
                cont+=1
    tabla+="</tr></table></tbody>"
    mensajeFinal = "</body></html>"

    mensajeCompleto = mensajeInicio + titulo + mensajeMedio + tabla + mensajeFinal
    f.write(mensajeCompleto)
    f.close()
    return ''

def reportePorPais():
    """
    Funcionamiento: Crea un archivo HTML donde imprime los reportes de las personas dividido por paises, activos o no, mostrando su estado
    Entrada: N/D
    Salida: showinfo(mensaje)
    """
    try:
        if baseDeDatos==[]:
            return mb.showinfo("Error", "La Base de Datos debe tener miembros antes de crear el archivo HTML")
        generarHtmlPorPais()
        return mb.showinfo("Información", "Archivo 'PorPaisHTML' de tipo html ha sido creado")
    except:
        return mb.showinfo("Error", "El archivo HTML NO ha podido ser creado")































#Botones Ventana Principal
titulo=Label(ventana, text="Personalidades", font=("Imprint MT Shadow", 40),bg='#FCF8E8')
cargarBD=Button(ventana, text="Cargar Bases de Datos",height=3, width=65,font=("Arial",12), bd=5,bg='#94B49F',command=lambda:[cargarBaseDatosPaises(), cargarBaseDatosPerso()])
insertarPart = Button(ventana, text="Insertar un participante",height=2, width=65,font=("Arial",12),bd=5, bg='#94B49F',command=ventanaAnhadirPersona,state=DISABLED)
insertarNPart = Button(ventana, text="Insertar N participantes",height=2, width=65,font=("Arial",12),bd=5,bg='#94B49F', command=ventanaAnhadirNPersonas,state=DISABLED)
modificar= Button(ventana, text="Modificar Participante",height=2, width=65,font=("Arial",12),bd=5, bg='#ECB390',command=ventanaModificarDatos,state=DISABLED,)
eliminar = Button(ventana, text="Eliminar Datos de una Persona",height=2, width=65,font=("Arial",12),bd=5, bg='#ECB390',state=DISABLED,command=ventanaEliminar)
xml= Button(ventana, text="Crear XML",height=2, width=65,font=("Arial",12),bd=5, bg='#ECB390',command=crearXML,state=DISABLED)
reportes = Button(ventana, text="Reportes",height=2, width=65,font=("Arial",12),bd=5,bg='#DF7861',state=DISABLED,command=ventanaReportes)
salir = Button(ventana, text="Salir",height=2, width=65,font=("Arial",12),bd=5,bg='#DF7861', command=ventana.quit)


#Botones para insertar Participante
cedula = StringVar()
nombre = StringVar()
genero = BooleanVar()
personalidadCaja=StringVar()  
pais=StringVar()
estado= StringVar()
####Botones Añadir Participante
tituloAñadir = Label(ventana, text="Insertar una persona", font=("Imprint MT Shadow", 20),bg='#FCF8E8')
cedulaTitulo = Label(ventana, text="Cédula",bg='#FCF8E8')
cedulaEntrada = Entry(ventana, textvariable=cedula)
nombreTitulo = Label(ventana, text="Nombre",bg='#FCF8E8')
nombreEntrada = Entry(ventana, textvariable=nombre)
generotitulo = Label(ventana, text="Genero",bg='#FCF8E8')
generoM = Radiobutton(ventana, text='Masculino', value=True, variable=genero)
generoF = Radiobutton(ventana, text="Femenino", value=False, variable=genero)
personalidadTitulo = Label(ventana, text="Tipo de Personalidad",bg='#FCF8E8')
opciones=generarPerso(cargarBaseDatosPerso())
personalidadEntrada = Combobox(ventana, state='readonly',values=[opciones[0],opciones[1],opciones[2],opciones[3],opciones[4],
opciones[5],opciones[6],opciones[7],opciones[8],opciones[9],opciones[10],opciones[11],opciones[12],opciones[13],opciones[14],
opciones[15]],textvariable=personalidadCaja)
paisTitulo = Label(ventana, text="Pais",bg='#FCF8E8')
paisEntrada = Entry(ventana,state=DISABLED, textvariable=pais)
estadoTitulo = Label(ventana, text="Estado",bg='#FCF8E8')
estadoEntrada=Entry(ventana,state=DISABLED,textvariable=estado)
insertar = Button(ventana, text="Insertar", command=insertarParti,bg='#94B49F')
botonRegresarPequeño = Button(ventana, text="Regresar", command=ventanaPrincipal, width=12, height=2,bg='#DF7861')


#Botones Añadir  N  Personas

tituloAñadirN = Label(ventana, text="Insertar N Personas", font=("Times", 20),bg='#FCF8E8')
cantidadLabel = Label(ventana, text="Cantidad a generar",bg='#FCF8E8')
cantidad = StringVar()
cantidadEntrada = Entry(ventana, textvariable=cantidad)
insertarBotonN = Button(ventana, text="Insertar", command=anhadirNPersonas,bg='#94B49F')
limpiarBotonN = Button(ventana, text="Limpiar", command=clean,bg='#FCF8E8')


#Botones para Modificar
cedulaCod = StringVar()
tituloModificar = Label(ventana, text="Modificar Datos", font=("Times", 20),bg='#FCF8E8')
cedulaCodTitulo = Label(ventana, text="Cédula de la Persona",bg='#FCF8E8')
cedulaCodEntrada = Entry(ventana, textvariable=cedulaCod)
InsertarBoton = Button(ventana, text="Insertar",command=ventanaModificarAux,bg='#94B49F')
limpiarBoton = Button(ventana, text="Limpiar", command=clean,bg='#FCF8E8')
regresarBoton = Button(ventana, text='Regresar',command=ventanaPrincipal,bg='#DF7861')

#Botones para Modificar Aux

cedulaAux = StringVar()
nombreAux=StringVar()
personalidadAux=StringVar()
nuevaPersoAux = StringVar()
modificarTitulo =  Label(ventana, text="Modificar Personalidad", font=("Times", 20),bg='#FCF8E8')
cedulaAuxTitulo = Label(ventana, text="Cédula",bg='#FCF8E8')
cedulaAuxEntrada = Entry(ventana,state=DISABLED,textvariable=cedulaAux)
nombreAuxTitulo = Label(ventana, text="Nombre",bg='#FCF8E8')
nombreAuxEntrada = Entry(ventana,state=DISABLED,textvariable=nombreAux)
personalidadAuxTitulo = Label(ventana, text="Personalidad Registrada",bg='#FCF8E8')
personalidadAuxEntrada = Entry(ventana,state=DISABLED,textvariable=personalidadAux)
persoListaAuxTitulo = Label(ventana,text='Nueva personalidad',bg='#FCF8E8')
persoListaAux = Combobox(ventana, state='readonly',values=[opciones[0],opciones[1],opciones[2],opciones[3],opciones[4],
opciones[5],opciones[6],opciones[7],opciones[8],opciones[9],opciones[10],opciones[11],opciones[12],opciones[13],opciones[14],
opciones[15]],textvariable=nuevaPersoAux)
insertarModAux = Button(ventana,text='Ingresar',command=mostrarModificarDatos,bg='#94B49F')


#Botones para Eliminar
cedulaEli = StringVar()
motivo = StringVar()

eliminarTitulo = Label(ventana, text="Eliminar Persona",bg='#FCF8E8',font=("Imprint MT Shadow", 20))
cedulaEliTitulo = Label(ventana, text="Ingrese la cédula",bg='#FCF8E8')
cedulaEliEntrada = Entry(ventana, textvariable=cedulaEli)
motivoTitulo = Label(ventana, text="Ingrese el motivo",bg='#FCF8E8')
motivoEntrada = Entry(ventana,textvariable=motivo)
ingresarMotivo = Button(ventana,text="Ingresar",bg="#94B49F",command=ventanaEliminarAux)#AUIII
limpiarMotivo = Button(ventana,text="Limpiar",bg="#FCF8E8",command=clean)
regresarMotivo = Button(ventana,text="Regresar",bg='#DF7861',command=ventanaPrincipal)
ingresarMotivoAux = Button(ventana,text="Ingresar",bg="#94B49F",command=eliminarPersona)


#Botones Reportes
tituloReportes=Label(ventana, text="Reporte", font=("Imprint MT Shadow", 40),bg='#FCF8E8')
reportePersonalidad=Button(ventana, text="Reporte Personalidades",height=2, width=65,font=("Arial",12), bd=5,bg='#94B49F',command=reportePersonalidades,state=ACTIVE)
reporteTipo = Button(ventana, text="Reporte Tipo de Personalidad",height=2, width=65,font=("Arial",12),bd=5, bg='#94B49F',command=reporteTipoPersonalidad,state=ACTIVE)
reportePersona = Button(ventana, text="Reporte de una Persona",height=2, width=65,font=("Arial",12),bd=5,bg='#94B49F', command=reporteInfoPersona,state=ACTIVE)
reporteBDBoton = Button(ventana, text="Reporte de la BD",height=2, width=65,font=("Arial",12),bd=5, bg='#94B49F', command=reporteBD,state=ACTIVE)
reporteRetiradosBoton = Button(ventana, text="Reporte Retirados",height=2, width=65,font=("Arial",12),bd=5, bg='#94B49F', command=reporteRetirados,state=ACTIVE)
reportePorPaisBoton= Button(ventana, text="Reporte por País",height=2, width=65,font=("Arial",12),bd=5, bg='#94B49F',command=reportePorPais,state=ACTIVE)
#ReporteTipos
tituloReporteTipos = Label(ventana, text="Reporte Tipos", font=("Times", 20))
selecccionarTipo = Label(ventana, text="Seleccione un tipo: ")
tipo = StringVar()
op = generarTipos(personalidades)
tipoCombobox = Combobox(ventana, state='readonly',values=[op[0],op[1],op[2],op[3]],textvariable=tipo)
generarBotonTipos = Button(ventana, text="Generar", command=generarReporteTipo)
limpiarBotonN = Button(ventana, text="Limpiar", command=clean)
regresarReportes = Button(ventana, text="Regresar", command=ventanaReportes, width=12, height=2)
#ReportePersona
tituloReportePersona = Label(ventana, text="Reporte de Persona", font=("Times", 20))
introducirCedula = Label(ventana, text="Introduzca una cédula: ")
generarBotonPersona = Button(ventana, text="Generar", command=generarReportePersonas)
limpiarBotonN = Button(ventana, text="Limpiar", command=clean)
regresarReportes = Button(ventana, text="Regresar", command=ventanaReportes, width=12, height=2)


#PP
ventanaPrincipal()
ventana.mainloop()
