# -*- coding: utf-8 -*-

# ----RUTINA PARA IMPRIMIR MAPAS DE UBICACIÓN A NIVEL PAIS, ESTADO, MUNICIPIO, REGIÓN, ZONA Y SITIO

import arcpy
import sys
import importlib

# Agrega la ruta del paquete al path de Python
ruta_libreria = r"Q:\09 SISTEMAS INFORMATICOS\GIS_PYTON"
sys.path.append(ruta_libreria)

mxd = arcpy.mapping.MapDocument("CURRENT")          # Obtener acceso al documento actual

# Importar el módulo prueba desde el paquete LIBRERIA utilizando importlib
ccapas = importlib.import_module("LIBRERIA.CARGAR CAPAS 1_0_0")         #carga el script de carga y remoción de capas
ctrlcapa = importlib.import_module("LIBRERIA.CONTROL DE CAPA 1_0_0")    #carga el script de control de capas
ctrlgrup = importlib.import_module("LIBRERIA.CONTROL DE GRUPO 1_0_0")   #carga el script de control de grupos
exportma = importlib.import_module("LIBRERIA.EXPORTAR MAPAS 1_0_0")     #carga el script para exportar mapas a pdf y jpg
filtro = importlib.import_module("LIBRERIA.FILTRO 1_0_0")               #carga el script para aplicar filtros a una capa
formato = importlib.import_module("LIBRERIA.FORMATO 1_0_0")             #carga el script para aplicar formato a layout
simbologia = importlib.import_module("LIBRERIA.SIMBOLOGIA_LYR 1_0_0")   #carga el script para aplicar simbología a capas
z_extent = importlib.import_module("LIBRERIA.ZOOM EXTENT 1_0_0")        #carga el script para aplicar zoom extent a una capa 

# Llamar a la función
nombres_capas = ["ESTATAL", "emas01"] # se deben agregar al menos dos capas para que la rutina de aplicar simbología funcione correctamente    modificar script de simbología
ruta_arch = "Y:/0_SIG_PROCESO/BASES DE DATOS/00 MEXICO/0 UBICACION"
ccapas.carga_capas(ruta_arch, nombres_capas)
layout_name = "Layout"
layer_name = "ESTATAL"
z_extent.zoom_extent(layout_name, layer_name)
simbologia.aplica_simb(nombres_capas)
formato.formato_layout("UBICACIÓN A NIVEL PAÍS")
ctrlcapa.apagacapa("emas01")
exportma.exportar("_01_pais")
ccapas.remover_capas

# hasta aquí, todo bien.

