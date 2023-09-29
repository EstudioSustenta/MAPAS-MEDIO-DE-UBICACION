import arcpy

def identi(SHPIDEN,SHPOUTPUT):
    import arcpy
    arcpy.env.overwriteOutput = True
    mxd = arcpy.mapping.MapDocument('current')
    df = arcpy.mapping.ListDataFrames(mxd,'Layers')[0]
    arcpy.Identity_analysis(
        in_features=r"Y:/0_SIG_PROCESO/00 GENERAL/SISTEMA.shp"
        ,identity_features=SHPIDEN
        ,out_feature_class=SHPOUTPUT
        , join_attributes="ALL"
        , cluster_tolerance=""
        , relationship="NO_RELATIONSHIPS"
        )