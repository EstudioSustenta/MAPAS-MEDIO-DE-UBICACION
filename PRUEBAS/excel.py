import xlsxwriter

# Crear un nuevo libro de trabajo (workbook) de Excel
workbook = xlsxwriter.Workbook('d:/nuevo_archivo.xlsx')

# Agregar una hoja de trabajo (worksheet)
worksheet = workbook.add_worksheet()

# Escribir datos en celdas
worksheet.write('A1', 'Hola')
worksheet.write('B1', 'Mundo')

# Cerrar el libro de trabajo
workbook.close()

