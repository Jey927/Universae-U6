"""
PROGRAMA INTERACTIVO DE PILA (STACK)
====================================
Menú interactivo para manejar una pila con todas las operaciones básicas.
"""

class Pila:
    """Clase simple para manejar una pila"""
    
    def __init__(self):
        """Crear una pila vacía"""
        self.elementos = []
    
    def push(self, elemento):
        """Insertar elemento en la pila"""
        self.elementos.append(elemento)
        print(f"✓ Elemento '{elemento}' añadido a la pila")
    
    def pop(self):
        """Eliminar y devolver elemento superior"""
        if self.esta_vacia():
            print("❌ Error: La pila está vacía, no se puede eliminar")
            return None
        
        elemento = self.elementos.pop()
        print(f"✓ Elemento '{elemento}' eliminado de la pila")
        return elemento
    
    def esta_vacia(self):
        """Verificar si la pila está vacía"""
        return len(self.elementos) == 0
    
    def tamaño(self):
        """Obtener el tamaño de la pila"""
        return len(self.elementos)
    
    def mostrar_pila(self):
        """Mostrar el contenido actual de la pila"""
        if self.esta_vacia():
            print("📋 Pila vacía: []")
        else:
            print(f"📋 Pila actual: {self.elementos}")
            print(f"   Top (arriba): '{self.elementos[-1]}'")
            print(f"   Tamaño: {len(self.elementos)} elementos")

def mostrar_menu():
    """Mostrar el menú de opciones"""
    print("\n" + "="*50)
    print("           MENÚ DE OPERACIONES DE PILA")
    print("="*50)
    print("1. 📥 Insertar elemento (PUSH)")
    print("2. 📤 Eliminar elemento superior (POP)")
    print("3. 🔍 Verificar si está vacía")
    print("4. 📏 Obtener tamaño de la pila")
    print("5. 👁️  Mostrar contenido de la pila")
    print("6. 🚪 Salir del programa")
    print("="*50)

def main():
    """Función principal del programa"""
    
    # Crear la pila
    mi_pila = Pila()
    
    # Mensaje de bienvenida
    print("🎯 BIENVENIDO AL PROGRAMA DE PILA INTERACTIVO")
    print("Una pila sigue el principio LIFO (Last In, First Out)")
    print("El último elemento en entrar es el primero en salir")
    
    while True:
        # Mostrar menú
        mostrar_menu()
        
        # Mostrar estado actual de la pila
        print(f"\n📊 Estado actual:")
        mi_pila.mostrar_pila()
        
        # Solicitar opción al usuario
        try:
            opcion = input("\n🔸 Selecciona una opción (1-6): ").strip()
            
            if opcion == "1":
                # PUSH - Insertar elemento
                print("\n--- INSERTAR ELEMENTO ---")
                elemento = input("Ingresa el elemento a añadir: ").strip()
                
                if elemento:  # Verificar que no esté vacío
                    mi_pila.push(elemento)
                else:
                    print("❌ Error: No puedes añadir un elemento vacío")
            
            elif opcion == "2":
                # POP - Eliminar elemento superior
                print("\n--- ELIMINAR ELEMENTO SUPERIOR ---")
                elemento_eliminado = mi_pila.pop()
                
                if elemento_eliminado is not None:
                    print(f"🗑️  Elemento eliminado: '{elemento_eliminado}'")
            
            elif opcion == "3":
                # Verificar si está vacía
                print("\n--- VERIFICAR SI ESTÁ VACÍA ---")
                if mi_pila.esta_vacia():
                    print("✅ La pila está VACÍA")
                else:
                    print("❌ La pila NO está vacía")
                    print(f"   Contiene {mi_pila.tamaño()} elementos")
            
            elif opcion == "4":
                # Obtener tamaño
                print("\n--- TAMAÑO DE LA PILA ---")
                tamaño = mi_pila.tamaño()
                print(f"📏 La pila tiene {tamaño} elementos")
                
                if tamaño == 0:
                    print("   (La pila está vacía)")
                elif tamaño == 1:
                    print("   (La pila tiene un solo elemento)")
                else:
                    print(f"   (Desde '{mi_pila.elementos[0]}' hasta '{mi_pila.elementos[-1]}')")
            
            elif opcion == "5":
                # Mostrar contenido
                print("\n--- CONTENIDO DE LA PILA ---")
                if mi_pila.esta_vacia():
                    print("📋 La pila está vacía")
                else:
                    print("📋 Contenido completo de la pila:")
                    print(f"   Elementos: {mi_pila.elementos}")
                    print("   Visualización (top arriba):")
                    
                    # Mostrar pila visualmente
                    for i in range(len(mi_pila.elementos) - 1, -1, -1):
                        if i == len(mi_pila.elementos) - 1:
                            print(f"   ┌─────────────┐")
                            print(f"   │  {mi_pila.elementos[i]:^9}  │ ← Top")
                        else:
                            print(f"   ├─────────────┤")
                            print(f"   │  {mi_pila.elementos[i]:^9}  │")
                    print(f"   └─────────────┘")
            
            elif opcion == "6":
                # Salir del programa
                print("\n--- SALIENDO DEL PROGRAMA ---")
                print("👋 ¡Gracias por usar el programa de pila!")
                
                if not mi_pila.esta_vacia():
                    print(f"📋 Estado final de la pila: {mi_pila.elementos}")
                    print(f"📏 Elementos restantes: {mi_pila.tamaño()}")
                
                print("🔚 Programa terminado")
                break
            
            else:
                # Opción inválida
                print("\n❌ Opción inválida. Por favor selecciona un número del 1 al 6")
            
            # Pausa para que el usuario vea el resultado
            input("\n⏸️  Presiona ENTER para continuar...")
        
        except KeyboardInterrupt:
            # Manejar Ctrl+C
            print("\n\n🛑 Programa interrumpido por el usuario")
            print("👋 ¡Hasta luego!")
            break
        
        except Exception as e:
            # Manejar errores inesperados
            print(f"\n❌ Error inesperado: {e}")
            print("🔄 Intentando continuar...")
            input("\n⏸️  Presiona ENTER para continuar...")

# Ejemplo de uso predefinido (opcional)
def ejemplo_uso():
    """Función que muestra un ejemplo de uso automático"""
    print("\n🎭 DEMOSTRACIÓN AUTOMÁTICA")
    print("-" * 40)
    
    pila_demo = Pila()
    
    # Insertar algunos elementos
    elementos = ["Primero", "Segundo", "Tercero"]
    for elemento in elementos:
        pila_demo.push(elemento)
        pila_demo.mostrar_pila()
        print()
    
    # Verificar tamaño
    print(f"Tamaño actual: {pila_demo.tamaño()}")
    
    # Eliminar elementos
    while not pila_demo.esta_vacia():
        pila_demo.pop()
        pila_demo.mostrar_pila()
        print()
    
    print("¿Está vacía?", pila_demo.esta_vacia())

if __name__ == "__main__":
    # Preguntar al usuario si quiere ver la demo
    print("🚀 PROGRAMA DE PILA INTERACTIVO")
    print("-" * 40)
    
    respuesta = input("¿Quieres ver una demostración automática primero? (s/n): ").strip().lower()
    
    if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
        ejemplo_uso()
        input("\n⏸️  Presiona ENTER para continuar al menú interactivo...")
    
    # Ejecutar el programa principal
    main()