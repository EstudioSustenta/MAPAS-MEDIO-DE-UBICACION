

import arcpy

def zextent(layer_name):
    # Obtener acceso al documento actual
    mxd = arcpy.mapping.MapDocument("CURRENT")
    
    # Obtener acceso a la capa "SISTEMA" por su nombre
    lyr_sistema = arcpy.mapping.ListLayers(mxd, layer_name)[0]
    
    # Obtener la extensión de la capa "SISTEMA"
    extent = lyr_sistema.getExtent()
    
    # Obtener acceso al data frame activo
    df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
    
    # Establecer la extensión del data frame a la extensión de la capa "SISTEMA"
    df.extent = extent
    
    # Actualizar la vista del mapa
    arcpy.RefreshActiveView()