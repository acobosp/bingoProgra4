import random

class GeneradorBingo:
    def __init__(self, palabra="BINGO", numero_maximo=75):
        """
        Inicializa el generador de Bingo.
        
        Args:
            palabra (str): Palabra para las columnas (debe tener 5 letras únicas)
            numero_maximo (int): Número máximo del juego (múltiplo de 5, entre 50 y 90)
        """
        if len(palabra) != 5:
            raise ValueError("La palabra debe tener exactamente 5 letras")
        
        if len(set(palabra)) != 5:
            raise ValueError("Las letras de la palabra no deben repetirse")
        
        if numero_maximo < 50 or numero_maximo > 90 or numero_maximo % 5 != 0:
            raise ValueError("El número máximo debe ser múltiplo de 5 entre 50 y 90")
        
        self.palabra = palabra.upper()
        self.numero_maximo = numero_maximo
        self.rango_por_columna = numero_maximo // 5

    def generar_tarjeta(self):
        """
        Genera una tarjeta de bingo aleatoria válida.
        
        Returns:
            list: Matriz 5x5 con los números de la tarjeta
        """
        tarjeta = []
    
        # Generar números para cada columna
        for columna in range(5):
            # Calcular el rango de números para esta columna
            inicio = columna * self.rango_por_columna + 1
            fin = (columna + 1) * self.rango_por_columna
            
            # Generar 5 números únicos para esta columna
            numeros_columna = random.sample(range(inicio, fin + 1), 5)
            # Agregar los números a la tarjeta por filas
            for fila in range(5):
                if columna == 0:  # Primera columna, crear nuevas filas
                    tarjeta.append([numeros_columna[fila]])
                else:  # Agregar a filas existentes
                    tarjeta[fila].append(numeros_columna[fila])
        
        # Marcar el centro como espacio libre
        tarjeta[2][2] = "LIBRE"
        
        return tarjeta

    def mostrar_tarjeta(self, tarjeta):
        """
        Muestra la tarjeta de forma bonita en consola.
        
        Args:
            tarjeta (list): Matriz 5x5 con los números de la tarjeta
        """
        # Mostrar encabezado con las letras
        print("  " + "  ".join(self.palabra))
        print("-" * 21)
        
        # Mostrar cada fila
        for fila in tarjeta:
            fila_formateada = []
            for numero in fila:
                if numero == "LIBRE":
                    fila_formateada.append("LIBRE")
                else:
                    fila_formateada.append(f"{numero:2d}")
            print("| " + " | ".join(fila_formateada) + " |")
        
        print("-" * 21)
    
    def validar_tarjeta(self, tarjeta):
        """
        Valida que una tarjeta sea correcta según las reglas del juego.
        
        Args:
            tarjeta (list): Matriz 5x5 con los números de la tarjeta
            
        Returns:
            bool: True si la tarjeta es válida, False en caso contrario
        """
        todos_los_numeros = []
        
        for columna in range(5):
            inicio = columna * self.rango_por_columna + 1
            fin = (columna + 1) * self.rango_por_columna
            
            for fila in range(5):
                numero = tarjeta[fila][columna]
                
                # Saltar el espacio libre
                if numero == "LIBRE":
                    continue
                
                # Verificar que el número esté en el rango correcto
                if numero < inicio or numero > fin:
                    return False
                
                todos_los_numeros.append(numero)
        
        # Verificar que no haya números duplicados
        return len(todos_los_numeros) == len(set(todos_los_numeros))


def crear_bingo_personalizado():
    """
    Función para crear un bingo con configuración personalizada del usuario.
    
    Returns:
        GeneradorBingo: Objeto configurado según las preferencias del usuario
    """
    print("\n=== CONFIGURAR BINGO PERSONALIZADO ===")
    
    while True:
        try:
            palabra = input("Ingresa una palabra de 5 letras únicas (ej: BINGO, PLENO, LUCKY): ").upper().strip()
            numero_max = int(input("Ingresa el número máximo (50, 55, 60, 65, 70, 75, 80, 85, 90): "))
            
            # Intentar crear el objeto con los parámetros del usuario
            bingo = GeneradorBingo(palabra, numero_max)
            print(f"✓ Bingo configurado: {palabra} con números hasta {numero_max}")
            return bingo
            
        except ValueError as e:
            print(f"❌ Error: {e}")
            print("Por favor, inténtalo de nuevo...\n")

def crear_bingo_aleatorio():
    """
    Función para crear un bingo con configuración aleatoria.
    
    Returns:
        GeneradorBingo: Objeto con configuración aleatoria
    """
    # Palabras válidas para escoger aleatoriamente
    palabras_validas = ["BINGO", "PLENO", "LUCKY", "MONEY", "PRIZE"]
    numeros_validos = [50, 55, 60, 65, 70, 75, 80, 85, 90]
    
    palabra_random = random.choice(palabras_validas)
    numero_random = random.choice(numeros_validos)
    
    bingo = GeneradorBingo(palabra_random, numero_random)
    print(f"🎲 Configuración aleatoria: {palabra_random} con números hasta {numero_random}")
    return bingo

def mostrar_menu():
    """
    Muestra el menú principal y maneja la selección del usuario.
    """
    print("=" * 50)
    print("🎯 GENERADOR DE TARJETAS DE BINGO 🎯")
    print("=" * 50)
    print("1. Configuración personalizada")
    print("2. Configuración aleatoria")
    print("3. Usar configuración clásica (BINGO - 75)")
    print("4. Salir")
    print("-" * 50)
    
    while True:
        try:
            opcion = input("Selecciona una opción (1-4): ").strip()
            
            if opcion == "1":
                return crear_bingo_personalizado()
            elif opcion == "2":
                return crear_bingo_aleatorio()
            elif opcion == "3":
                print("📋 Usando configuración clásica: BINGO con 75 números")
                return GeneradorBingo()
            elif opcion == "4":
                print("👋 ¡Gracias por usar el generador de Bingo!")
                return None
            else:
                print("❌ Opción no válida. Por favor, selecciona 1, 2, 3 o 4.")
                
        except KeyboardInterrupt:
            print("\n👋 ¡Hasta luego!")
            return None
