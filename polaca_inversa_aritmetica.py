class Pila:
    """
    Implementación de una pila (stack) usando una lista de Python. La pila sigue el principio LIFO (Last In, First Out).
    """
    def __init__(self):
        # Inicializa una lista vacía para almacenar los elementos
        self.elementos = []
    
    def apilar(self, elemento):
        """ Agrega un elemento al tope de la pila. Operación también conocida como 'push'.
        """
        self.elementos.append(elemento)
    
    def desapilar(self):
        """ Remueve y retorna el elemento del tope de la pila. Operación también conocida como 'pop'. Lanza excepción si la pila está vacía. """
        if self.esta_vacia():
            raise IndexError("❌ No se puede desapilar: la pila está vacía")
        return self.elementos.pop()
    
    def tope(self):
        """ Retorna el elemento del tope sin removerlo de la pila. Operación también conocida como 'peek' o 'top'."""
        if self.esta_vacia():
            raise IndexError("❌ No se puede ver el tope: la pila está vacía")
        return self.elementos[-1]
    
    def esta_vacia(self):
        """Verifica si la pila está vacía"""
        return len(self.elementos) == 0
    
    def tamaño(self):
        """Retorna el número de elementos en la pila"""
        return len(self.elementos)
    
    def mostrar(self):
        """Muestra el contenido de la pila de forma visual"""
        if self.esta_vacia():
            print("📚 Pila vacía: []")
        else:
            print(f"📚 Pila (tope → base): {self.elementos[::-1]}")

class EvaluadorPostfija:
    """
    Clase que evalúa expresiones aritméticas en notación postfija.
    Notación Postfija (Polaca Inversa):
    - Los operadores van DESPUÉS de los operandos
    - Ejemplo: "3 4 +" significa "3 + 4"
    - Ventaja: No necesita paréntesis ni precedencia de operadores
    """
    
    def __init__(self):
        # Conjunto de operadores soportados
        self.operadores = {'+', '-', '*', '/', '^', '**'}
    
    def es_operador(self, token):
        """Verifica si un token es un operador válido"""
        return token in self.operadores
    
    def es_numero(self, token):
        """
        Verifica si un token es un número válido.
        Soporta enteros y decimales (positivos y negativos).
        """
        try:
            float(token)
            return True
        except ValueError:
            return False
    
    def aplicar_operacion(self, operador, operando2, operando1):
        """
        Aplica una operación aritmética entre dos operandos.
        
        IMPORTANTE: El orden de los operandos es crucial:
        - operando1 es el primer operando (se desapila segundo)
        - operando2 es el segundo operando (se desapila primero)
        
        Ejemplo: Para "5 3 -" → operando1=5, operando2=3 → resultado=5-3=2
        """
        try:
            if operador == '+':
                return operando1 + operando2
            elif operador == '-':
                return operando1 - operando2
            elif operador == '*':
                return operando1 * operando2
            elif operador == '/':
                if operando2 == 0:
                    raise ZeroDivisionError("❌ Error: División por cero")
                return operando1 / operando2
            elif operador == '^' or operador == '**':
                return operando1 ** operando2
            else:
                raise ValueError(f"❌ Operador no soportado: {operador}")
        except Exception as e:
            raise ValueError(f"❌ Error en operación {operando1} {operador} {operando2}: {e}")
    
    def evaluar(self, expresion, mostrar_pasos=False):
        """
        Evalúa una expresión en notación postfija.
        
        Algoritmo:
        1. Recorrer la expresión de izquierda a derecha
        2. Si es un número: apilarlo
        3. Si es un operador: desapilar dos operandos, aplicar operación, apilar resultado
        4. Al final, la pila debe contener exactamente un elemento (el resultado)
        """
        # Crear una nueva pila para esta evaluación
        pila = Pila()
        
        # Dividir la expresión en tokens (separados por espacios)
        tokens = expresion.strip().split()
        
        if mostrar_pasos:
            print(f"\n🔍 Evaluando expresión: '{expresion}'")
            print("📝 Pasos de evaluación:")
            print("-" * 50)
        
        paso = 1
        
        # Procesar cada token de la expresión
        for token in tokens:
            if mostrar_pasos:
                print(f"\nPaso {paso}: Procesando '{token}'")
            
            if self.es_numero(token):
                # Es un número: convertir a float y apilar
                numero = float(token)
                pila.apilar(numero)
                
                if mostrar_pasos:
                    print(f"   📥 Número detectado: {numero}")
                    print(f"   ➡️ Apilando: {numero}")
                    pila.mostrar()
            
            elif self.es_operador(token):
                # Es un operador: necesitamos dos operandos
                if pila.tamaño() < 2:
                    raise ValueError(f"❌ Error: Operador '{token}' necesita 2 operandos, pero solo hay {pila.tamaño()} en la pila")
                
                # Desapilar dos operandos (orden importante!)
                operando2 = pila.desapilar()  # Segundo operando (se desapila primero)
                operando1 = pila.desapilar()  # Primer operando (se desapila segundo)
                
                if mostrar_pasos:
                    print(f"   🔧 Operador detectado: {token}")
                    print(f"   ⬆️ Desapilando: {operando2} (segundo operando)")
                    print(f"   ⬆️ Desapilando: {operando1} (primer operando)")
                
                # Aplicar la operación
                resultado = self.aplicar_operacion(token, operando2, operando1)
                
                if mostrar_pasos:
                    print(f"   🧮 Calculando: {operando1} {token} {operando2} = {resultado}")
                
                # Apilar el resultado
                pila.apilar(resultado)
                
                if mostrar_pasos:
                    print(f"   ➡️ Apilando resultado: {resultado}")
                    pila.mostrar()
            
            else:
                # Token no válido
                raise ValueError(f"❌ Token no válido: '{token}'. Solo se permiten números y operadores (+, -, *, /, ^)")
            
            paso += 1
        
        # Verificar que quede exactamente un elemento en la pila
        if pila.tamaño() != 1:
            raise ValueError(f"❌ Error: Expresión mal formada. La pila debe contener exactamente 1 elemento al final, pero contiene {pila.tamaño()}")
        
        # El resultado final es el único elemento que queda en la pila
        resultado_final = pila.desapilar()
        
        if mostrar_pasos:
            print(f"\n✅ Evaluación completada!")
            print(f"🎯 Resultado final: {resultado_final}")
        
        return resultado_final

def mostrar_menu():
    """Muestra el menú principal del programa"""
    print("\n" + "="*60)
    print("🧮 EVALUADOR DE EXPRESIONES POSTFIJAS")
    print("="*60)
    print("1. 📝 Evaluar expresión postfija")
    print("2. 📚 Ver ejemplos de notación postfija")
    print("3. 🎓 Tutorial: ¿Qué es la notación postfija?")
    print("4. 🧪 Ejecutar casos de prueba")
    print("5. 🚪 Salir")
    print("="*60)

def mostrar_tutorial():
    """Explica qué es la notación postfija"""
    print("\n" + "="*60)
    print("🎓 TUTORIAL: NOTACIÓN POSTFIJA (POLACA INVERSA)")
    print("="*60)
    
    print("""
📖 ¿Qué es la notación postfija?
   La notación postfija coloca los operadores DESPUÉS de los operandos.
   
📊 Comparación de notaciones:
   • Infija (normal):    3 + 4
   • Postfija (RPN):     3 4 +
   
✅ Ventajas de la notación postfija:
   • No necesita paréntesis
   • No hay precedencia de operadores
   • Evaluación de izquierda a derecha
   • Perfecta para usar con pilas
   
🔄 Algoritmo de evaluación:
   1. Leer de izquierda a derecha
   2. Si es número → apilar
   3. Si es operador → desapilar 2, operar, apilar resultado
   4. El resultado final queda en la pila
   
📝 Ejemplos paso a paso:
   
   Expresión: "3 4 +"
   Paso 1: Ver "3" → Apilar 3 → Pila: [3]
   Paso 2: Ver "4" → Apilar 4 → Pila: [3, 4]
   Paso 3: Ver "+" → Desapilar 4 y 3 → Calcular 3+4=7 → Apilar 7 → Pila: [7]
   Resultado: 7
   
   Expresión: "5 3 2 * +"
   Paso 1: Ver "5" → Apilar 5 → Pila: [5]
   Paso 2: Ver "3" → Apilar 3 → Pila: [5, 3]
   Paso 3: Ver "2" → Apilar 2 → Pila: [5, 3, 2]
   Paso 4: Ver "*" → Desapilar 2 y 3 → Calcular 3*2=6 → Apilar 6 → Pila: [5, 6]
   Paso 5: Ver "+" → Desapilar 6 y 5 → Calcular 5+6=11 → Apilar 11 → Pila: [11]
   Resultado: 11
   """)

def mostrar_ejemplos():
    """Muestra ejemplos de expresiones postfijas"""
    ejemplos = [
        ("3 4 +", "3 + 4 = 7"),
        ("10 2 -", "10 - 2 = 8"),
        ("5 3 *", "5 * 3 = 15"),
        ("8 4 /", "8 / 4 = 2"),
        ("2 3 ^", "2 ^ 3 = 8"),
        ("5 3 2 * +", "(3 * 2) + 5 = 11"),
        ("15 7 1 1 + - / 3 * 2 1 1 + + -", "Expresión compleja = 5"),
        ("4 2 + 3 5 1 - * +", "(4 + 2) + (3 * (5 - 1)) = 18"),
    ]
    
    print("\n" + "="*60)
    print("📚 EJEMPLOS DE NOTACIÓN POSTFIJA")
    print("="*60)
    
    for i, (postfija, equivalente) in enumerate(ejemplos, 1):
        print(f"\n{i}. Postfija: '{postfija}'")
        print(f"   Equivale a: {equivalente}")

def ejecutar_casos_prueba():
    """Ejecuta casos de prueba automáticos"""
    evaluador = EvaluadorPostfija()
    
    casos_prueba = [
        ("3 4 +", 7),
        ("10 2 -", 8),
        ("5 3 *", 15),
        ("8 4 /", 2),
        ("2 3 ^", 8),
        ("5 3 2 * +", 11),
        ("15 7 1 1 + - / 3 * 2 1 1 + + -", 5),
        ("4 2 + 3 5 1 - * +", 18),
        ("1.5 2.5 +", 4.0),
        ("10 3 / 2 *", 6.666666666666667),
    ]
    
    print("\n" + "="*60)
    print("🧪 EJECUTANDO CASOS DE PRUEBA")
    print("="*60)
    
    exitosos = 0
    total = len(casos_prueba)
    
    for i, (expresion, esperado) in enumerate(casos_prueba, 1):
        try:
            resultado = evaluador.evaluar(expresion)
            if abs(resultado - esperado) < 0.000001:  # Comparación con tolerancia para decimales
                print(f"✅ Caso {i}: '{expresion}' = {resultado} (correcto)")
                exitosos += 1
            else:
                print(f"❌ Caso {i}: '{expresion}' = {resultado} (esperado: {esperado})")
        except Exception as e:
            print(f"❌ Caso {i}: '{expresion}' → Error: {e}")
    
    print(f"\n📊 Resultados: {exitosos}/{total} casos exitosos ({exitosos/total*100:.1f}%)")

def main():
    """Función principal del programa"""
    evaluador = EvaluadorPostfija()
    
    print("🎉 ¡Bienvenido al Evaluador de Expresiones Postfijas!")
    print("Este programa evalúa expresiones aritméticas en notación polaca inversa.")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("👆 Selecciona una opción (1-5): ").strip()
            
            if opcion == "1":
                # Evaluar expresión
                print("\n📝 Evaluación de Expresión Postfija")
                print("-" * 40)
                print("💡 Formato: números y operadores separados por espacios")
                print("💡 Operadores: + - * / ^ (o **)")
                print("💡 Ejemplo: '3 4 +' para evaluar 3 + 4")
                
                expresion = input("\n🔤 Ingresa la expresión postfija: ").strip()
                
                if not expresion:
                    print("❌ No puedes evaluar una expresión vacía")
                    continue
                
                mostrar_pasos = input("🔍 ¿Mostrar pasos detallados? (s/n): ").strip().lower() == 's'
                
                try:
                    resultado = evaluador.evaluar(expresion, mostrar_pasos)
                    print(f"\n🎯 Resultado final: {resultado}")
                    
                    # Formatear el resultado si es un entero
                    if isinstance(resultado, float) and resultado.is_integer():
                        print(f"🎯 Resultado (entero): {int(resultado)}")
                
                except Exception as e:
                    print(f"\n❌ Error al evaluar la expresión: {e}")
            
            elif opcion == "2":
                # Mostrar ejemplos
                mostrar_ejemplos()
            
            elif opcion == "3":
                # Tutorial
                mostrar_tutorial()
            
            elif opcion == "4":
                # Casos de prueba
                ejecutar_casos_prueba()
            
            elif opcion == "5":
                # Salir
                print("\n👋 ¡Gracias por usar el Evaluador de Expresiones Postfijas!")
                print("🎓 ¡Esperamos que hayas aprendido sobre pilas y notación postfija!")
                break
            
            else:
                print("❌ Opción no válida. Por favor selecciona una opción del 1 al 5.")
        
        except KeyboardInterrupt:
            print("\n\n👋 ¡Programa interrumpido por el usuario!")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        
        input("\n⏸️ Presiona Enter para continuar...")

if __name__ == "__main__":
    main()