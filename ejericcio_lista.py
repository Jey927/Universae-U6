class TDALista:
    
    def __init__(self):
        self._elementos = []
        self._tamaño = 0
        print("Lista creada")
    
    def insertar(self, elemento, posicion=None):
        if posicion is None:
            posicion = self._tamaño
        
        if not (0 <= posicion <= self._tamaño):
            print(f"Error: Posición {posicion} inválida")
            return False
        
        self._elementos.insert(posicion, elemento)
        self._tamaño += 1
        print(f"'{elemento}' insertado en posición {posicion}")
        return True
    
    def eliminar(self, posicion):
        if self.esta_vacia():
            print("Error: Lista vacía")
            return None
        
        if not (0 <= posicion < self._tamaño):
            print(f"Error: Posición {posicion} inválida")
            return None
        
        elemento = self._elementos.pop(posicion)
        self._tamaño -= 1
        print(f"'{elemento}' eliminado")
        return elemento
    
    def obtener(self, posicion):
        if self.esta_vacia():
            print("Error: Lista vacía")
            return None
        
        if not (0 <= posicion < self._tamaño):
            print(f"Error: Posición {posicion} inválida")
            return None
        
        elemento = self._elementos[posicion]
        print(f"Posición {posicion}: '{elemento}'")
        return elemento
    
    def buscar(self, elemento):
        for i in range(self._tamaño):
            if self._elementos[i] == elemento:
                print(f"'{elemento}' encontrado en posición {i}")
                return i
        print(f"'{elemento}' no encontrado")
        return -1
    
    def tamaño(self):
        print(f"Tamaño: {self._tamaño}")
        return self._tamaño
    
    def esta_vacia(self):
        vacia = (self._tamaño == 0)
        print(f"¿Vacía? {vacia}")
        return vacia
    
    def mostrar(self):
        if self._tamaño == 0:
            print("Lista vacía: []")
        else:
            print(f"Lista: {self._elementos}")
            print(f"Posiciones: {list(range(self._tamaño))}")

def mostrar_menu():
    print("\n--- MENU TDA LISTA ---")
    print("1. Insertar elemento")
    print("2. Eliminar elemento")
    print("3. Obtener elemento")
    print("4. Buscar elemento")
    print("5. Ver tamaño")
    print("6. Verificar si vacía")
    print("7. Mostrar lista")
    print("8. Salir")

def main():
    lista = TDALista()
    
    while True:
        mostrar_menu()
        lista.mostrar()
        
        opcion = input("\nOpción: ")
        
        if opcion == "1":
            elemento = input("Elemento: ")
            pos = input("Posición (Enter=final): ")
            if pos:
                lista.insertar(elemento, int(pos))
            else:
                lista.insertar(elemento)
        
        elif opcion == "2":
            if not lista.esta_vacia():
                pos = int(input("Posición: "))
                lista.eliminar(pos)
        
        elif opcion == "3":
            if not lista.esta_vacia():
                pos = int(input("Posición: "))
                lista.obtener(pos)
        
        elif opcion == "4":
            elemento = input("Elemento: ")
            lista.buscar(elemento)
        
        elif opcion == "5":
            lista.tamaño()
        
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