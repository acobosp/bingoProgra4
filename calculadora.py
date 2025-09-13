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