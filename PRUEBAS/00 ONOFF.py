# ENCIENDE O APAGA LA CAPA DEFINIDA EN LA FUNCIÓN onoff
# SÍ FUNCIONA

import arcpy

def onoff(layer_name):
    # Obtener el mapa actual
    mxd = arcpy.mapping.MapDocument("CURRENT")

    # Iterar a través de los data frames en el mapa
    for df in arcpy.mapping.ListDataFrames(mxd):
        # Iterar a través de las capas en el data frame
        for lyr in arcpy.mapping.ListLayers(mxd, "", df):
            if lyr.name == layer_name:
                if lyr.visible:
                    lyr.visible = False  # Apagar la capa
                else:
                    lyr.visible = True  # Encender la capa

    # Actualizar la vista del mapa
    arcpy.RefreshActiveView()

# Llamar a la función con el nombre de la capa, ejemplo:
# onoff("EMAS_88_22")
