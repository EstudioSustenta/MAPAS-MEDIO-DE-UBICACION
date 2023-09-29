arcpy.Identity_analysis(
    in_features=r"Y:/0_SIG_PROCESO/00 GENERAL/SISTEMA.shp"
    , identity_features=r"Y:/0_SIG_PROCESO/01 PAIS.mdb/Sistema_Urbano_Nacional"
    , out_feature_class="Y:/0_SIG_PROCESO/MAPAS/TEMPORAL/SISTEMA.shp"
    , join_attributes="ALL"
    , cluster_tolerance=""
    , relationship="NO_RELATIONSHIPS"
    )

