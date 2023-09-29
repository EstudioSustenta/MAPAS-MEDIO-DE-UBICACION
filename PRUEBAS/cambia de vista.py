import arcpy

# Obtener acceso al documento actual
mxd = arcpy.mapping.MapDocument("CURRENT")

# Obtener el tipo de vista activa actual ('PAGE_LAYOUT' para vista de diseño, 'DATAFRAME_LAYOUT' para vista de datos)
current_view = mxd.activeView

# Cambiar a la otra vista
if current_view == "PAGE_LAYOUT":
    mxd.activeView = "DATA_LAYOUT"
    print ("ejecutó if")
else:
    print ("ejecutó else")
    mxd.activeView = "PAGE_LAYOUT"

# Actualizar la vista activa
arcpy.RefreshActiveView()

layout.exportToPDF(r"C:\BORRAME\archivo.pdf")

# Liberar los recursos
del mxd