import json
import os

def cargar_datos(nombre_archivo):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            return json.load(archivo)
    else:
        with open(nombre_archivo, 'w') as archivo:
            json.dump([], archivo, indent=4)
        return []

def guardar_datos(nombre_archivo, datos):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent=4)
