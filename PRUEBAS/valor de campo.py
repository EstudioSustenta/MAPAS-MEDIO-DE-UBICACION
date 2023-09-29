import arcpy
arcpy.env.overwriteOutput = True
mxd = arcpy.mapping.MapDocument('current')
df = arcpy.mapping.ListDataFrames(mxd,'Layers')[0]
fc = r'Y:\0_SIG_PROCESO\00 GENERAL\MULTIBUFFER.shp'
field = 'DISTANCIA'
cursor = arcpy.SearchCursor(fc)
for row in cursor:
    print(row.getValue(field))