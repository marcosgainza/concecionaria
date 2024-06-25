import vehiculo
import cliente
import transaccion

def mostrar_menu():
    print("\nMenú de la Concesionaria")
    print("1. Gestión de Vehículos")
    print("2. Gestión de Clientes")
    print("3. Gestión de Transacciones")
    print("4. Salir")

def gestion_vehiculos():
    while True:
        print("\nGestión de Vehículos")
        print("1. Agregar Vehículo")
        print("2. Actualizar Vehículo")
        print("3. Eliminar Vehículo")
        print("4. Ver Vehículos")
        print("5. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        #if opcion == '1':
        match opcion: 
            case 1:
                n_patente = input("Número de Patente: ")
                marca = input("Marca: ")
                modelo = input("Modelo: ")
                tipo = input("Tipo: ")
                año = int(input("Año: "))
                kilometraje = int(input("Kilometraje: "))
                precio_compra = float(input("Precio de Compra: "))
                precio_venta = float(input("Precio de Venta: "))
                estado = input("Estado (Disponible, Reservado, Vendido): ")
                vehiculo.agregar_vehiculo({
                    "n_patente": n_patente,
                    "marca": marca,
                    "modelo": modelo,
                    "tipo": tipo,
                    "año": año,
                    "kilometraje": kilometraje,
                    "precio_compra": precio_compra,
                    "precio_venta": precio_venta,
                    "estado": estado
            }) 
        #elif opcion == '2':
            case 1:
                id_vehiculo = int(input("ID del Vehículo a actualizar: "))
                n_patente = input("Nuevo Número de Patente: ")
                marca = input("Nueva Marca: ")
                modelo = input("Nuevo Modelo: ")
                tipo = input("Nuevo Tipo: ")
                año = int(input("Nuevo Año: "))
                kilometraje = int(input("Nuevo Kilometraje: "))
                precio_compra = float(input("Nuevo Precio de Compra: "))
                precio_venta = float(input("Nuevo Precio de Venta: "))
                estado = input("Nuevo Estado (Disponible, Reservado, Vendido): ")
                vehiculo_actualizado = {
                    "n_patente": n_patente,
                    "marca": marca,
                    "modelo": modelo,
                    "tipo": tipo,
                    "año": año,
                    "kilometraje": kilometraje,
                    "precio_compra": precio_compra,
                    "precio_venta": precio_venta,
                    "estado": estado
            }
                vehiculo.actualizar_vehiculo(id_vehiculo, vehiculo_actualizado)
        #elif opcion == '3':
            case 3:
                id_vehiculo = int(input("ID del Vehículo a eliminar: "))
                vehiculo.eliminar_vehiculo(id_vehiculo)
        #elif opcion == '4':
            case 4:
                vehiculos = vehiculo.obtener_vehiculos()
                for v in vehiculos:
                    print(v)
        #elif opcion == '5':
            case 5:       
                break
        #else:
            case _: 
                print("Opción no válida. Intente de nuevo.")

def gestion_clientes():
    while True:
        print("\nGestión de Clientes")
        print("1. Agregar Cliente")
        print("2. Actualizar Cliente")
        print("3. Eliminar Cliente")
        print("4. Ver Clientes")
        print("5. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre: ")
            documento = input("Documento: ")
            apellido = input("Apellido: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            correo = input("Correo Electrónico: ")
            cliente.agregar_cliente({
                "nombre": nombre,
                "documento": documento,
                "apellido": apellido,
                "direccion": direccion,
                "telefono": telefono,
                "correo": correo
            })
        elif opcion == '2':
            id_cliente = int(input("ID del Cliente a actualizar: "))
            nombre = input("Nuevo Nombre: ")
            documento = input("Nuevo Documento: ")
            apellido = input("Nuevo Apellido: ")
            direccion = input("Nueva Dirección: ")
            telefono = input("Nuevo Teléfono: ")
            correo = input("Nuevo Correo Electrónico: ")
            cliente_actualizado = {
                "nombre": nombre,
                "documento": documento,
                "apellido": apellido,
                "direccion": direccion,
                "telefono": telefono,
                "correo": correo
            }
            cliente.actualizar_cliente(id_cliente, cliente_actualizado)
        elif opcion == '3':
            id_cliente = int(input("ID del Cliente a eliminar: "))
            cliente.eliminar_cliente(id_cliente)
        elif opcion == '4':
            clientes = cliente.obtener_clientes()
            for c in clientes:
                print(c)
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def gestion_transacciones():
    while True:
        print("\nGestión de Transacciones")
        print("1. Registrar Transacción")
        print("2. Ver Transacciones")
        print("3. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_vehiculo = int(input("ID del Vehículo: "))
            id_cliente = int(input("ID del Cliente: "))
            tipo_transaccion = input("Tipo de Transacción (Compra/Venta): ")
            fecha = input("Fecha (YYYY-MM-DD): ")
            monto = float(input("Monto: "))
            observaciones = input("Observaciones: ")
            transaccion.agregar_transaccion({
                "id_vehiculo": id_vehiculo,
                "id_cliente": id_cliente,
                "tipo_transaccion": tipo_transaccion,
                "fecha": fecha,
                "monto": monto,
                "observaciones": observaciones
            })
        elif opcion == '2':
            transacciones = transaccion.obtener_transacciones()
            for t in transacciones:
                print(t)
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            gestion_vehiculos()
        elif opcion == '2':
            gestion_clientes()
        elif opcion == '3':
            gestion_transacciones()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
