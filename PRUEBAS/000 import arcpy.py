import arcpy

def apagacapas(dataframe_name):
    # Obtener acceso al documento actual
    mxd = arcpy.mapping.MapDocument("CURRENT")

    # Obtener acceso al data frame por su nombre
    df = arcpy.mapping.ListDataFrames(mxd, dataframe_name)[0]

    # Iterar a través de las capas en el data frame y apagarlas
    for lyr in arcpy.mapping.ListLayers(mxd, "", df):
        lyr.visible = False

    # Actualizar la vista del mapa
    arcpy.RefreshActiveView()

# Llamar a la función y pasar el nombre del data frame 'Layers'
apagacapas("Layers")
