# -*- coding: utf-8 -*-

# ----RUTINA PARA IMPRIMIR MAPAS DE UBICACIÓN A NIVEL PAIS, ESTADO, MUNICIPIO, REGIÓN, ZONA Y SITIO

import arcpy
import sys
import importlib

# Proceso para inicializar cuadros de diálogo
import Tkinter as tk
import tkFileDialog
root = tk.Tk()
root.withdraw()


def rutacarp():

    # Abre un cuadro de diálogo para seleccionar una carpeta
    carp_mapas = "Y:/02 CLIENTES (EEX-CLI)/(2001-0001) FAMILIA MARTINEZ DEL RIO/(2008-PIN-0005) CASA BUENAVISTA/SIG"
    carpeta_cliente = tkFileDialog.askdirectory(initialdir=carp_mapas, title="Selecciona la carpeta destino de los mapas") + "/"
    arcpy.env.carp_cliente = carpeta_cliente
    # Verifica si el usuario seleccionó una carpeta
    if carpeta_cliente:
        print("Ruta de la carpeta seleccionada: %s" % carpeta_cliente)
    else:
        print("No se seleccionó ninguna carpeta.")


    
# Agrega la ruta del paquete al path de Python

ruta_libreria = "Q:/09 SISTEMAS INFORMATICOS/GIS_PYTON/SOPORTE_GIS"
print(ruta_libreria)
sys.path.append(ruta_libreria)

arcpy.env.mxd = arcpy.mapping.MapDocument("CURRENT")                    # Obtener acceso al documento actual
mxd = arcpy.env.mxd
arcpy.env.df = arcpy.mapping.ListDataFrames(mxd)[0]
df = arcpy.env.df

# Importar el módulo desde el paquete LIBRERIA utilizando importlib
dbas = importlib.import_module("LIBRERIA.datos_basicos")
ccapas = importlib.import_module("LIBRERIA.cargar_capas")               #carga el script de carga y remoción de capas  -----> funciones: carga_capas(ruta_arch, nombres_capas), remover_capas(capas_remover)
ctrlcapa = importlib.import_module("LIBRERIA.control_de_capa")          #carga el script de control de capas  -----> funciones: apagacapa(capa_a_apagar), encendercapa(capa_a_encender)
ctrlgrup = importlib.import_module("LIBRERIA.control_de_grupo")         #carga el script de control de grupos
exportma = importlib.import_module("LIBRERIA.exportar_mapas")           #carga el script para exportar mapas a pdf y jpg
filtro = importlib.import_module("LIBRERIA.filtro")                     #carga el script para aplicar filtros a una capa
formato = importlib.import_module("LIBRERIA.formato")                   #carga el script para aplicar formato a layout
simbologia = importlib.import_module("LIBRERIA.simbologia_lyr")         #carga el script para aplicar simbología a capas
z_extent = importlib.import_module("LIBRERIA.zoom_extent")              #carga el script para aplicar zoom extent a una capa 
act_rot = importlib.import_module("LIBRERIA.activa_rotulos")            #carga el script para activar y desactivar los rótulos de una capa  -----> funciones: 
buff_cl = importlib.import_module("LIBRERIA.buffer_clip")               #carga el script para activar y desactivar los rótulos de una capa  -----> funciones: clip(ruta, radio)
transp = importlib.import_module("LIBRERIA.aplica_transparencia")       #carga el script para aplicar transparencia a capas
renombra = importlib.import_module("LIBRERIA.renombrar_capa")           #carga el script para cambiar el nombre a capas
urbano = importlib.import_module("LIBRERIA.urbano_nacional")            # ejecuta rutina de zonas urbanas
rural = importlib.import_module("LIBRERIA.rural_nacional")              # ejecuta rutina de zonas rurales
dwgs = importlib.import_module("LIBRERIA.cuadro_de_localizacion")
servicios = importlib.import_module("LIBRERIA.servicios")
cliptema = importlib.import_module("LIBRERIA.clip_tematico")
idproy = importlib.import_module("LIBRERIA.identity_sistema")
nearexp = importlib.import_module("LIBRERIA.near_a_sistema")



reload(dbas)
reload(ccapas)
reload(ctrlcapa)
reload(ctrlgrup)
reload(exportma)
reload(filtro)
reload(formato)
reload(simbologia)
reload(z_extent)
reload(act_rot)
reload(buff_cl)
reload(transp)
reload(renombra)
reload(urbano)
reload(rural)
reload(dwgs)
reload(servicios)
reload(cliptema)
reload(idproy)
reload(nearexp)


    # nota, para poder cargar las librería y que se genere el archivo .pyc adecuadamente, cada librería debe iniciar con la línea: # -*- coding: utf-8 -*-


# -------------------------------------------------------------------------------
# Preliminares
def db():
    dbas.datosbasicos() # define los datos básicos del proyecto y crea el archivo txt correspondiente
    formato.formato_layout("Preparacion")


# elimina todas las capas, excepto "SISTEMA"

capas_a_mantener = []

# Iterar a través de todas las capas en el DataFrame
for lyr in arcpy.mapping.ListLayers(mxd, "", df):
    # Verificar si el nombre de la capa es "SISTEMA"
    if lyr.name == "SISTEMA":
        capas_a_mantener.append(lyr)  # Agregar la capa a la lista de capas a mantener

# Eliminar todas las capas del DataFrame
for lyr in arcpy.mapping.ListLayers(mxd, "", df):
    if lyr not in capas_a_mantener:
        arcpy.mapping.RemoveLayer(df, lyr)

# Actualizar el contenido del DataFrame
arcpy.RefreshTOC()



def mapaPais(nummapa):
    # -------------------------------------------------------------------------------
    # Proceso para generar mapa a nivel pais
    nombre_capa = "ESTATAL decr185"
    ruta_arch = "Y:/GIS/MEXICO/VARIOS/INEGI/Mapa Digital 6/WGS84/GEOPOLITICOS"
    ccapas.carga_capas(ruta_arch, nombre_capa)
    arcpy.env.layout = "Layout"
    act_rot.activar_rotulos("CURRENT", nombre_capa,"NOM_ENT")
    z_extent.zoom_extent(arcpy.env.layout, nombre_capa)
    simbologia.aplica_simb(nombre_capa)
    formato.formato_layout("UBICACIÓN A NIVEL PAÍS")
    r_dest = arcpy.env.carp_cliente + arcpy.env.proyecto + " " + str(nummapa) + " pais"
    nnomb = "Entidades Federativas"
    renombra.renomb(nombre_capa, nnomb)
    exportma.exportar(r_dest)
    ccapas.remover_capas(nnomb)
    arcpy.env.nummapa = nummapa + 1

def mapaEstatal(nummapa):
    # -------------------------------------------------------------------------------
    # Proceso para generar mapa estatal

    nombre_capa = "MUNICIPAL CENSO 2020 DECRETO 185"
    ruta_arch = "Y:/0_SIG_PROCESO/BASES DE DATOS/00 MEXICO/INEGI"
    ruta_arch1 = "Y:/GIS/MEXICO/VARIOS/INEGI/CENSALES/SCINCE 2020/" + arcpy.env.estado + "/cartografia"
    nombre_capa1 = "manzana_localidad"
    campo = "NOM_ENT"
    ccapas.carga_capas(ruta_arch, nombre_capa)
    filtro.aplicar_defq(nombre_capa, campo, "'" + arcpy.env.estado + "'")
    z_extent.zoom_extent(arcpy.env.layout, nombre_capa)
    simbologia.aplica_simb(nombre_capa)
    formato.formato_layout("UBICACIÓN A NIVEL ESTADO")
    act_rot.activar_rotulos("CURRENT", nombre_capa,"NOM_MUN")
    ccapas.carga_capas(ruta_arch1, "red nacional de caminos")
    simbologia.aplica_simb("red nacional de caminos")
    transp.transp("red nacional de caminos",50)
    ccapas.carga_capas(ruta_arch1, nombre_capa1)        # carga las manzanas del estado correspondiente.
    simbologia.aplica_simb(nombre_capa1)
    r_dest = arcpy.env.carp_cliente + arcpy.env.proyecto + " " + str(nummapa) + " estado"
    nnomb = "Municipios " + arcpy.env.estado
    renombra.renomb(nombre_capa, nnomb)
    renombra.renomb("manzana_localidad", "Manzanas urbanas")
    exportma.exportar(r_dest)
    ccapas.remover_capas(nnomb)
    ccapas.remover_capas("Manzanas urbanas")
    arcpy.env.nummapa = nummapa + 1
   


def mapaMunicipal(nummapa):
    # -------------------------------------------------------------------------------
    # Proceso para generar mapa municipal

    if not arcpy.env.localidad == "Zona no urbanizada":
        # proceso si el sistema es urbano
        print("Iniciando proceso urbano")
        urbano.purbano(nummapa)

        # 
    else:
        # proceso si el sistema es rural
        print("Iniciando Proceso rural")
        rural.prural(nummapa)


def cuadroConstruccion():
    # -------------------------------------------------------------------------------
    # Proceso para generar cuadros de construcción en formato dwg
    
    # reload(dwgs)
    dwgs.dxf("aaaa")

def serviciosCercanos(nummapa):
    # -------------------------------------------------------------------------------
    # Proceso para analizar servicios cercanos al sistema (5 minutos caminando a 5 km/hr)


    if  arcpy.env.localidad != "Zona no urbanizada":
        # proceso si el sistema es urbano
        print("Iniciando proceso de servicios urbanos")
        servicios.servicios()


# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# Proceso para el medio físico natural

def usodeSuelo(nummapa):
    #-----------------> USO DE SUELO<------------------------------------------
        # tabla
    rutaCl = "Y:/0_SIG_PROCESO/BASES DE DATOS/00 MEXICO/INEGI" # ruta del archivo a identificar
    capaCl = "USO DE SUELO INEGI SERIE IV.shp" # archivo a identificar
    capa_salida = "Uso de suelo" # capa a crear en el mapa
    camposCons = ["DESCRIP", "INFYS_0409", "VEG_FORES", 
                  "CVE_FAO", "HECTARES", "FORMACION", 
                  "DESVEG", "ECOS_VEGE"] # campos a escribir en el archivo
    dAlter = ["PROYECTO", "INFORMACION DEL SISTEMA", "VEGETACION FORESTAL", 
              "CLAVE FAO", "HECTAREAS", "FORMACION", 
              "DESCRIPCION DE VEGETACION", "ECOSISTEMA VEGETAL"]

    idproy.idproy(rutaCl, capaCl, capa_salida, camposCons, dAlter)

        # mapa
    capas = ["USO DE SUELO INEGI SERIE IV"]
    rutas = ["Y:/0_SIG_PROCESO/BASES DE DATOS/00 MEXICO/INEGI"]
    ncampo = "ECOS_VEGE"
    tipo = "municipal"
    nummapa = arcpy.env.nummapa
    tit = "USO DE SUELO INEGI SERIE IV"
    ordinal = 0
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit, ordinal)



def curvasdeNivel(nummapa):
    #----------------->CURVAS DE NIVEL<------------------------------------------

        # mapa
    capas = ["Curvas de nivel"]
    rutas = ["Y:/GIS/MEXICO/VARIOS/INEGI/Mapa Digital 6/WGS84"]
    tipo = "municipal"
    ncampo = "ALTURA"
    nummapa = arcpy.env.nummapa
    tit = "Curvas de nivel"
    ordinal = 0
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit, ordinal)


def hidrologia(nummapa):
    #----------------->CORRIENTES Y CUERPOS DE AGUA<------------------------------------------

        # mapa
    capas = ["Corrientes de agua", "Cuerpos de agua"]
    rutaor = "Y:/GIS/MEXICO/VARIOS/INEGI/Mapa Digital 6/WGS84"
    rutas = [rutaor, rutaor]
    tipo = "municipal"
    ncampo = "NOMBRE"
    nummapa = arcpy.env.nummapa
    tit = "Hidrologia"
    ordinal = 0
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit, ordinal)

        # near a corrientes de agua
    rutaorigen = rutaor + "/"
    capa = capas[0]
    distancia = 50
    campo = "NEAR_DIST"
    valor = -1
    camporef = "NOMBRE"
    archivo = capa + " near"
    cantidad = 20
    print ("iniciando proceso para " + capa)
    nearexp.nearproceso(rutaorigen, capa, distancia, campo, valor, camporef, archivo, cantidad)

        # near a cuerpos de agua
    rutaorigen = rutaor + "/"
    capa = capas[1]
    distancia = 50
    campo = "NEAR_DIST"
    valor = -1
    camporef = "NOMBRE"
    archivo = capa + " near"
    cantidad = 20
    print ("iniciando proceso para " + capa)
    nearexp.nearproceso(rutaorigen, capa, distancia, campo, valor, camporef, archivo, cantidad)

def lineasElectricas(nummapa):
    #----------------->LINEAS DE TRANSMISIÓN ELECTRICA<------------------------------------------

        # mapa
    capas = ["Linea de transmision electrica"]
    rutaor = "Y:/GIS/MEXICO/VARIOS/INEGI/Mapa Digital 6/WGS84"
    rutas = [rutaor]
    tipo = "estatal"
    ncampo = "TIPO"
    nummapa = arcpy.env.nummapa
    tit = u"Líneas de transmisión eléctrica"
    ordinal = 0
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit, ordinal)

    tipo = "municipal"
    nummapa = arcpy.env.nummapa
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit, ordinal)

        # near a Linea de transmision electrica
    rutaorigen = rutaor + "/"
    capa = capas[0]
    distancia = 50
    campo = "NEAR_DIST"
    valor = -1
    camporef = "TIPO"
    archivo = capa + " near"
    cantidad = 20
    nearexp.nearproceso(rutaorigen, capa, distancia, campo, valor, camporef, archivo, cantidad)


def malpais(nummapa):
    #-----------------> MALPAIS<------------------------------------------
        # tabla
    rutaCl = "Y:/GIS/MEXICO/VARIOS/INEGI/Mapa Digital 6/WGS84" # ruta del archivo a identificar
    capaCl = "Malpais.shp" # archivo a identificar
    capa_salida = "Malpais" # capa a crear en el mapa
    camposCons = ["GEOGRAFICO", "IDENTIFICA", "CODIGO"] # campos a escribir en el archivo
    dAlter = ["IDENTIFICADOR GEOGRAFICO", "CLAVE DE IDENTIFICACION", "CODIGO DE IDENTIFICACION"] # descriptores para los campos en el archivo txt de salida

    idproy.idproy(rutaCl, capaCl, capa_salida, camposCons, dAlter)

        # mapa
    capas = ["Malpais"]
    rutas = [rutaCl]
    ncampo = "IDENTIFICA" # campo para el rótulo
    tipo = "estatal" # código para el nivel de representación
    nummapa = arcpy.env.nummapa
    tit = "MALPAIS INEGI SERIE IV"  # título del mapa en el layout
    ordinal = 4

        # near 
    rutaorigen = rutaCl + "/"                   # Ruta del archivo a analizar
    capa = capas[0]                             # Capa a analizar
    distancia = 1000                            # Distancia a realizar el análisis en km (incluye cualquier elemento que esté a esa distancia)
    campo = "NEAR_DIST"                         # campo donde se guarda la distancia al sistema
    valor = -1                                  # valor a eliminar del campo 'campo'
    camporef = "OBJECTID"                       # campo de referencia (para agregar a la descripción del archivo)
    archivo = capa + " near"                    # nombre del archivo de texto a generar
    cantidad = 20                               # cantidad de registros más cercanos
    nearexp.nearproceso(rutaorigen, capa, distancia, campo, valor, camporef, archivo, cantidad)

    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit, ordinal)


def pantano(nummapa):
    #-----------------> PANTANO<------------------------------------------
        # tabla
    rutaCl = "Y:/GIS/MEXICO/VARIOS/INEGI/Mapa Digital 6/WGS84" # ruta del archivo a identificar
    capaCl = "Pantano.shp" # archivo a identificar
    capa_salida = "Pantano" # capa a crear en el mapa
    camposCons = ["GEOGRAFICO", "IDENTIFICA"] # campos a escribir en el archivo
    dAlter = [u"IDENTIFICADOR GEOGRÁFICO", u"CLAVE DE IDENTIFICACIÓN"] # descriptores para los campos en el archivo txt de salida
    
    idproy.idproy(rutaCl, capaCl, capa_salida, camposCons, dAlter)
    
        # mapa
    capas = ["Pantano"]
    rutas = [rutaCl]
    ncampo = "IDENTIFICA" # campo para el rótulo
    tipo = "estatal" # código para el nivel de representación
    nummapa = arcpy.env.nummapa           # consecutivo para el número de mapa en el nombre del archivo
    tit = "PANTANOS INEGI SERIE IV"  # título del mapa en el layout
    ordinal = 4
    
    
        # near 
    rutaorigen = rutaCl + "/"                   # Ruta del archivo a analizar
    capa = capas[0]                             # Capa a analizar
    distancia = 1000                            # Distancia a realizar el análisis en km (incluye cualquier elemento que esté a esa distancia)
    campo = "NEAR_DIST"                         # campo donde se guarda la distancia al sistema
    valor = -1                                  # valor a eliminar del campo 'campo'
    camporef = "OBJECTID"                       # campo de referencia (para agregar a la descripción del archivo)
    archivo = capa + " near"                    # nombre del archivo de texto a generar
    cantidad = 20                               # cantidad de registros más cercanos
    nearexp.nearproceso(rutaorigen, capa, distancia, campo, valor, camporef, archivo, cantidad)

    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit, ordinal)



def pistadeAviacion(nummapa):
    #-----------------> PISTA DE AVIACIÓN<------------------------------------------
        # tabla
    rutaCl = "Y:/GIS/MEXICO/VARIOS/INEGI/Mapa Digital 6/WGS84" # ruta del archivo a identificar
    capaCl = "Pista de aviacion.shp" # archivo a identificar
    capa_salida = "Pista de aviacion" # capa a crear en el mapa
    camposCons = ["GEOGRAFICO", "IDENTIFICA", "NOMBRE", "CONDICION", "TIPO"] # campos a escribir en el archivo
    dAlter = [u"IDENTIFICADOR GEOGRÁFICO", u"CLAVE DE IDENTIFICACIÓN", u"NOMBRE", u"CONDICIÓN", u"TIPO"] # descriptores para los campos en el archivo txt de salida

    # idproy.idproy(rutaCl, capaCl, capa_salida, camposCons, dAlter)

        # mapa
    capas = ["Pista de aviacion"]
    rutas = [rutaCl]
    ncampo = "IDENTIFICA"                       # campo para el rótulo
    tipo = "estatal"                            # código para el nivel de representación
    nummapa = arcpy.env.nummapa                       # consecutivo para el número de mapa en el nombre del archivo
    tit = u"PISTAS DE AVIACIÓN"                 # título del mapa en el layout
    ordinal = 5
        # near 
    rutaorigen = rutaCl + "/"                   # Ruta del archivo a analizar
    capa = capas[0]                             # Capa a analizar
    distancia = 1000                            # Distancia a realizar el análisis en km (incluye cualquier elemento que esté a esa distancia)
    campo = "NEAR_DIST"                         # campo donde se guarda la distancia al sistema
    valor = -1                                  # valor a eliminar del campo 'campo'
    camporef = ncampo                           # campo de referencia (para agregar a la descripción del archivo)
    archivo = capa + " near"                    # nombre del archivo de texto a generar
    cantidad = 20                               # cantidad de registros más cercanos

    nearexp.nearproceso(rutaorigen, capa, distancia, campo, valor, camporef, archivo, cantidad)
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit, ordinal)



#-----------------> PLANTA GENERADORA<------------------------------------------

def plantaGeneradora(nummapa):
    
        # tabla
    rutaCl = "Y:/GIS/MEXICO/VARIOS/INEGI/Mapa Digital 6/WGS84" # ruta del archivo a identificar
    capaCl = "Planta generadora.shp" # archivo a identificar
    capa_salida = "Planta generadora" # capa a crear en el mapa
    camposCons = ["GEOGRAFICO", "IDENTIFICA", "NOMBRE", "CONDICION", "TIPO"] # campos a escribir en el archivo
    dAlter = [u"IDENTIFICADOR GEOGRAFICO", u"CLAVE DE IDENTIFICACION", u"NOMBRE", u"CONDICION", u"TIPO"] # descriptores para los campos en el archivo txt de salida

    # idproy.idproy(rutaCl, capaCl, capa_salida, camposCons, dAlter)

        # mapa
    capas = ["Planta generadora"]
    rutas = [rutaCl]
    ncampo = "NOMBRE"                           # campo para el rótulo
    tit = u"PLANTA GENERADORA"                  # título del mapa en el layout
    ordinal = 0
        # near 
    rutaorigen = rutaCl + "/"                   # Ruta del archivo a analizar
    capa = capas[0]                             # Capa a analizar
    distancia = 1000                            # Distancia a realizar el análisis en km (incluye cualquier elemento que esté a esa distancia)
    campo = "NEAR_DIST"                         # campo donde se guarda la distancia al sistema
    valor = -1                                  # valor a eliminar del campo 'campo'
    camporef = ncampo                           # campo de referencia (para agregar a la descripción del archivo)
    archivo = capa + " near"                    # nombre del archivo de texto a generar
    cantidad = 20                               # cantidad de registros más cercanos
    
    nearexp.nearproceso(rutaorigen, capa, distancia, campo, valor, camporef, archivo, cantidad)

    tipo = "nacional"                           # código para el nivel de representación
    nummapa = arcpy.env.nummapa                       # consecutivo para el número de mapa en el nombre del archivo
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit, ordinal) 

    tipo = "estatal"                            # código para el nivel de representación
    nummapa = arcpy.env.nummapa                       # consecutivo para el número de mapa en el nombre del archivo
    ordinal = 5
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit, ordinal)


#-----------------> PRESA<------------------------------------------

def presa(nummapa):

        # tabla

    rutaCl = "Y:/GIS/MEXICO/VARIOS/INEGI/Mapa Digital 6/WGS84" # ruta del archivo a identificar
    capaCl = "Presa.shp" # archivo a identificar
    capa_salida = "Presa" # capa a crear en el mapa
    camposCons = ["GEOGRAFICO", "IDENTIFICA", "NOMBRE", "CONDICION"] # campos a escribir en el archivo
    dAlter = [u"IDENTIFICADOR GEOGRAFICO", u"CLAVE DE IDENTIFICACION", u"NOMBRE", u"CONDICION"] # descriptores para los campos en el archivo txt de salida

    # idproy.idproy(rutaCl, capaCl, capa_salida, camposCons, dAlter)

        # mapa
    capas = ["Presa"]
    rutas = [rutaCl]
    ncampo = "NOMBRE"                           # campo para el rótulo
    tit = u"Presa".upper()                      # título del mapa en el layout


          # near 
    rutaorigen = rutaCl + "/"                   # Ruta del archivo a analizar
    capa = capas[0]                             # Capa a analizar
    distancia = 1000                            # Distancia a realizar el análisis en km (incluye cualquier elemento que esté a esa distancia)
    campo = "NEAR_DIST"                         # campo donde se guarda la distancia al sistema
    valor = -1                                  # valor a eliminar del campo 'campo'
    camporef = ncampo                           # campo de referencia (para agregar a la descripción del archivo)
    archivo = capa + " near"                    # nombre del archivo de texto a generar
    cantidad = 20                               # cantidad de registros más cercanos
    nearexp.nearproceso(rutaorigen, capa, distancia, campo, valor, camporef, archivo, cantidad)  

    tipo = "nacional"                           # código para el nivel de representación
    nummapa = arcpy.env.nummapa                       # consecutivo para el número de mapa en el nombre del archivo
    ordinal = 0
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit, ordinal) 

    tipo = "estatal"                            # código para el nivel de representación
    nummapa = arcpy.env.nummapa                       # consecutivo para el número de mapa en el nombre del archivo
    ordinal = 5
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit, ordinal)





def rasgoArqueologico(nummapa):

    #-----------------> RASGO ARQUEOLOGICO<------------------------------------------
        # tabla

    rutaCl = "Y:/GIS/MEXICO/VARIOS/INEGI/Mapa Digital 6/WGS84" # ruta del archivo a identificar
    capaCl = "Rasgo arqueologico.shp" # archivo a identificar
    capa_salida = "Rasgo arqueologico" # capa a crear en el mapa
    camposCons = ["GEOGRAFICO", "IDENTIFICA", "NOMBRE", "TIPO"] # campos a escribir en el archivo
    dAlter = ["IDENTIFICADOR GEOGRAFICO", "CLAVE DE IDENTIFICACION", "NOMBRE", "TIPO"] # descriptores para los campos en el archivo txt de salida

    # idproy.idproy(rutaCl, capaCl, capa_salida, camposCons, dAlter)

        # mapa
    capas = ["Rasgo arqueologico"]
    rutas = [rutaCl]
    ncampo = "NOMBRE"                           # campo para el rótulo
    tit = "Rasgo arqueologico".upper()                      # título del mapa en el layout
        
        # near 
    rutaorigen = rutaCl + "/"                   # Ruta del archivo a analizar
    capa = capas[0]                             # Capa a analizar
    distancia = 1000                            # Distancia a realizar el análisis en km (incluye cualquier elemento que esté a esa distancia)
    campo = "NEAR_DIST"                         # campo donde se guarda la distancia al sistema
    valor = -1                                  # valor a eliminar del campo 'campo'
    camporef = ncampo                           # campo de referencia (para agregar a la descripción del archivo)
    archivo = capa + " near"                    # nombre del archivo de texto a generar
    cantidad = 20                               # cantidad de registros más cercanos
    nearexp.nearproceso(rutaorigen, capa, distancia, campo, valor, camporef, archivo, cantidad)

    tipo = "nacional"                           # código para el nivel de representación
    nummapa = arcpy.env.nummapa                       # consecutivo para el número de mapa en el nombre del archivo
    ordinal = 0
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit, ordinal) 

    tipo = "estatal"                            # código para el nivel de representación
    nummapa = arcpy.env.nummapa                       # consecutivo para el número de mapa en el nombre del archivo
    ordinal = 4
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit, ordinal)



def salina(nummapa):

    #-----------------> SALINA<------------------------------------------
        # tabla

    rutaCl = "Y:/GIS/MEXICO/VARIOS/INEGI/Mapa Digital 6/WGS84" # ruta del archivo a identificar
    capaCl = "Salina.shp" # archivo a identificar
    capa_salida = "Salina" # capa a crear en el mapa
    camposCons = ["GEOGRAFICO", "IDENTIFICA", "NOMBRE", "TIPO"] # campos a escribir en el archivo
    dAlter = ["IDENTIFICADOR GEOGRAFICO", "CLAVE DE IDENTIFICACION", "NOMBRE", "TIPO"] # descriptores para los campos en el archivo txt de salida

    idproy.idproy(rutaCl, capaCl, capa_salida, camposCons, dAlter)

        
    capas = ["Salina"]
    rutas = [rutaCl]
    ncampo = "NOMBRE"                           # campo para el rótulo
    tit = "Salina".upper()                      # título del mapa en el layout

        # near 
    rutaorigen = rutaCl + "/"                   # Ruta del archivo a analizar
    capa = capas[0]                             # Capa a analizar
    distancia = 1000                            # Distancia a realizar el análisis en km (incluye cualquier elemento que esté a esa distancia)
    campo = "NEAR_DIST"                         # campo donde se guarda la distancia al sistema
    valor = -1                                  # valor a eliminar del campo 'campo'
    camporef = ncampo                           # campo de referencia (para agregar a la descripción del archivo)
    archivo = capa + " near"                    # nombre del archivo de texto a generar
    cantidad = 20                               # cantidad de registros más cercanos
    nearexp.nearproceso(rutaorigen, capa, distancia, campo, valor, camporef, archivo, cantidad)

        # mapa
    tipo = "nacional"                           # código para el nivel de representación
    nummapa = arcpy.env.nummapa                       # consecutivo para el número de mapa en el nombre del archivo
    ordinal = 0
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit, ordinal) 

    tipo = "estatal"                            # código para el nivel de representación
    nummapa = arcpy.env.nummapa                       # consecutivo para el número de mapa en el nombre del archivo
    ordinal = 3
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit, ordinal)




def subestacionelectrica(nummapa):

    #-----------------> SUBESTACION ELECTRICA<------------------------------------------
        # tabla

    rutaCl = "Y:/GIS/MEXICO/VARIOS/INEGI/Mapa Digital 6/WGS84" # ruta del archivo a identificar
    capaCl = "Subestacion electrica.shp" # archivo a identificar
    capa_salida = "Subestacion electrica" # capa a crear en el mapa
    camposCons = ["GEOGRAFICO", "IDENTIFICA", "NOMBRE", "CONDICION"] # campos a escribir en el archivo
    dAlter = ["IDENTIFICADOR GEOGRAFICO", "CLAVE DE IDENTIFICACION", "NOMBRE", "CONDICION"] # descriptores para los campos en el archivo txt de salida

    idproy.idproy(rutaCl, capaCl, capa_salida, camposCons, dAlter)

        # mapa
    capas = ["Subestacion electrica"]
    rutas = [rutaCl]
    ncampo = "NOMBRE"                           # campo para el rótulo
    tit = "Subestacion electrica".upper()                      # título del mapa en el layout

        # near 
    rutaorigen = rutaCl + "/"                   # Ruta del archivo a analizar
    capa = capas[0]                             # Capa a analizar
    distancia = 1000                            # Distancia a realizar el análisis en km (incluye cualquier elemento que esté a esa distancia)
    campo = "NEAR_DIST"                         # campo donde se guarda la distancia al sistema
    valor = -1                                  # valor a eliminar del campo 'campo'
    camporef = ncampo                           # campo de referencia (para agregar a la descripción del archivo)
    archivo = capa + " near"                    # nombre del archivo de texto a generar
    cantidad = 20                               # cantidad de registros más cercanos
    nearexp.nearproceso(rutaorigen, capa, distancia, campo, valor, camporef, archivo, cantidad)

    # tipo = "nacional"                           # código para el nivel de representación
    # nummapa = arcpy.env.nummapa                       # consecutivo para el número de mapa en el nombre del archivo
    # cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit, ordinal) 

    tipo = "estatal"                            # código para el nivel de representación
    nummapa = arcpy.env.nummapa                       # consecutivo para el número de mapa en el nombre del archivo
    ordinal = 5
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit, ordinal)


rutacarp()
db()
arcpy.env.nummapa = 1
mapaPais(arcpy.env.nummapa)
mapaEstatal(arcpy.env.nummapa)
mapaMunicipal(arcpy.env.nummapa)
cuadroConstruccion()
serviciosCercanos(arcpy.env.nummapa)
usodeSuelo(arcpy.env.nummapa)
curvasdeNivel(arcpy.env.nummapa)
hidrologia(arcpy.env.nummapa)
lineasElectricas(arcpy.env.nummapa)
malpais(arcpy.env.nummapa)
pantano(arcpy.env.nummapa)
pistadeAviacion(arcpy.env.nummapa)
plantaGeneradora(arcpy.env.nummapa)
presa(arcpy.env.nummapa) 
rasgoArqueologico(arcpy.env.nummapa)
salina(arcpy.env.nummapa)
subestacionelectrica(arcpy.env.nummapa)

print ("\n\n\n\n PROCESO SIG FINALIZADO!! \n\n No es necesario guardar el mapa. \n\n\n")

