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
ruta_libreria = "Q:/09 SISTEMAS INFORMATICOS/GIS_PYTON"
sys.path.append(ruta_libreria)

arcpy.env.mxd = arcpy.mapping.MapDocument("CURRENT")                    # Obtener acceso al documento actual
mxd = arcpy.env.mxd
arcpy.env.df = arcpy.mapping.ListDataFrames(mxd)[0]
df = arcpy.env.df

# Importar el módulo desde el paquete LIBRERIA utilizando importlib
dbas = importlib.import_module("LIBRERIA.DATOS BASICOS")
ccapas = importlib.import_module("LIBRERIA.CARGAR CAPAS 1_0_0")         #carga el script de carga y remoción de capas  -----> funciones: carga_capas(ruta_arch, nombres_capas), remover_capas(capas_remover)
ctrlcapa = importlib.import_module("LIBRERIA.CONTROL DE CAPA 1_0_0")    #carga el script de control de capas  -----> funciones: apagacapa(capa_a_apagar), encendercapa(capa_a_encender)
ctrlgrup = importlib.import_module("LIBRERIA.CONTROL DE GRUPO 1_0_0")   #carga el script de control de grupos
exportma = importlib.import_module("LIBRERIA.EXPORTAR MAPAS 1_0_0")     #carga el script para exportar mapas a pdf y jpg
filtro = importlib.import_module("LIBRERIA.FILTRO 1_0_0")               #carga el script para aplicar filtros a una capa
formato = importlib.import_module("LIBRERIA.FORMATO 1_0_0")             #carga el script para aplicar formato a layout
simbologia = importlib.import_module("LIBRERIA.SIMBOLOGIA_LYR 1_0_0")   #carga el script para aplicar simbología a capas
z_extent = importlib.import_module("LIBRERIA.ZOOM EXTENT 1_0_0")        #carga el script para aplicar zoom extent a una capa 
act_rot = importlib.import_module("LIBRERIA.ACTIVA ROTULOS 1_0_0")      #carga el script para activar y desactivar los rótulos de una capa  -----> funciones: 
buff_cl = importlib.import_module("LIBRERIA.BUFFER_CLIP 1_0_0")         #carga el script para activar y desactivar los rótulos de una capa  -----> funciones: clip(ruta, radio)
transp = importlib.import_module("LIBRERIA.APLICA TRANSPARENCIA 1_0_0")   #carga el script para aplicar transparencia a capas
renombra = importlib.import_module("LIBRERIA.RENOMBRAR_CAPA_1_0_0")       #carga el script para cambiar el nombre a capas
urbano =   importlib.import_module("LIBRERIA.URBANO NACIONAL 1_0_0")        # ejecuta rutina de zonas urbanas
rural =   importlib.import_module("LIBRERIA.RURAL_NACIONAL_1_0_0")        # ejecuta rutina de zonas rurales
dwgs = importlib.import_module("LIBRERIA.CUADRO DE LOCALIZACION")
servicios = importlib.import_module("LIBRERIA.SERVICIOS")
cliptema = importlib.import_module("LIBRERIA.CLIP TEMATICO")
idproy = importlib.import_module("LIBRERIA.IDENTITY SISTEMA")
nearexp = importlib.import_module("LIBRERIA.NEAR A SISTEMA")



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



def mapaPais():
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
    r_dest = carpeta_cliente + arcpy.env.proyecto + "_01_pais"
    nnomb = "Entidades Federativas"
    renombra.renomb(nombre_capa, nnomb)
    exportma.exportar(r_dest)
    ccapas.remover_capas(nnomb)


def mapaEstatal():
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
    r_dest = carpeta_cliente + arcpy.env.proyecto + "_02_estado"
    nnomb = "Municipios " + arcpy.env.estado
    renombra.renomb(nombre_capa, nnomb)
    renombra.renomb("manzana_localidad", "Manzanas urbanas")
    exportma.exportar(r_dest)
    ccapas.remover_capas(nnomb)
    ccapas.remover_capas("Manzanas urbanas")

def mapaMunicipal():
    # -------------------------------------------------------------------------------
    # Proceso para generar mapa municipal

    if not arcpy.env.localidad == "Zona no urbanizada":
        # proceso si el sistema es urbano
        print("Iniciando proceso urbano")
        urbano.purbano()

        # 
    else:
        # proceso si el sistema es rural
        print("Iniciando Proceso rural")
        rural.prural()

def cuadroConstruccion():
    # -------------------------------------------------------------------------------
    # Proceso para generar cuadros de construcción en formato dwg
    
    # reload(dwgs)
    dwgs.dxf("aaaa")

def serviciosCercanos():
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
    nummapa = nummapa + 1
    tit = "USO DE SUELO INEGI SERIE IV"
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit)



def curvasdeNivel(nummapa):
    #----------------->CURVAS DE NIVEL<------------------------------------------

        # mapa
    capas = ["Curvas de nivel"]
    rutas = ["Y:/GIS/MEXICO/VARIOS/INEGI/Mapa Digital 6/WGS84"]
    tipo = "municipal"
    ncampo = "ALTURA"
    nummapa = nummapa + 1
    tit = "Curvas de nivel"
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit)


def hidrologia(nummapa):
    #----------------->CORRIENTES Y CUERPOS DE AGUA<------------------------------------------

        # mapa
    capas = ["Corrientes de agua", "Cuerpos de agua"]
    rutaor = "Y:/GIS/MEXICO/VARIOS/INEGI/Mapa Digital 6/WGS84"
    rutas = [rutaor, rutaor]
    tipo = "municipal"
    ncampo = "NOMBRE"
    nummapa = nummapa + 1
    tit = "Hidrologia"
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit)

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
    nummapa = nummapa + 1
    tit = u"Líneas de transmisión eléctrica"
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit)

    tipo = "municipal"
    nummapa = nummapa + 1
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit)

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
    nummapa = nummapa + 1
    tit = "MALPAIS INEGI SERIE IV"  # título del mapa en el layout
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit)


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
    nummapa = nummapa + 1           # consecutivo para el número de mapa en el nombre del archivo
    tit = "PANTANOS INEGI SERIE IV"  # título del mapa en el layout
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit)
    
    
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
    nummapa = nummapa + 1                       # consecutivo para el número de mapa en el nombre del archivo
    tit = u"PISTAS DE AVIACIÓN"                 # título del mapa en el layout
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit)


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



def plantaGeneradora(nummapa):
    #-----------------> PLANTA GENERADORA<------------------------------------------
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

    tipo = "nacional"                           # código para el nivel de representación
    nummapa = nummapa + 1                       # consecutivo para el número de mapa en el nombre del archivo
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit) 

    tipo = "estatal"                            # código para el nivel de representación
    nummapa = nummapa + 1                       # consecutivo para el número de mapa en el nombre del archivo
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit)


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



def presa(nummapa):

    #-----------------> PRESA<------------------------------------------
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

    tipo = "nacional"                           # código para el nivel de representación
    nummapa = nummapa + 1                       # consecutivo para el número de mapa en el nombre del archivo
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit) 

    tipo = "estatal"                            # código para el nivel de representación
    nummapa = nummapa + 1                       # consecutivo para el número de mapa en el nombre del archivo
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit)


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

    tipo = "nacional"                           # código para el nivel de representación
    nummapa = nummapa + 1                       # consecutivo para el número de mapa en el nombre del archivo
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit) 

    tipo = "estatal"                            # código para el nivel de representación
    nummapa = nummapa + 1                       # consecutivo para el número de mapa en el nombre del archivo
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit)


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

def salina(nummapa):

    #-----------------> SALINA<------------------------------------------
        # tabla

    rutaCl = "Y:/GIS/MEXICO/VARIOS/INEGI/Mapa Digital 6/WGS84" # ruta del archivo a identificar
    capaCl = "Salina.shp" # archivo a identificar
    capa_salida = "Salina" # capa a crear en el mapa
    camposCons = ["GEOGRAFICO", "IDENTIFICA", "NOMBRE", "TIPO"] # campos a escribir en el archivo
    dAlter = ["IDENTIFICADOR GEOGRAFICO", "CLAVE DE IDENTIFICACION", "NOMBRE", "TIPO"] # descriptores para los campos en el archivo txt de salida

    idproy.idproy(rutaCl, capaCl, capa_salida, camposCons, dAlter)

        # mapa
    capas = ["Salina"]
    rutas = [rutaCl]
    ncampo = "NOMBRE"                           # campo para el rótulo
    tit = "Salina".upper()                      # título del mapa en el layout

    tipo = "nacional"                           # código para el nivel de representación
    nummapa = nummapa + 1                       # consecutivo para el número de mapa en el nombre del archivo
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit) 

    tipo = "estatal"                            # código para el nivel de representación
    nummapa = nummapa + 1                       # consecutivo para el número de mapa en el nombre del archivo
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit)


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


def subestacionelectrica(nummapa):

    #-----------------> SALINA<------------------------------------------
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

    # tipo = "nacional"                           # código para el nivel de representación
    # nummapa = nummapa + 1                       # consecutivo para el número de mapa en el nombre del archivo
    # cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit) 

    tipo = "estatal"                            # código para el nivel de representación
    nummapa = nummapa + 1                       # consecutivo para el número de mapa en el nombre del archivo
    cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit)


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




nummapa = 9
dbas.datosbasicos() # define los datos básicos del proyecto y crea el archivo txt correspondiente
rutacarp()
mapaPais()
mapaEstatal()
mapaMunicipal()
cuadroConstruccion()
serviciosCercanos()
usodeSuelo(nummapa + 1)
curvasdeNivel(nummapa + 1)
hidrologia(nummapa + 1)
lineasElectricas(nummapa + 1)
malpais(nummapa + 1)
pantano(nummapa + 1)
pistadeAviacion(nummapa + 1)
plantaGeneradora(nummapa + 1)
presa(nummapa + 1) 
rasgoArqueologico(nummapa + 1)
salina(nummapa + 1)
subestacionelectrica(nummapa + 1)

print ("\n\n\n\n PROCESO SIG FINALIZADO!! \n\n No es necesario guardar el mapa. \n\n\n")

