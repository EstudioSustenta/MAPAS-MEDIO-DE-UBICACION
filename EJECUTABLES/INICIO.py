# -*- coding: utf-8 -*-

# ----PROGRAMA PARA SELECCIÓN DE PROYECTO

import sys
import importlib
import tkinter as tk
from tkinter import ttk
import arcpy


# Agrega la ruta del paquete al path de Python
ruta_libreria = "Q:/09 SISTEMAS INFORMATICOS/GIS_PYTON/SOPORTE_GIS"
sys.path.append(ruta_libreria)


gensis = importlib.import_module("LIBRERIA.generacion_sistema")
# reload(gensis)

def ini():

    print("se selecionó el boton 'nuevo proyecto'")

    # VENTANA PARA SELECCIONAR EL PROYECTO

    # Función para mostrar la selección y cerrar la ventana
    def mostrar_seleccion():
        seleccion = entry.get()
        if seleccion:
            print("Selección: " + seleccion)
            ventana.destroy()
            gensis.start(seleccion)


    # Archivo shapefile de entrada
    shapefile = "Y:/0_SIG_PROCESO/ORIGEN/PROYECTOS.shp"

    # Campo 'DESCRIP'
    campo_descrip = "DESCRIP"

    # Leer todos los valores del campo 'DESCRIP' del shapefile
    valores_descrip = [row[0] for row in arcpy.da.SearchCursor(shapefile, [campo_descrip])]
    valores_descrip = sorted(set(valores_descrip))

    # Crear una ventana principal
    ventana = tk.Tk()
    ventana.title("Seleccionar Valor")

    # Obtener las dimensiones de la pantalla
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()

    # Calcular el ancho y alto de la ventana
    nuevo_ancho = 400  # Cambia este valor según tus preferencias
    nuevo_alto = 200  # Cambia este valor según tus preferencias

    # Configurar el tamaño y posición de la ventana
    x = (ancho_pantalla - nuevo_ancho) // 2
    y = (alto_pantalla - nuevo_alto) // 2
    ventana.geometry("{}x{}+{}+{}".format(nuevo_ancho, nuevo_alto, x, y)) # ESTA LÍNEA DEFINE DIMENSIONES Y POSICIÓN DE LA VENTANA

    # Etiqueta con instrucciones
    etiqueta = ttk.Label(ventana, text="Selecciona un valor:")
    etiqueta.pack(padx=20, pady=10)

    # Entry para mostrar los valores y permitir la selección
    # global entry  # Declarar entry como global
    entry = ttk.Combobox(ventana, values=valores_descrip, width=50)
    entry.pack(padx=20)

    # Botón para mostrar la selección
    yboton = 50   # determina la posición en 'y' del botón
    boton_seleccionar = ttk.Button(ventana, text="Seleccionar", command=mostrar_seleccion)
    boton_seleccionar.pack(pady=yboton)

    # Iniciar el bucle principal de la ventana
    ventana.mainloop()


def decision():

    # Función que se ejecuta cuando se hace clic en el botón "Sí"
    def nuevo_proyecto():

        print("SELECCIONAR NUEVO PROYECTO")
        ventana1.destroy()
        ini()

    # Función que se ejecuta cuando se hace clic en el botón "No"
    def proyecto_predefinido():
        ventana1.destroy()
        # arcpy.AddMessage("Proceso no iniciado")
        print("PROCESO CON EL PROYECTO PREDEFINIDO")

    # Crear una ventana1 principal
    ventana1 = tk.Tk()
    ventana1.title("DEFINIR PROYECTO")

    # Obtener las dimensiones actuales de la ventana1
    ventana1_ancho_actual = ventana1.winfo_reqwidth()
    ventana1_alto_actual = ventana1.winfo_reqheight()

    # Multiplicar las dimensiones actuales por 2 para hacer la ventana1 más grande
    nuevo_ancho = ventana1_ancho_actual * 2
    nuevo_alto = ventana1_alto_actual * 1

    # Configurar el tamaño de la ventana1
    ventana1.geometry("{}x{}".format(nuevo_ancho, nuevo_alto))

    # Obtener las dimensiones de la pantalla
    ancho_pantalla = ventana1.winfo_screenwidth()
    alto_pantalla = ventana1.winfo_screenheight()

    # Calcular las coordenadas para centrar la ventana1 en la pantalla
    x = (ancho_pantalla - nuevo_ancho) / 2
    y = (alto_pantalla - nuevo_alto) / 2

    # Configurar la posición de la ventana1 en el centro de la pantalla
    ventana1.geometry("+%d+%d" % (x, y))

    # Etiqueta con la pregunta
    pregunta_label = tk.Label(ventana1, text="¿Definir nuevo proyecto?")
    pregunta_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)  # Alineada en la primera fila

    # Botón "Sí" que llama a la función iniciar_proceso al hacer clic
    si_boton = tk.Button(ventana1, text="Nuevo proyecto", command=nuevo_proyecto)
    si_boton.grid(row=1, column=0, padx=10, pady=10)  # Alineado en la segunda fila, primera columna

    # Botón "No" que llama a la función no_iniciar_proceso al hacer clic
    no_boton = tk.Button(ventana1, text="Proyecto predefinido", command=proyecto_predefinido)
    no_boton.grid(row=1, column=1, padx=10, pady=10)  # Alineado en la segunda fila, segunda columna

    # Iniciar el bucle principal de la ventana1
    ventana1.mainloop()

decision()
# print("\n\nIniciando proceso de generación de mapas")
# mapas = importlib.import_module("LIBRERIA.MAPAS")
# # importlib.import_module("LIBRERIA.MAPAS")
# reload(mapas)
# # mapas.arranque()
# print(u"\n\nFIN DE PROCESO DE GENERACIÓN DE MAPAS")
#mapas()