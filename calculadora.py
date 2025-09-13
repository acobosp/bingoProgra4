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