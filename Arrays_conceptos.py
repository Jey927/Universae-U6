"""
ARRAYS EN PYTHON - GUÍA COMPLETA PARA PRINCIPIANTES
===================================================

Un array (en Python llamado "lista") es como una caja con compartimentos numerados
donde puedes guardar diferentes elementos en orden.

Imagina una estantería con cajones numerados: 0, 1, 2, 3, etc.
Cada cajón puede contener un elemento.
"""

print("=" * 60)
print("CONCEPTOS BÁSICOS DE ARRAYS (LISTAS)")
print("=" * 60)

# 1. CREACIÓN DE ARRAYS
print("\n1. CREANDO ARRAYS:")
print("-" * 20)

# Array vacío
mi_array_vacio = []
print(f"Array vacío: {mi_array_vacio}")
print(f"Tipo de dato: {type(mi_array_vacio)}")

# Array con números
numeros = [10, 20, 30, 40, 50]
print(f"Array de números: {numeros}")

# Array con nombres
nombres = ["Ana", "Luis", "María", "Pedro"]
print(f"Array de nombres: {nombres}")

# Array mixto (diferentes tipos de datos)
mixto = [1, "Hola", 3.14, True]
print(f"Array mixto: {mixto}")

# 2. CONCEPTOS FUNDAMENTALES
print("\n2. CONCEPTOS FUNDAMENTALES:")
print("-" * 30)

print("ÍNDICES - Cada elemento tiene una posición (índice):")
print("Array: [10, 20, 30, 40, 50]")
print("Índice: 0   1   2   3   4")
print("        ↑   ↑   ↑   ↑   ↑")
print("       10  20  30  40  50")

# Mostrar cada elemento con su índice
print("\nElementos y sus índices:")
for i in range(len(numeros)):
    print(f"Índice {i}: {numeros[i]}")

# 3. ACCESO A ELEMENTOS
print("\n3. ACCEDIENDO A ELEMENTOS:")
print("-" * 30)

# Acceso por índice positivo
print("Acceso con índices positivos:")
print(f"Primer elemento (índice 0): {numeros[0]}")
print(f"Segundo elemento (índice 1): {numeros[1]}")
print(f"Último elemento (índice 4): {numeros[4]}")

# Acceso por índice negativo (desde el final)
print("\nAcceso con índices negativos:")
print("Array: [10, 20, 30, 40, 50]")
print("Índice: -5  -4  -3  -2  -1")
print(f"Último elemento (índice -1): {numeros[-1]}")
print(f"Penúltimo elemento (índice -2): {numeros[-2]}")

# 4. PROPIEDADES BÁSICAS
print("\n4. PROPIEDADES DEL ARRAY:")
print("-" * 30)

print(f"Array completo: {numeros}")
print(f"Longitud del array: {len(numeros)} elementos")
print(f"Primer elemento: {numeros[0]}")
print(f"Último elemento: {numeros[-1]}")
print(f"¿Está vacío? {len(numeros) == 0}")

# 5. MODIFICACIÓN DE ELEMENTOS
print("\n5. MODIFICANDO ELEMENTOS:")
print("-" * 30)

print(f"Array original: {numeros}")

# Cambiar un elemento específico
numeros[0] = 100  # Cambio paso a paso explicado
print("Cambiando numeros[0] = 100")
print(f"Array después del cambio: {numeros}")

# Cambiar el último elemento
numeros[-1] = 500
print("Cambiando numeros[-1] = 500")
print(f"Array después del cambio: {numeros}")

# 6. AÑADIR ELEMENTOS
print("\n6. AÑADIENDO ELEMENTOS:")
print("-" * 30)

# Restaurar array original para demostración
numeros = [10, 20, 30, 40, 50]
print(f"Array inicial: {numeros}")

# Añadir al final
numeros.append(60)
print("Ejecutando: numeros.append(60)")
print(f"Resultado: {numeros}")
print("Explicación: append() añade el elemento al final del array")

# Insertar en posición específica
numeros.insert(2, 25)
print("\nEjecutando: numeros.insert(2, 25)")
print(f"Resultado: {numeros}")
print("Explicación: insert(2, 25) inserta 25 en la posición 2")
print("Los elementos posteriores se desplazan hacia la derecha")

# 7. ELIMINAR ELEMENTOS
print("\n7. ELIMINANDO ELEMENTOS:")
print("-" * 30)

print(f"Array antes de eliminar: {numeros}")

# Eliminar por valor
elemento_eliminado = numeros.remove(25)
print("Ejecutando: numeros.remove(25)")
print(f"Resultado: {numeros}")
print("Explicación: remove() elimina la primera aparición del valor 25")

# Eliminar por índice
elemento_eliminado = numeros.pop(0)
print(f"\nEjecutando: elemento = numeros.pop(0)")
print(f"Elemento eliminado: {elemento_eliminado}")
print(f"Array resultante: {numeros}")
print("Explicación: pop(0) elimina y devuelve el elemento en índice 0")

# Eliminar último elemento
ultimo = numeros.pop()
print(f"\nEjecutando: ultimo = numeros.pop()")
print(f"Elemento eliminado: {ultimo}")
print(f"Array resultante: {numeros}")
print("Explicación: pop() sin parámetro elimina el último elemento")

# 8. BÚSQUEDA EN ARRAYS
print("\n8. BUSCANDO EN ARRAYS:")
print("-" * 30)

frutas = ["manzana", "banana", "naranja", "uva", "manzana"]
print(f"Array de frutas: {frutas}")

# Verificar si existe un elemento
if "banana" in frutas:
    print("✓ 'banana' está en el array")
else:
    print("✗ 'banana' NO está en el array")

# Encontrar la posición de un elemento
posicion = frutas.index("naranja")
print(f"La posición de 'naranja' es: {posicion}")

# Contar apariciones
cantidad = frutas.count("manzana")
print(f"'manzana' aparece {cantidad} veces en el array")

# 9. RECORRIDO DE ARRAYS
print("\n9. RECORRIENDO ARRAYS:")
print("-" * 30)

print("Método 1 - Recorrido simple:")
for fruta in frutas:
    print(f"  Fruta: {fruta}")

print("\nMétodo 2 - Con índices:")
for i in range(len(frutas)):
    print(f"  Índice {i}: {frutas[i]}")

print("\nMétodo 3 - Con enumerate (índice y valor):")
for indice, fruta in enumerate(frutas):
    print(f"  Posición {indice}: {fruta}")

# 10. OPERACIONES ÚTILES
print("\n10. OPERACIONES ÚTILES:")
print("-" * 30)

calificaciones = [85, 92, 78, 96, 88, 75, 90]
print(f"Calificaciones: {calificaciones}")

# Estadísticas básicas
print(f"Número total de calificaciones: {len(calificaciones)}")
print(f"Calificación más alta: {max(calificaciones)}")
print(f"Calificación más baja: {min(calificaciones)}")
print(f"Suma total: {sum(calificaciones)}")
print(f"Promedio: {sum(calificaciones) / len(calificaciones):.2f}")

# Ordenamiento
print(f"\nCalificaciones originales: {calificaciones}")
calificaciones_ordenadas = sorted(calificaciones)
print(f"Ordenadas (ascendente): {calificaciones_ordenadas}")
calificaciones_desc = sorted(calificaciones, reverse=True)
print(f"Ordenadas (descendente): {calificaciones_desc}")

# 11. SLICING (REBANADAS)
print("\n11. SLICING - OBTENER PARTES DEL ARRAY:")
print("-" * 45)

letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print(f"Array completo: {letras}")
print("Índices:        0   1   2   3   4   5   6")

# Diferentes tipos de slicing
print(f"\nletras[1:4] = {letras[1:4]}")  # Desde índice 1 hasta 3
print("Explicación: Toma elementos desde índice 1 hasta 3 (4 no incluido)")

print(f"\nletras[:3] = {letras[:3]}")    # Desde el inicio hasta índice 2
print("Explicación: Desde el inicio hasta índice 2 (3 no incluido)")

print(f"\nletras[3:] = {letras[3:]}")    # Desde índice 3 hasta el final
print("Explicación: Desde índice 3 hasta el final")

print(f"\nletras[::2] = {letras[::2]}")  # Cada 2 elementos
print("Explicación: Toma cada 2 elementos (paso de 2)")

# 12. COPIA DE ARRAYS
print("\n12. COPIANDO ARRAYS:")
print("-" * 25)

original = [1, 2, 3, 4, 5]
print(f"Array original: {original}")

# Copia por referencia (¡CUIDADO!)
referencia = original
referencia[0] = 999
print(f"Después de modificar 'referencia': original = {original}")
print("¡PROBLEMA! Se modificó el array original también")

# Copia real
original = [1, 2, 3, 4, 5]  # Restaurar
copia_real = original.copy()
copia_real[0] = 888
print(f"\nUsando copy(): original = {original}")
print(f"                copia = {copia_real}")
print("✓ Ahora los arrays son independientes")

# 13. EJERCICIO PRÁCTICO
print("\n13. EJERCICIO PRÁCTICO - LISTA DE COMPRAS:")
print("-" * 50)

def gestionar_lista_compras():
    lista_compras = []
    
    print("Sistema de Lista de Compras")
    print("Vamos a añadir algunos productos...")
    
    # Añadir productos
    productos = ["leche", "pan", "huevos", "queso", "manzanas"]
    for producto in productos:
        lista_compras.append(producto)
        print(f"  ✓ Añadido: {producto}")
        print(f"    Lista actual: {lista_compras}")
    
    print(f"\nLista completa: {lista_compras}")
    print(f"Total de productos: {len(lista_compras)}")
    
    # Simular compra de algunos productos
    print("\nComprando productos...")
    comprados = []
    while lista_compras and len(comprados) < 3:
        producto = lista_compras.pop(0)  # Tomar el primero
        comprados.append(producto)
        print(f"  ✓ Comprado: {producto}")
        print(f"    Pendientes: {lista_compras}")
        print(f"    Comprados: {comprados}")
    
    print(f"\nResumen final:")
    print(f"  Productos comprados: {comprados}")
    print(f"  Productos pendientes: {lista_compras}")

# Ejecutar el ejercicio
gestionar_lista_compras()

print("\n" + "=" * 60)
print("RESUMEN DE CONCEPTOS CLAVE")
print("=" * 60)
print("1. Arrays son colecciones ordenadas de elementos")
print("2. Los índices empiezan en 0")
print("3. Se puede acceder, modificar, añadir y eliminar elementos")
print("4. Son dinámicos (pueden cambiar de tamaño)")
print("5. Pueden contener diferentes tipos de datos")
print("6. Son muy útiles para almacenar y procesar colecciones de datos")