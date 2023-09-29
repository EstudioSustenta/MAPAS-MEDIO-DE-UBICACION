#import arcpy
mxd = arcpy.mapping.MapDocument("current")
data_frame = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
layers = arcpy.mapping.ListLayers(mxd)

for layer in layers:
  if layer.isGroupLayer:
    layer.visible = True
  if layer.longName =="Group Name\SubLayer Name":
    layer.visible = True

arcpy.RefreshTOC()
arcpy.RefreshActiveView()