class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    
    def __init__(self):
        self.cabeza = None
        self.tamaño = 0
        print("Lista enlazada creada")
    
    def insertar_inicio(self, elemento):
        nuevo_nodo = Nodo(elemento)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        self.tamaño += 1
        print(f"'{elemento}' insertado al inicio")
    
    def insertar_final(self, elemento):
        nuevo_nodo = Nodo(elemento)
        
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        
        self.tamaño += 1
        print(f"'{elemento}' insertado al final")
    
    def eliminar(self, elemento):
        if self.cabeza is None:
            print("Lista vacía")
            return False
        
        if self.cabeza.dato == elemento:
            self.cabeza = self.cabeza.siguiente
            self.tamaño -= 1
            print(f"'{elemento}' eliminado")
            return True
        
        actual = self.cabeza
        while actual.siguiente is not None:
            if actual.siguiente.dato == elemento:
                actual.siguiente = actual.siguiente.siguiente
                self.tamaño -= 1
                print(f"'{elemento}' eliminado")
                return True
            actual = actual.siguiente
        
        print(f"'{elemento}' no encontrado")
        return False
    
    def buscar(self, elemento):
        actual = self.cabeza
        posicion = 0
        
        while actual is not None:
            if actual.dato == elemento:
                print(f"'{elemento}' encontrado en posición {posicion}")
                return posicion
            actual = actual.siguiente
            posicion += 1
        
        print(f"'{elemento}' no encontrado")
        return -1
    
    def ver_tamaño(self):
        print(f"Tamaño: {self.tamaño}")
        return self.tamaño
    
    def esta_vacia(self):
        vacia = (self.cabeza is None)
        print(f"¿Vacía? {vacia}")
        return vacia
    
    def mostrar(self):
        if self.cabeza is None:
            print("Lista enlazada: []")
            return
        
        elementos = []
        actual = self.cabeza
        
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        
        print(f"Lista enlazada: {' -> '.join(elementos)} -> None")

def mostrar_menu():
    print("\n--- MENU LISTA ENLAZADA ---")
    print("1. Insertar al inicio")
    print("2. Insertar al final")
    print("3. Eliminar elemento")
    print("4. Buscar elemento")
    print("5. Ver tamaño")
    print("6. Verificar si vacía")
    print("7. Mostrar lista")
    print("8. Salir")

def main():
    lista = ListaEnlazada()
    
    while True:
        mostrar_menu()
        lista.mostrar()
        
        opcion = input("\nOpción: ")
        
        if opcion == "1":
            elemento = input("Elemento: ")
            lista.insertar_inicio(elemento)
        
        elif opcion == "2":
            elemento = input("Elemento: ")
            lista.insertar_final(elemento)
        
        elif opcion == "3":
            elemento = input("Elemento a eliminar: ")
            lista.eliminar(elemento)
        
        elif opcion == "4":
            elemento = input("Elemento a buscar: ")
            lista.buscar(elemento)
        
        elif opcion == "5":
            lista.ver_tamaño()
        
        elif opcion == "6":
            lista.esta_vacia()
        
        elif opcion == "7":
            lista.mostrar()
        
        elif opcion == "8":
            print("Adiós!")
            break
        
        else:
            print("Opción inválida")
        
        input("\nPresiona ENTER...")

if __name__ == "__main__":
    main()