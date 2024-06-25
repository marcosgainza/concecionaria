from storage import cargar_datos, guardar_datos

ARCHIVO_CLIENTES = 'clientes.json'

def obtener_clientes():
    return cargar_datos(ARCHIVO_CLIENTES)

def agregar_cliente(cliente):
    clientes = obtener_clientes()
    cliente['id'] = len(clientes) + 1
    clientes.append(cliente)
    guardar_datos(ARCHIVO_CLIENTES, clientes)

def actualizar_cliente(id_cliente, cliente_actualizado):
    clientes = obtener_clientes()
    for cliente in clientes:
        if cliente['id'] == id_cliente:
            cliente.update(cliente_actualizado)
            break
    guardar_datos(ARCHIVO_CLIENTES, clientes)

def eliminar_cliente(id_cliente):
    clientes = obtener_clientes()
    clientes = [c for c in clientes if c['id'] != id_cliente]
    guardar_datos(ARCHIVO_CLIENTES, clientes)
