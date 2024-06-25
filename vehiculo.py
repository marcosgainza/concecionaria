from storage import cargar_datos, guardar_datos

ARCHIVO_VEHICULOS = 'vehiculos.json'

def obtener_vehiculos():
    return cargar_datos(ARCHIVO_VEHICULOS)

def agregar_vehiculo(vehiculo):
    vehiculos = obtener_vehiculos()
    vehiculo['id'] = len(vehiculos) + 1
    vehiculos.append(vehiculo)
    guardar_datos(ARCHIVO_VEHICULOS, vehiculos)

def actualizar_vehiculo(id_vehiculo, vehiculo_actualizado):
    vehiculos = obtener_vehiculos()
    for vehiculo in vehiculos:
        if vehiculo['id'] == id_vehiculo:
            vehiculo.update(vehiculo_actualizado)
            break
    guardar_datos(ARCHIVO_VEHICULOS, vehiculos)

def eliminar_vehiculo(id_vehiculo):
    vehiculos = obtener_vehiculos()
    vehiculos = [v for v in vehiculos if v['id'] != id_vehiculo]
    guardar_datos(ARCHIVO_VEHICULOS, vehiculos)
