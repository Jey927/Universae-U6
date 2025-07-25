"""
LISTAS ENLAZADAS EN PYTHON - GUÍA COMPLETA PARA PRINCIPIANTES
==============================================================

Una lista enlazada es como una cadena de vagones de tren:
- Cada vagón (nodo) contiene datos y sabe dónde está el siguiente vagón
- No están en posiciones fijas de memoria como los arrays
- Cada nodo "apunta" al siguiente usando una referencia

Diferencias con Arrays:
- Arrays: [A][B][C][D] - elementos consecutivos en memoria
- Listas enlazadas: [A]→[B]→[C]→[D]→None - elementos conectados por referencias
"""

print("=" * 70)
print("CONCEPTOS BÁSICOS DE LISTAS ENLAZADAS")
print("=" * 70)

# 1. CREACIÓN DE UN NODO (LA PIEZA BÁSICA)
print("\n1. ¿QUÉ ES UN NODO?")
print("-" * 25)

class Nodo:
    """
    Un nodo es como una caja que contiene:
    1. Un dato (la información que queremos guardar)
    2. Una referencia al siguiente nodo (como una flecha que apunta al próximo)
    """
    def __init__(self, dato):
        self.dato = dato           # El valor que guarda este nodo
        self.siguiente = None      # Referencia al siguiente nodo (inicialmente None)
    
    def __str__(self):
        """Representación en texto del nodo"""
        return f"[{self.dato}]"

# Crear nodos individuales para demostrar
print("Creando nodos individuales:")
nodo1 = Nodo("A")
nodo2 = Nodo("B")
nodo3 = Nodo("C")

print(f"Nodo 1: {nodo1} - siguiente: {nodo1.siguiente}")
print(f"Nodo 2: {nodo2} - siguiente: {nodo2.siguiente}")
print(f"Nodo 3: {nodo3} - siguiente: {nodo3.siguiente}")

print("\nConectando los nodos manualmente:")
# Conectar manualmente los nodos
nodo1.siguiente = nodo2  # nodo1 apunta a nodo2
nodo2.siguiente = nodo3  # nodo2 apunta a nodo3
# nodo3.siguiente ya es None (fin de la lista)

print(f"Nodo 1: {nodo1} → {nodo1.siguiente}")
print(f"Nodo 2: {nodo2} → {nodo2.siguiente}")
print(f"Nodo 3: {nodo3} → {nodo3.siguiente}")

print("\nVisualización de la lista enlazada:")
print("[A] → [B] → [C] → None")

# 2. CLASE LISTA ENLAZADA COMPLETA
print("\n2. IMPLEMENTACIÓN COMPLETA DE LISTA ENLAZADA:")
print("-" * 50)

class ListaEnlazada:
    """
    Una lista enlazada es una colección de nodos conectados.
    Solo necesitamos saber dónde está el primer nodo (cabeza).
    """
    
    def __init__(self):
        """Inicializar lista vacía"""
        self.cabeza = None    # Al inicio no hay ningún nodo
        self.tamaño = 0      # Contador de elementos
    
    def esta_vacia(self):
        """Verificar si la lista está vacía"""
        return self.cabeza is None
    
    def obtener_tamaño(self):
        """Obtener el número de elementos"""
        return self.tamaño
    
    def insertar_al_inicio(self, dato):
        """
        Insertar un nuevo nodo al inicio de la lista
        Pasos:
        1. Crear un nuevo nodo
        2. El nuevo nodo apunta a la cabeza actual
        3. La cabeza ahora es el nuevo nodo
        """
        print(f"\n--- Insertando '{dato}' al inicio ---")
        
        # Paso 1: Crear nuevo nodo
        nuevo_nodo = Nodo(dato)
        print(f"Paso 1: Creado nuevo nodo {nuevo_nodo}")
        
        # Paso 2: El nuevo nodo apunta a la cabeza actual
        nuevo_nodo.siguiente = self.cabeza
        print(f"Paso 2: Nuevo nodo apunta a: {self.cabeza}")
        
        # Paso 3: Actualizar la cabeza
        self.cabeza = nuevo_nodo
        self.tamaño += 1
        print(f"Paso 3: Nueva cabeza es: {self.cabeza}")
        
        self.mostrar_lista()
    
    def insertar_al_final(self, dato):
        """
        Insertar un nuevo nodo al final de la lista
        Pasos:
        1. Si la lista está vacía, el nuevo nodo es la cabeza
        2. Si no, recorrer hasta el último nodo
        3. Conectar el último nodo al nuevo nodo
        """
        print(f"\n--- Insertando '{dato}' al final ---")
        
        nuevo_nodo = Nodo(dato)
        print(f"Paso 1: Creado nuevo nodo {nuevo_nodo}")
        
        # Si la lista está vacía
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            print("Paso 2: Lista vacía, nuevo nodo es la cabeza")
        else:
            # Recorrer hasta el final
            print("Paso 2: Buscando el último nodo...")
            actual = self.cabeza
            while actual.siguiente is not None:
                print(f"   Visitando nodo: {actual}")
                actual = actual.siguiente
            
            print(f"   Último nodo encontrado: {actual}")
            
            # Conectar el último nodo al nuevo
            actual.siguiente = nuevo_nodo
            print(f"Paso 3: Conectando {actual} → {nuevo_nodo}")
        
        self.tamaño += 1
        self.mostrar_lista()
    
    def insertar_en_posicion(self, dato, posicion):
        """
        Insertar en una posición específica
        """
        print(f"\n--- Insertando '{dato}' en posición {posicion} ---")
        
        if posicion < 0 or posicion > self.tamaño:
            print(f"Error: Posición {posicion} no válida")
            return
        
        # Si es la primera posición, usar insertar_al_inicio
        if posicion == 0:
            self.insertar_al_inicio(dato)
            return
        
        # Si es la última posición, usar insertar_al_final
        if posicion == self.tamaño:
            self.insertar_al_final(dato)
            return
        
        # Inserción en el medio
        nuevo_nodo = Nodo(dato)
        actual = self.cabeza
        
        # Avanzar hasta la posición anterior
        for i in range(posicion - 1):
            print(f"   Avanzando a posición {i}: {actual}")
            actual = actual.siguiente
        
        print(f"   Nodo en posición {posicion-1}: {actual}")
        print(f"   Siguiente nodo: {actual.siguiente}")
        
        # Insertar el nuevo nodo
        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente = nuevo_nodo
        self.tamaño += 1
        
        print(f"   Insertado: {actual} → {nuevo_nodo} → {nuevo_nodo.siguiente}")
        self.mostrar_lista()
    
    def eliminar_por_valor(self, dato):
        """
        Eliminar el primer nodo que contenga el dato especificado
        """
        print(f"\n--- Eliminando '{dato}' ---")
        
        if self.esta_vacia():
            print("Error: La lista está vacía")
            return False
        
        # Si el elemento a eliminar es la cabeza
        if self.cabeza.dato == dato:
            print(f"Eliminando cabeza: {self.cabeza}")
            self.cabeza = self.cabeza.siguiente
            self.tamaño -= 1
            print("Nueva cabeza:", self.cabeza)
            self.mostrar_lista()
            return True
        
        # Buscar el nodo anterior al que queremos eliminar
        actual = self.cabeza
        while actual.siguiente is not None:
            print(f"   Verificando: {actual.siguiente}")
            if actual.siguiente.dato == dato:
                # Encontrado el nodo a eliminar
                nodo_a_eliminar = actual.siguiente
                print(f"   Eliminando: {nodo_a_eliminar}")
                actual.siguiente = nodo_a_eliminar.siguiente
                self.tamaño -= 1
                print(f"   Conexión actualizada: {actual} → {actual.siguiente}")
                self.mostrar_lista()
                return True
            actual = actual.siguiente
        
        print(f"   Elemento '{dato}' no encontrado")
        return False
    
    def buscar(self, dato):
        """
        Buscar un elemento en la lista
        """
        print(f"\n--- Buscando '{dato}' ---")
        
        if self.esta_vacia():
            print("La lista está vacía")
            return -1
        
        actual = self.cabeza
        posicion = 0
        
        while actual is not None:
            print(f"   Posición {posicion}: {actual}")
            if actual.dato == dato:
                print(f"   ¡Encontrado '{dato}' en posición {posicion}!")
                return posicion
            actual = actual.siguiente
            posicion += 1
        
        print(f"   '{dato}' no encontrado en la lista")
        return -1
    
    def obtener_elemento(self, posicion):
        """
        Obtener el elemento en una posición específica
        """
        print(f"\n--- Obteniendo elemento en posición {posicion} ---")
        
        if posicion < 0 or posicion >= self.tamaño:
            print(f"Error: Posición {posicion} no válida")
            return None
        
        actual = self.cabeza
        for i in range(posicion):
            print(f"   Avanzando desde posición {i}: {actual}")
            actual = actual.siguiente
        
        print(f"   Elemento en posición {posicion}: {actual}")
        return actual.dato
    
    def mostrar_lista(self):
        """
        Mostrar toda la lista de forma visual
        """
        if self.esta_vacia():
            print("   Lista: [vacía]")
            return
        
        elementos = []
        actual = self.cabeza
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        
        print(f"   Lista: {' → '.join(elementos)} → None")
        print(f"   Tamaño: {self.tamaño} elementos")
    
    def recorrer_lista(self):
        """
        Recorrer la lista paso a paso mostrando cada nodo
        """
        print("\n--- Recorriendo la lista completa ---")
        
        if self.esta_vacia():
            print("La lista está vacía")
            return
        
        actual = self.cabeza
        posicion = 0
        
        print("Recorrido paso a paso:")
        while actual is not None:
            print(f"   Posición {posicion}: {actual} → {actual.siguiente}")
            actual = actual.siguiente
            posicion += 1
        
        print(f"   Total de nodos visitados: {posicion}")

# 3. DEMOSTRACIÓN PRÁCTICA
print("\n3. DEMOSTRACIÓN PRÁCTICA:")
print("-" * 35)

# Crear una nueva lista enlazada
mi_lista = ListaEnlazada()
print(f"Lista creada. ¿Está vacía? {mi_lista.esta_vacia()}")

# Insertar elementos al inicio
print("\n=== INSERTANDO AL INICIO ===")
mi_lista.insertar_al_inicio("Primero")
mi_lista.insertar_al_inicio("Segundo")
mi_lista.insertar_al_inicio("Tercero")

# Insertar elementos al final
print("\n=== INSERTANDO AL FINAL ===")
mi_lista.insertar_al_final("Último")
mi_lista.insertar_al_final("Muy último")

# Insertar en posición específica
print("\n=== INSERTANDO EN POSICIÓN ESPECÍFICA ===")
mi_lista.insertar_en_posicion("En medio", 2)

# Mostrar estado actual
print("\n=== ESTADO ACTUAL DE LA LISTA ===")
mi_lista.recorrer_lista()

# Buscar elementos
print("\n=== BÚSQUEDAS ===")
mi_lista.buscar("En medio")
mi_lista.buscar("No existe")

# Obtener elementos por posición
print("\n=== ACCESO POR POSICIÓN ===")
mi_lista.obtener_elemento(0)
mi_lista.obtener_elemento(3)
mi_lista.obtener_elemento(10)

# Eliminar elementos
print("\n=== ELIMINACIONES ===")
mi_lista.eliminar_por_valor("Segundo")
mi_lista.eliminar_por_valor("Muy último")
mi_lista.eliminar_por_valor("No existe")

# Estado final
print("\n=== ESTADO FINAL ===")
mi_lista.recorrer_lista()

# 4. COMPARACIÓN CON ARRAYS
print("\n4. COMPARACIÓN: ARRAYS VS LISTAS ENLAZADAS")
print("-" * 55)

def comparar_estructuras():
    print("ARRAYS (Listas de Python):")
    print("✓ Acceso directo por índice: O(1)")
    print("✗ Inserción en el medio: O(n) - hay que mover elementos")
    print("✓ Uso eficiente de memoria")
    print("✓ Buenos para acceso aleatorio")
    
    print("\nLISTAS ENLAZADAS:")
    print("✗ Acceso por índice: O(n) - hay que recorrer")
    print("✓ Inserción en cualquier parte: O(1) si tienes la referencia")
    print("✗ Memoria extra para las referencias")
    print("✓ Buenos para inserción/eliminación frecuente")
    
    # Demostración práctica
    print("\nEjemplo práctico de diferencias:")
    
    # Array - acceso directo
    mi_array = ["A", "B", "C", "D"]
    print(f"Array: {mi_array}")
    print(f"Acceso directo al elemento 2: {mi_array[2]} (inmediato)")
    
    # Lista enlazada - acceso secuencial
    print(f"Lista enlazada: para acceder al elemento 2 hay que:")
    print("   1. Empezar en la cabeza")
    print("   2. Ir al siguiente nodo")
    print("   3. Ir al siguiente nodo")
    print("   4. Ahora estamos en la posición 2")

comparar_estructuras()

# 5. EJERCICIO PRÁCTICO: LISTA DE REPRODUCCIÓN
print("\n5. EJERCICIO PRÁCTICO: LISTA DE REPRODUCCIÓN DE MÚSICA")
print("-" * 65)

class CancionNodo:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista
        self.siguiente = None
    
    def __str__(self):
        return f"{self.titulo} - {self.artista}"

class ListaReproduccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.primera_cancion = None
        self.total_canciones = 0
    
    def agregar_cancion(self, titulo, artista):
        print(f"\n♪ Agregando: {titulo} - {artista}")
        nueva_cancion = CancionNodo(titulo, artista)
        
        if self.primera_cancion is None:
            self.primera_cancion = nueva_cancion
            print("   Primera canción de la playlist")
        else:
            # Agregar al final
            actual = self.primera_cancion
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nueva_cancion
            print("   Agregada al final de la playlist")
        
        self.total_canciones += 1
        self.mostrar_playlist()
    
    def reproducir_siguiente(self):
        if self.primera_cancion is not None:
            cancion_actual = self.primera_cancion
            print(f"\n♪ Reproduciendo: {cancion_actual}")
            
            # Quitar de la lista (simular reproducción)
            self.primera_cancion = self.primera_cancion.siguiente
            self.total_canciones -= 1
            
            print(f"   Canciones restantes: {self.total_canciones}")
            return cancion_actual
        else:
            print("\n♪ Playlist vacía")
            return None
    
    def mostrar_playlist(self):
        print(f"\n   📋 Playlist '{self.nombre}':")
        if self.primera_cancion is None:
            print("   (vacía)")
            return
        
        actual = self.primera_cancion
        posicion = 1
        while actual is not None:
            print(f"   {posicion}. {actual}")
            actual = actual.siguiente
            posicion += 1

# Usar la lista de reproducción
mi_playlist = ListaReproduccion("Mis Favoritas")

# Agregar canciones
mi_playlist.agregar_cancion("Bohemian Rhapsody", "Queen")
mi_playlist.agregar_cancion("Hotel California", "Eagles")
mi_playlist.agregar_cancion("Imagine", "John Lennon")
mi_playlist.agregar_cancion("Stairway to Heaven", "Led Zeppelin")

# Reproducir algunas canciones
print("\n=== REPRODUCIENDO MÚSICA ===")
mi_playlist.reproducir_siguiente()
mi_playlist.reproducir_siguiente()
mi_playlist.mostrar_playlist()

print("\n" + "=" * 70)
print("RESUMEN DE CONCEPTOS CLAVE")
print("=" * 70)
print("1. Lista enlazada = colección de nodos conectados")
print("2. Cada nodo tiene: dato + referencia al siguiente")
print("3. Solo necesitamos conocer el primer nodo (cabeza)")
print("4. Inserción/eliminación eficiente si tienes la referencia")
print("5. Acceso secuencial (no aleatorio como arrays)")
print("6. Útil cuando el tamaño varía mucho y hay muchas inserciones")
print("7. Trade-off: flexibilidad vs velocidad de acceso")