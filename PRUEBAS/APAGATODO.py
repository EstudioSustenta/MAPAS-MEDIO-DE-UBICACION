# APAGA TODAS LAS CAPAS DEL MAPA
# SÍ FUNCIONA

import arcpy

def onoff(layer_name, turn_on=True):
    # Obtener el mapa actual
    mxd = arcpy.mapping.MapDocument("CURRENT")

    # Iterar a través de los data frames en el mapa
    for df in arcpy.mapping.ListDataFrames(mxd):
        # Iterar a través de las capas en el data frame
        for lyr in arcpy.mapping.ListLayers(mxd, "", df):
            if lyr.name == layer_name:
                if turn_on:
                    lyr.visible = True  # Encender la capa
                else:
                    lyr.visible = False  # Apagar la capa

    # Actualizar la vista del mapa
    arcpy.RefreshActiveView()

# Apagar todas las capas del mapa
# onoff("", False)

