import arcpy

arcpy.env.overwriteOutput = True

es_sistema = "Y:/0_SIG_PROCESO/00 GENERAL/SISTEMA_SIMPLIFICADO.shp"
es_buffer = "Y:/0_SIG_PROCESO/00 GENERAL/ESCALAS DE UBICACION.shp"
dist = "50;100;500;1000;2000;5000;10000"
clip_manzanas = "Y:/0_SIG_PROCESO/00 GENERAL/CLIP MANZANAS.shp"
es_manzloc = "Y:/GIS/MEXICO/VARIOS/INEGI/CENSALES/SCINCE 2020/Aguascalientes/cartografia/manzana_localidad.shp"
temporal = "Y:/0_SIG_PROCESO/X TEMPORAL/"


# arcpy.MultipleRingBuffer_analysis(Input_Features=es_sistema, Output_Feature_class=es_buffer, Distances=dist, Buffer_Unit="Meters", Field_Name="radio", Dissolve_Option="ALL", Outside_Polygons_Only="FULL")


arcpy.Buffer_analysis(in_features=es_sistema, out_feature_class=temporal + "Buffer100.shp", buffer_distance_or_field="100 Meters", line_side="FULL", line_end_type="ROUND",
                       dissolve_option="NONE", dissolve_field="", method="PLANAR")
arcpy.Clip_analysis(in_features="Y:/GIS/MEXICO/VARIOS/INEGI/CENSALES/SCINCE 2020/Aguascalientes/cartografia/manzana_localidad.shp", clip_features=es_buffer, out_feature_class=clip_manzanas, cluster_tolerance="")
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "manzana_localidad", "SISTEMA_SIMPLIFICADO_Buffer"
arcpy.Clip_analysis(in_features=es_manzloc, clip_features=es_buffer, out_feature_class=clip_manzanas, cluster_tolerance="")

