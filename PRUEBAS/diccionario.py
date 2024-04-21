import json

# Diccionario a escribir en el archivo
diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Ciudad de Mexico"
}

# Nombre del archivo donde se escribirá el diccionario
nombre_archivo = "d:/diccionario.json"

def escr():
    # Escribir el diccionario en el archivo como JSON
    with open(nombre_archivo, "w") as archivo:
        json.dump(diccionario, archivo)
    archivo.close
    print("Diccionario escrito en el archivo:", nombre_archivo)


def lee():
    # Leer el contenido del archivo
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()

    # Convertir la cadena JSON a un diccionario
    diccionario = json.loads(contenido)

    # Ahora puedes usar el diccionario como desees
    print(diccionario['nombre'])

if __name__ == '__main__':
    escr()
    lee()
