import arcpy

# Especifica la ruta del shapefile de entrada
input_shapefile = "\\Esnas01\ESUSTENTA\0_SIG_PROCESO\00 GENERAL\\SISTEMA.shp"

# Especifica el nombre del campo que deseas leer
field_name = "ESTADO"

# Crea un objeto cursor para leer los registros del shapefile
with arcpy.da.SearchCursor(input_shapefile, [field_name]) as cursor:
    # Itera a través de los registros
    for row in cursor:
        # Asigna el valor del campo a una variable llamada 'estado'
        estado = row[0]
        # Imprime el valor de la variable 'estado'
        print("El valor de 'estado' es {0}".format(estado))
