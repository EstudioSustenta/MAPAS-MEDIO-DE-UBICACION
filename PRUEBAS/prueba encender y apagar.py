
import arcpy
    def apaga():
        # Obtén una referencia al proyecto de mapa actual
        mxd = arcpy.mapping.MapDocument("CURRENT")

        # Nombre de la capa que deseas apagar
        nombre_de_la_capa = "EMAS_22-03"

        # Busca la capa en el proyecto de mapa
        capa_objetivo = None
        for capa in arcpy.mapping.ListLayers(mxd):
            if capa.name == nombre_de_la_capa:
                capa_objetivo = capa
                break
            
        # Apaga la capa si se encuentra
        if capa_objetivo:
            capa_objetivo.visible = False

            # Actualiza el proyecto de mapa
            arcpy.RefreshActiveView()
            arcpy.RefreshTOC()

            print("La capa '{capa_objetivo}' ha sido apagada.")

        # No se encontró la capa
        else:
            print("No se encontró la capa '{capa_objetivo}' en el mapa.")
