"""
PROGRAMA SIMPLE DE ARREGLO
=========================
Programa básico para agregar elementos y ver el tamaño de un arreglo
"""

# Crear arreglo vacío
mi_arreglo = []

def mostrar_menu():
    """Mostrar opciones disponibles"""
    print("\n--- MENÚ ARREGLO ---")
    print("1. Agregar elemento")
    print("2. Ver tamaño")
    print("3. Mostrar arreglo")
    print("4. Salir")

def agregar_elemento():
    """Agregar elemento al arreglo"""
    elemento = input("Ingresa el elemento: ")
    mi_arreglo.append(elemento)
    print(f"✓ '{elemento}' agregado al arreglo")

def ver_tamaño():
    """Mostrar el tamaño del arreglo"""
    tamaño = len(mi_arreglo)
    print(f" Tamaño del arreglo: {tamaño} elementos")

def mostrar_arreglo():
    """Mostrar contenido del arreglo"""
    if len(mi_arreglo) == 0:
        print("Arreglo vacío: []")
    else:
        print(f"Arreglo: {mi_arreglo}")

# PROGRAMA PRINCIPAL
print("🎯 PROGRAMA DE ARREGLO SIMPLE")

while True:
    mostrar_menu()
    mostrar_arreglo()
    
    opcion = input("\nElige opción (1-4): ")
    
    if opcion == "1":
        agregar_elemento()
    elif opcion == "2":
        ver_tamaño()
    elif opcion == "3":
        mostrar_arreglo()
    elif opcion == "4":
        print("¡Adiós!")
        break
    else:
        print("Opción inválida")
    
    input("\nPresiona ENTER para continuar...")