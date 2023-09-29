import sys
sys.path.append(r"Q:/09 SISTEMAS INFORMATICOS/GIS_PYTON")  # Agrega la ruta al directorio donde se encuentra el archivo "micodigo.py"

try:
    import micodigo  # Importa el archivo "micodigo.py" como un módulo
except ImportError:
    print("No se pudo importar el archivo 'micodigo.py'.")

#def main():
#    try:
#        micodigo.mi_funcion()  # Llama a una función desde "micodigo.py"
#    except AttributeError:
#        print("La función 'mi_funcion' no se encuentra en 'micodigo.py'.")
#
#if __name__ == "__main__":
#    main()
