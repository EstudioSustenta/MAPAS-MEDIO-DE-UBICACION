# apagar un grupo 
#

import arcpy

def apagagr(group_name):
    # Redefine el nombre con comillas
    #group_name = '"' + group_name + '"'
    print("APAGANDO GRUPO " + group_name)

    # Obtener el mapa actual
    mxd = arcpy.mapping.MapDocument("CURRENT")

    # Iterar a través de los data frames en el mapa
    for df in arcpy.mapping.ListDataFrames(mxd):
        # Iterar a través de las capas en el data frame
        for lyr in arcpy.mapping.ListLayers(mxd, "", df):
            if lyr.isGroupLayer and lyr.name == group_name:
                lyr.visible = False  # Apagar el grupo

    # Actualizar la vista del mapa
    arcpy.RefreshActiveView()

# Llamar a la función para apagar un grupo específico
# apgr("Nombre_del_Grupo")

import arcpy

def enciendegr(group_name):
    # Redefine el nombre con comillas
    #group_name = '"' + group_name + '"'
    print("ENCENDIENDO GRUPO " + group_name)

    # Obtener el mapa actual
    mxd = arcpy.mapping.MapDocument("CURRENT")

    # Iterar a través de los data frames en el mapa
    for df in arcpy.mapping.ListDataFrames(mxd):
        # Iterar a través de las capas en el data frame
        for lyr in arcpy.mapping.ListLayers(mxd, "", df):
            if lyr.isGroupLayer and lyr.name == group_name:
                lyr.visible = True  # Apagar el grupo

    # Actualizar la vista del mapa
    arcpy.RefreshActiveView()

# Llamar a la función para apagar un grupo específico
# apgr("Nombre_del_Grupo")
