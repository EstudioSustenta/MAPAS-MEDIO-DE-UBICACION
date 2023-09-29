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


    # nota, para poder cargar las librería y que se genere el archivo .pyc adecuadamente, cada librería debe iniciar con la línea: # -*- coding: utf-8 -*-


# -------------------------------------------------------------------------------
# Preliminares
formato.formato_layout("Preparacion")
capas = arcpy.mapping.ListLayers(mxd)
for capa in capas:
    print capa.name
    if capa.name == "SISTEMA":
        capa.name = arcpy.env.proyecto
        arcpy.RefreshActiveView()
        print(capa.name + " renombrada correctamente")


# -------------------------------------------------------------------------------
# Proceso para generar mapa a nivel pais
nombre_capa = "ESTATAL"
ruta_arch = "Y:/0_SIG_PROCESO/BASES DE DATOS/00 MEXICO/0 UBICACION"
ccapas.carga_capas(ruta_arch, nombre_capa)
layout_name = "Layout"
nombre_capa = nombre_capa
z_extent.zoom_extent(layout_name, nombre_capa)
simbologia.aplica_simb(nombre_capa)
formato.formato_layout("UBICACIÓN A NIVEL PAÍS")
r_dest = carpeta_cliente + arcpy.env.proyecto + "_01_pais"
nnomb = "Entidades Federativas"
renombra.renomb(nombre_capa, nnomb)
exportma.exportar(r_dest)
ccapas.remover_capas(nnomb)


# -------------------------------------------------------------------------------
# Proceso para generar mapa estatal

nombre_capa = "MUNICIPAL CENSO 2020 DECRETO 185"
ruta_arch = "Y:/0_SIG_PROCESO/BASES DE DATOS/00 MEXICO/INEGI"
ruta_arch1 = "Y:/GIS/MEXICO/VARIOS/INEGI/CENSALES/SCINCE 2020/" + arcpy.env.estado + "/cartografia"
nombre_capa1 = "manzana_localidad"
campo = "NOM_ENT"
layout_name = "Layout"
ccapas.carga_capas(ruta_arch, nombre_capa)
filtro.aplicar_defq(nombre_capa, campo, "'" + arcpy.env.estado + "'")
z_extent.zoom_extent(layout_name, nombre_capa)
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

# -------------------------------------------------------------------------------
# Proceso para generar mapa municipal

if not arcpy.env.localidad == "Zona no urbanizada":
    # proceso si el sistema es urbano
    print("Iniciando proceso urbano")
    urbano =   importlib.import_module("LIBRERIA.URBANO NACIONAL 1_0_0")        # ejecuta rutina de zonas urbanas
    # reload(urbano)
    urbano.purbano()

    # 
else:
    # proceso si el sistema es rural
    print("Iniciando Proceso rural")
    rural =   importlib.import_module("LIBRERIA.RURAL_NACIONAL_1_0_0")        # ejecuta rutina de zonas rurales
    rural.prural("abc")

# -------------------------------------------------------------------------------
# Proceso para generar cuadros de construcción en formato dwg

dwgs = importlib.import_module("LIBRERIA.CUADRO DE LOCALIZACION")
# reload(dwgs)
dwgs.dxf("aaaa")


# -------------------------------------------------------------------------------
# Proceso para analizar servicios cercanos al sistema (5 minutos caminando a 5 km/hr)


if  arcpy.env.localidad != "Zona no urbanizada":
    # proceso si el sistema es urbano
    print("Iniciando proceso de servicios urbanos")
    servicios = importlib.import_module("LIBRERIA.SERVICIOS")
    reload(servicios)


# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# Proceso para el medio físico natural

cliptema = importlib.import_module("LIBRERIA.CLIP TEMATICO")
idproy = importlib.import_module("LIBRERIA.IDENTITY SISTEMA")

#-----------------> USO DE SUELO<------------------------------------------
    # tabla
rutaCl = "Y:/0_SIG_PROCESO/BASES DE DATOS/00 MEXICO/INEGI/" # ruta del archivo a identificar
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
nummapa = "09"
tit = "USO DE SUELO INEGI SERIE IV"
cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit)




#----------------->CURVAS DE NIVEL<------------------------------------------

    # mapa
capas = ["Curvas de nivel"]
rutas = ["Y:/0_SIG_PROCESO/BASES DE DATOS/00 MEXICO/INEGI"]
tipo = "municipal"
ncampo = "ALTURA"
nummapa = "10"
tit = "Curvas de nivel"
cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit)


#----------------->CORRIENTES Y CUERPOS DE AGUA<------------------------------------------

    # mapa
capas = ["Corrientes de agua", "Cuerpos de agua"]
rutaor = "Y:/GIS/MEXICO/VARIOS/INEGI/Mapa Digital 6/WGS84"
rutas = [rutaor, rutaor]
tipo = "municipal"
ncampo = "NOMBRE"
nummapa = "11"
tit = "Hidrologia"
cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit)

nearexp = importlib.import_module("LIBRERIA.NEAR A SISTEMA")

    # near a Linea de transmision electrica
rutaorigen = rutaor + "/"
capa = capas[0]
distancia = 50
campo = "NEAR_DIST"
valor = -1
camporef = "NOMBRE"
archivo = capa + " near"
cantidad = 20
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
nearexp.nearproceso(rutaorigen, capa, distancia, campo, valor, camporef, archivo, cantidad)


#----------------->LINEAS DE TRANSMISIÓN ELECTRICA<------------------------------------------

    # mapa
capas = ["Linea de transmision electrica"]
rutaor = "Y:/GIS/MEXICO/VARIOS/INEGI/Mapa Digital 6/WGS84"
rutas = [rutaor]
tipo = "estatal"
ncampo = "TIPO"
nummapa = "12"
tit = u"Líneas de transmisión eléctrica"
cliptema.cliptema(rutas, capas, tipo, ncampo, nummapa, tit)

nearexp = importlib.import_module("NEAR A SISTEMA")

    # near a Linea de transmision electrica
rutaorigen = rutaor + "/"
capa = capas[0]
distancia = 50
campo = "NEAR_DIST"
valor = -1
camporef = "CODIGO"
archivo = capa + " near"
cantidad = 20
nearproceso(rutaorigen, capa, distancia, campo, valor, camporef, archivo, cantidad)
