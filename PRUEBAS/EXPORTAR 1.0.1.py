import arcpy

# Definición de la función expmapa con parámetros grupos y capas
def expmapa(grupos, capas):
    arcpy.env.overwriteOutput = True  # Permitir sobrescribir archivos de salida
    
    mxd = arcpy.mapping.MapDocument("current")  # Acceder al documento actual
    mxd.save()  # Guardar el documento
    
    df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]  # Obtener el primer data frame llamado "Layers"
    
    # Acceder a elementos de diseño por su nombre
    titulo = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT", "TITULO")[0]
    tfecha = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT", "FECHA")[0]
    leyenda = arcpy.mapping.ListLayoutElements(mxd, "LEGEND_ELEMENT", "Legend")[0]
    
    featureClass = r"Y:/0_SIG_PROCESO/00 GENERAL/SISTEMA.shp"  # Ruta al archivo shapefile
    
    # Leer el valor 'DESCRIP' del primer registro en el shapefile
    with arcpy.da.SearchCursor(featureClass, ("DESCRIP")) as cursor:
        for row in cursor:
            tit = (row[0])
    print tit
    
    import datetime  # Importar módulo para obtener fecha y hora
    from datetime import datetime
    now = datetime.now()
    fecha = str(now.date())  # Obtener la fecha actual en formato de cadena
    print fecha
    
    # Hacer visible cada grupo en la lista 'grupos'
    for grupo in grupos:
        arcpy.mapping.Layer(grupo).visible = True
    
    arcpy.RefreshActiveView()  # Actualizar la vista del mapa
    
    # Iterar a través de las capas en la lista 'capas'
    for capa in capas:
        filename = "Y:/0_SIG_PROCESO/MAPAS/" + capa  # Ruta y nombre del archivo
        lyr_capa = arcpy.mapping.ListLayers(mxd, capa, df)[0]  # Obtener la capa por nombre
        lyr_capa.visible = True  # Hacer la capa visible
        ext = lyr_capa.getExtent()  # Obtener la extensión de la capa
        df.extent = ext  # Establecer la extensión del data frame
        titulo.text = tit + "\n" + "Mapa de " + capa  # Actualizar el título
        tfecha.text = df.spatialReference.PCSName + " " + df.spatialReference.projectionName + " GMV: " + fecha + " " + str(now.time())  # Actualizar la fecha
        ext = lyr_capa.getExtent()  # Obtener nuevamente la extensión (¿repetición?)
        df.extent = ext  # Establecer nuevamente la extensión del data frame
        
        # Ajustar el ancho de la leyenda si es mayor que 4
        if leyenda.elementWidth > 4:
            leyenda.elementWidth = 4
        else:
            pass
        
        arcpy.RefreshActiveView()  # Actualizar la vista
        arcpy.mapping.ExportToJPEG(mxd, filename + ".jpg", "page_layout", 1024, 768, 250)  # Exportar a JPEG
        arcpy.mapping.ExportToPDF(mxd, filename + ".pdf", "page_layout", 1024, 768, 350)  # Exportar a PDF
        lyr_capa.visible = False  # Hacer la capa invisible
        print "Mapa " + capa + " generado satisfactoriamente."

    # Hacer invisible cada grupo en la lista 'grupos'
    for grupo in grupos:
        arcpy.mapping.Layer(grupo).visible = False

    arcpy.RefreshActiveView()  # Actualizar la vista
    print "Proceso de creación de mapas " + grupos[0] + " terminado."
