class Nodo:
    """ Clase que representa un nodo de la lista enlazada. Cada nodo contiene un dato y una referencia al siguiente nodo. """
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
class ListaEnlazada:
    """
    Clase que implementa una lista enlazada simple.  Permite agregar, eliminar, buscar y mostrar elementos.
    """
    def __init__(self):
        # Inicializa la lista con la cabeza como None (lista vacía)
        self.cabeza = None
        self.tamaño = 0
    
    def agregar_al_inicio(self, dato):
        """Agrega un nuevo nodo al inicio de la lista"""
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        self.tamaño += 1
        print(f"✅ Elemento '{dato}' agregado al inicio de la lista")
    
    def agregar_al_final(self, dato):
        """Agrega un nuevo nodo al final de la lista"""
        nuevo_nodo = Nodo(dato)
        
        # Si la lista está vacía, el nuevo nodo es la cabeza
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            # Recorre hasta el último nodo
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            # Conecta el último nodo con el nuevo nodo
            actual.siguiente = nuevo_nodo
        
        self.tamaño += 1
        print(f"✅ Elemento '{dato}' agregado al final de la lista")
    
    def eliminar(self, dato):
        """Elimina la primera ocurrencia del dato en la lista"""
        if not self.cabeza:
            print("❌ La lista está vacía")
            return False
        
        # Si el elemento a eliminar es la cabeza
        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            self.tamaño -= 1
            print(f"✅ Elemento '{dato}' eliminado de la lista")
            return True
        
        # Busca el elemento en el resto de la lista
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.dato == dato:
                actual.siguiente = actual.siguiente.siguiente
                self.tamaño -= 1
                print(f"✅ Elemento '{dato}' eliminado de la lista")
                return True
            actual = actual.siguiente
        print(f"❌ Elemento '{dato}' no encontrado en la lista")
        return False
    
    def buscar(self, dato):
        """Busca un elemento en la lista y retorna su posición"""
        actual = self.cabeza
        posicion = 0
        
        while actual:
            if actual.dato == dato:
                print(f"🔍 Elemento '{dato}' encontrado en la posición {posicion}")
                return posicion
            actual = actual.siguiente
            posicion += 1
        
        print(f"❌ Elemento '{dato}' no encontrado en la lista")
        return -1
    
    def mostrar(self):
        """Muestra todos los elementos de la lista"""
        if not self.cabeza:
            print("📋 La lista está vacía")
            return
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        
        print(f"📋 Lista actual: {' -> '.join(elementos)} -> None")
        print(f"📊 Tamaño: {self.tamaño} elementos")
    
    def obtener_tamaño(self):
        """Retorna el tamaño actual de la lista"""
        return self.tamaño
    
    def esta_vacia(self):
        """Verifica si la lista está vacía"""
        return self.cabeza is None

def mostrar_menu():
    """Muestra el menú de opciones disponibles"""
    print("\n" + "="*50)
    print("🔗 SISTEMA DE LISTA ENLAZADA")
    print("="*50)
    print("1. Agregar elemento al inicio")
    print("2. Agregar elemento al final")
    print("3. Eliminar elemento")
    print("4. Buscar elemento")
    print("5. Mostrar lista completa")
    print("6. Mostrar tamaño de la lista")
    print("7. Verificar si está vacía")
    print("8. Salir")
    print("="*50)

def main():
    """Función principal que maneja la interacción con el usuario"""
    # Crear una nueva lista enlazada
    lista = ListaEnlazada()
    
    print("🎉 ¡Bienvenido al sistema de Lista Enlazada!")
    print("Este programa te permite gestionar una lista enlazada de forma interactiva.")
    
    while True:
        mostrar_menu()
        try:
            opcion = input("👆 Selecciona una opción (1-8): ").strip()   
            if opcion == "1":
                # Agregar al inicio
                dato = input("📝 Ingresa el elemento a agregar al inicio: ").strip()
                if dato:
                    lista.agregar_al_inicio(dato)
                else:
                    print("❌ No puedes agregar un elemento vacío")
            elif opcion == "2":
                # Agregar al final
                dato = input("📝 Ingresa el elemento a agregar al final: ").strip()
                if dato:
                    lista.agregar_al_final(dato)
                else:
                    print("❌ No puedes agregar un elemento vacío")
            elif opcion == "3":
                # Eliminar elemento
                if lista.esta_vacia():
                    print("❌ La lista está vacía, no hay elementos para eliminar")
                else:
                    lista.mostrar()  # Mostrar lista actual
                    dato = input("🗑️ Ingresa el elemento a eliminar: ").strip()
                    if dato:
                        lista.eliminar(dato)
                    else:
                        print("❌ No puedes eliminar un elemento vacío")
            elif opcion == "4":
                # Buscar elemento
                if lista.esta_vacia():
                    print("❌ La lista está vacía, no hay elementos para buscar")
                else:
                    dato = input("🔍 Ingresa el elemento a buscar: ").strip()
                    if dato:
                        lista.buscar(dato)
                    else:
                        print("❌ No puedes buscar un elemento vacío")
            elif opcion == "5":
                # Mostrar lista completa
                lista.mostrar()
            elif opcion == "6":
                # Mostrar tamaño
                tamaño = lista.obtener_tamaño()
                print(f"📊 La lista tiene {tamaño} elemento(s)")
            elif opcion == "7":
                # Verificar si está vacía
                if lista.esta_vacia():
                    print("📋 La lista está vacía")
                else:
                    print(f"📋 La lista NO está vacía, tiene {lista.obtener_tamaño()} elemento(s)")
            elif opcion == "8":
                # Salir del programa
                print("👋 ¡Gracias por usar el sistema de Lista Enlazada!")
                print("🔗 Estado final de la lista:")
                lista.mostrar()
                break
            
            else:
                print("❌ Opción no válida. Por favor selecciona una opción del 1 al 8.")
        
        except KeyboardInterrupt:
            print("\n\n👋 ¡Programa interrumpido por el usuario!")
            print("🔗 Estado final de la lista:")
            lista.mostrar()
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        
        # Pausa para que el usuario pueda leer los resultados
        input("\n⏸️ Presiona Enter para continuar...")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
    