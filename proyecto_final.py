import os

# --- ESTRUCTURAS DE DATOS ---
# Usamos una tupla para valores que no deben cambiar (ej. nombre del negocio)
CONFIGURACION = ("Café Andrómeda", "pedidos.txt")

def mostrar_menu():
    print(f"\n=== SISTEMA DE VENTAS - {CONFIGURACION[0]} ===")
    print("1. Registrar un pedido")
    print("2. Consultar pedidos (Pantalla)")
    print("3. Guardar pedidos en archivo")
    print("4. Leer pedidos desde archivo")
    print("5. Salir")
    return input("Seleccione una opción: ")

def registrar_pedido():
    # Estructura de datos principal: Lista de diccionarios
    pedidos_locales = []
    nombre_cliente = input("Nombre del cliente: ")
    
    continuar = "si"
    while continuar.lower() == "si":
        print("\n--- Nuevo Producto ---")
        nombre_p = input("Producto: ").strip()
        while not nombre_p:
            nombre_p = input("El nombre no puede estar vacío. Producto: ")

        # Manejo de excepciones para entradas numéricas
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad <= 0: raise ValueError
            
            precio = float(input("Precio unitario: "))
            if precio <= 0: raise ValueError
        except ValueError:
            print("Error: Ingrese valores numéricos positivos.")
            continue

        subtotal = cantidad * precio
        
        # Uso de DICCIONARIO para representar cada pedido
        pedido = {
            "cliente": nombre_cliente,
            "producto": nombre_p,
            "cantidad": cantidad,
            "precio": precio,
            "subtotal": subtotal
        }
        pedidos_locales.append(pedido)
        print("¡Producto agregado!")
        
        continuar = input("¿Agregar otro producto? (si/no): ")
    
    return pedidos_locales

def mostrar_total(lista):
    if not lista:
        print("No hay pedidos en la sesión actual.")
        return
    
    print("\n--- RESUMEN DE VENTAS ---")
    gran_total = 0
    for p in lista:
        print(f"Cliente: {p['cliente']} | {p['producto']} (x{p['cantidad']}) - Subtotal: ${p['subtotal']:.2f}")
        gran_total += p['subtotal']
    print(f"TOTAL ACUMULADO: ${gran_total:.2f}")

def guardar_en_archivo(lista):
    try:
        with open(CONFIGURACION[1], "a") as archivo:
            for p in lista:
                # Guardamos formato: cliente,producto,cantidad,precio,subtotal
                linea = f"{p['cliente']},{p['producto']},{p['cantidad']},{p['precio']},{p['subtotal']}\n"
                archivo.write(linea)
        print("Datos guardados exitosamente en", CONFIGURACION[1])
    except Exception as e:
        print(f"Error al guardar: {e}")

def leer_desde_archivo():
    if not os.path.exists(CONFIGURACION[1]):
        print("El archivo no existe o está vacío.")
        return

    print(f"\n--- HISTORIAL DESDE ARCHIVO ({CONFIGURACION[1]}) ---")
    try:
        with open(CONFIGURACION[1], "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                print(f"Cliente: {datos[0]} | Prod: {datos[1]} | Cant: {datos[2]} | Total: ${datos[4]}")
    except FileNotFoundError:
        print("Error: No se encontró el archivo de pedidos.")

# --- FLUJO PRINCIPAL ---
def main():
    pedidos_totales = []
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            nuevos_pedidos = registrar_pedido()
            pedidos_totales.extend(nuevos_pedidos)
        elif opcion == "2":
            mostrar_total(pedidos_totales)
        elif opcion == "3":
            guardar_en_archivo(pedidos_totales)
        elif opcion == "4":
            leer_desde_archivo()
        elif opcion == "5":
            print("Saliendo del sistema... ¡Gracias!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
