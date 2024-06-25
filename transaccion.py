from storage import cargar_datos, guardar_datos

ARCHIVO_TRANSACCIONES = 'transacciones.json'

def obtener_transacciones():
    return cargar_datos(ARCHIVO_TRANSACCIONES)

def agregar_transaccion(transaccion):
    transacciones = obtener_transacciones()
    transaccion['id'] = len(transacciones) + 1
    transacciones.append(transaccion)
    guardar_datos(ARCHIVO_TRANSACCIONES, transacciones)
