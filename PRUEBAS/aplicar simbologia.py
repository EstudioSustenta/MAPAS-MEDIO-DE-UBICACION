import arcpy

def aplicar_simbologia(capa, campo_condicion):
    # Obtener el mapa actual
    mxd = arcpy.mapping.MapDocument("CURRENT")
    capa_actual = None

    # Buscar la capa por nombre
    for lyr in arcpy.mapping.ListLayers(mxd):
        if lyr.name == capa:
            capa_actual = lyr
            break

    if capa_actual is None:
        print(f"Capa '{capa}' no encontrada en el mapa.")
        return

    # Crear un objeto simbología para la línea gris obscura sin relleno
    simbolo_linea = arcpy.mapping.Symbol()
    simbolo_linea.color = arcpy.Color(50, 50, 50)  # Color gris oscuro
    simbolo_linea.style = "SOLID"
    simbolo_linea.width = 1

    # Crear un objeto simbología para el símbolo por defecto (sin relleno)
    simbolo_defecto = arcpy.mapping.Symbol()

    # Crear un objeto de clase de simbología
    simbologia = capa_actual.symbology

    # Obtener el índice del campo "NOM_ENT"
    indice_campo = capa_actual.fields.index(campo_condicion)

    with arcpy.da.UpdateCursor(capa_actual, ['SHAPE@', campo_condicion]) as cursor:
        for fila in cursor:
            geometria = fila[0]
            valor_campo = fila[1]

            if valor_campo == "condicion_especifica":
                simbologia.renderer.symbol = simbolo_defecto
            else:
                simbologia.renderer.symbol = simbolo_linea

            cursor.updateRow(fila)
exit()
# Reemplazar 'nombre_de_la_capa' con el nombre de la capa que deseas simbolizar
capa_entrada = 'nombre_de_la_capa'
campo_condicion = "NOM_ENT"

aplicar_simbologia(capa_entrada, campo_condicion)

exit()







import arcpy

def aplicar_simbologia(campo_condicion):
    # Obtener el mapa actual
    mxd = arcpy.mapping.MapDocument("CURRENT")
    capa_actual = arcpy.mapping.ListLayers(mxd)[0]  # Suponiendo que la capa es la primera en la lista

    # Crear un objeto simbología para la línea gris obscura sin relleno
    simbolo_linea = arcpy.Symbol()
    simbolo_linea.color = arcpy.Color(50, 50, 50)  # Color gris oscuro
    simbolo_linea.style = "SOLID"
    simbolo_linea.width = 1

    # Crear un objeto simbología para el símbolo por defecto (sin relleno)
    simbolo_defecto = arcpy.Symbol()

    # Crear un objeto de clase de simbología
    simbologia = capa_actual.symbology

    # Obtener el índice del campo "NOM_ENT"
    indice_campo = capa_actual.fields.index(campo_condicion)

    with arcpy.da.UpdateCursor(capa_actual, ['SHAPE@', campo_condicion]) as cursor:
        for fila in cursor:
            geometria = fila[0]
            valor_campo = fila[1]

            if valor_campo == "condicion_especifica":
                simbologia.renderer.symbol = simbolo_defecto
            else:
                simbologia.renderer.symbol = simbolo_linea

            cursor.updateRow(fila)



# Reemplazar campo_condicion con el nombre del campo en el que deseas verificar la condición
campo_condicion = "NOM_ENT"

aplicar_simbologia(campo_condicion)



import arcpy

def aplicar_simbologia(capa, campo_condicion):
    # Crear un objeto simbología para la línea gris obscura sin relleno
    simbolo_linea = arcpy.Symbol()
    simbolo_linea.color = arcpy.Color(50, 50, 50)  # Color gris oscuro
    simbolo_linea.style = "SOLID"
    simbolo_linea.width = 1

    # Crear un objeto simbología para el símbolo por defecto (sin relleno)
    simbolo_defecto = arcpy.Symbol()

    # Crear un objeto de clase de simbología
    simbologia = arcpy.mapping.Layer(capa).symbology

    # Obtener el índice del campo "NOM_ENT"
    indice_campo = capa.findField(campo_condicion)

    with arcpy.da.UpdateCursor(capa, ['SHAPE@', campo_condicion]) as cursor:
        for fila in cursor:
            geometria = fila[0]
            valor_campo = fila[1]

            if valor_campo == "condicion_especifica":
                simbologia.setRenderer("SimpleRenderer")
                simbologia.renderer.symbol = simbolo_defecto
            else:
                simbologia.setRenderer("SimpleRenderer")
                simbologia.renderer.symbol = simbolo_linea

            cursor.updateRow(fila)

# Reemplazar las rutas de capa y el campo_condicion con los valores adecuados
capa_entrada = r"C:\Ruta\A\Tu\Capa.shp"
campo_condicion = "NOM_ENT"

#aplicar_simbologia(capa_entrada, campo_condicion)
