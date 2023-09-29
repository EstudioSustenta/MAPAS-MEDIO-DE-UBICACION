import arcpy

def expmapa(grupos,capas):
    arcpy.env.overwriteOutput = True
    mxd = arcpy.mapping.MapDocument("current")
    mxd.save
    df = arcpy.mapping.ListDataFrames(mxd,"Layers")[0]
    titulo = arcpy.mapping.ListLayoutElements(mxd,"TEXT_ELEMENT","TITULO")[0]
    tfecha = arcpy.mapping.ListLayoutElements(mxd,"TEXT_ELEMENT","FECHA")[0]
    leyenda = arcpy.mapping.ListLayoutElements(mxd,"LEGEND_ELEMENT","Legend")[0]
    featureClass = r"Y:/0_SIG_PROCESO/00 GENERAL/SISTEMA.shp"
    with arcpy.da.SearchCursor(featureClass,("DESCRIP")) as cursor:
        for row in cursor:
            tit = (row[0])
    print tit
    
    import datetime     # importa módulo para obtener fecha y hora
    from datetime import datetime
    now = datetime.now()
    fecha = str(now.date())
    print fecha

    for grupo in grupos:
        arcpy.mapping.Layer(grupo).visible = True

    arcpy.RefreshActiveView()

    for capa in capas:
    	filename = "Y:/0_SIG_PROCESO/MAPAS/" + capa #+ ".jpg"
    	lyr_capa = arcpy.mapping.ListLayers(mxd,capa,df)[0]
    	lyr_capa.visible = True
    	ext = lyr_capa.getExtent() #
    	df.extent = ext #
    	titulo.text = tit + "\n" + "Mapa de " + capa
        tfecha.text = df.spatialReference.PCSName + " " + df.spatialReference.projectionName + " GMV: " + fecha + " " + str(now.time())
    	ext = lyr_capa.getExtent()
    	df.extent = ext
        if leyenda.elementWidth > 4:
            leyenda.elementWidth = 4
        else: pass
    	arcpy.RefreshActiveView()
    	arcpy.mapping.ExportToJPEG(mxd,filename + ".jpg","page_layout",1024,768,250)
        arcpy.mapping.ExportToPDF(mxd,filename + ".pdf","page_layout",1024,768,350)
    	lyr_capa.visible = False
    	print "Mapa " + capa + " generado satisfactoriamente."

    for grupo in grupos:
        arcpy.mapping.Layer(grupo).visible = False

    arcpy.RefreshActiveView()
    print "Proceso de creación de mapas " + grupos[0] + " terminado."