import arcpy
arcpy.env.overwriteOutput = True
mxd = arcpy.mapping.MapDocument('current')
mxd.save
df = arcpy.mapping.ListDataFrames(mxd,'Layers')[0]
capas = ['CRECIMIENTO_HISTORICO_CD_AGS','Perimetro_de_Contencion_Urbana_2018'
         ,'Delegaciones','ZONAS_URBANAS_DE_FOCALIZACION']
for capa in capas:
    simbologia = 'Y:/0_SIG_PROCESO/MAPAS/SIMBOLOGIA/' + capa + '.lyr'
    lyr_capa = arcpy.mapping.ListLayers(mxd,capa,df)[0]
    lyr_capa1 = lyr_capa.datasetName
    arcpy.ApplySymbologyFromLayer_management(lyr_capa1,simbologia)
    print capa + ' aplicada'