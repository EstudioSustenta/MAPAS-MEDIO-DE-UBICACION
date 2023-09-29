import arcpy

mxd = arcpy.mapping.MapDocument("CURRENT")          # Obtener acceso al documento actual
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]         # Obtener acceso al data frame activo

# --------------------FUNCIÓN PARA APAGAR UNA CAPA--------------------------
def apagacapa(capa_a_apagar):
 
    # Obtener acceso a la capa y apagarla
    capa_uno1 = arcpy.mapping.ListLayers(mxd, capa_a_apagar, df)[0]
    capa_uno1.visible = False
    arcpy.RefreshActiveView()           # Actualizar la vista del mapa


# --------------------FUNCIÓN PARA ENCENDER UNA CAPA--------------------------
def encendercapa(capa_a_encender):
 
    # Obtener acceso a la capa y apagarla
    capa_uno1 = arcpy.mapping.ListLayers(mxd, capa_a_encender, df)[0]
    capa_uno1.visible = True
    arcpy.RefreshActiveView()           # Actualizar la vista del mapa