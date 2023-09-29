#RUTINA PARA ASIGNAR VALOR DE CAMPO EN ARCHIVO SHP
# SHP = ARCHIVO EN EL QUE SE HARÁ LA BÚSQUEDA Y CAMBIO SI CORRESPONDE
# CAMPO = NOMBRE DEL CAMPO A VERIFICAR
# VAL = VALOR A ASIGNAR EN EL CAMPO 'CAMPO' SI LA CADENA SE SUSTITUYE
# NULOS = CADENA A BUSCAR PARA SUSTITUIR

def valor(SHP,CAMPO,NULO,VAL,SHPIDEN):
    cursor = arcpy.SearchCursor(SHP)
    for row in cursor:
        SUN = (row.getValue(CAMPO))
        print "valor de campo:" + SUN
    if SUN == NULO:
        #print "fuera de SUN"
        with arcpy.da.UpdateCursor(SHP,CAMPO) as cursor1:
            for row in cursor1:
                row[0] = VAL
                cursor1.updateRow(row)
    print CAMPO + "=" + VAL + ", BUSCADO -" + NULO + "-, ARCHIVO: " +SHP
    NULO == VAL
    del cursor
    archivo = open(r"Y:/0_SIG_PROCESO/MAPAS/DATOS ARCHIVO.TXT","a")
    archivo.write("\n"+ SHPIDEN)
    archivo.write("\n"+ CAMPO)
    archivo.write("\n"+ VAL)
    archivo.close()