
# ENCIENDE UNA CAPA DETERMINADA EN UN GRUPO DEFINIDO
#
import arcpy

def prende(grupo,capaly)
    
    mxd = arcpy.mapping.MapDocument("CURRENT")
    
    # Nombre del grupo y la capa que deseas encender o apagar
    #grupo = "SISTEMA"
    #capaly = "EMAS_22_03"
    
    # Obtén una lista de todas las capas en el mapa
    capas = arcpy.mapping.ListLayers(mxd)
    
    # Enciende o apaga la capa dentro del grupo
    for capa in capas:
        if capa.isGroupLayer and capa.name == grupo:
            for subcapa in capa:
                if subcapa.name == capaly :
                    subcapa.visible = True  # Cambia a False para apagar la capa
                    break  # Termina el bucle interno
            break  # Termina el bucle externo
        
    # Actualizar el proyecto de mapa
    arcpy.RefreshActiveView()
    arcpy.RefreshTOC()