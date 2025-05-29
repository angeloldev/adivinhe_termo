#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo contendo a classe Palavra, que representa a palavra a ser adivinhada no jogo.
"""

class Palavra:
    """
    Classe que representa a palavra a ser adivinhada no jogo da forca.
    Implementa encapsulamento para proteger a palavra e o estado das letras reveladas.
    """
    
    def __init__(self, texto):
        """
        Inicializa uma palavra para o jogo.
        
        Args:
            texto (str): A palavra a ser adivinhada.
        """
        self.__texto = texto.upper()
        self.__letras_reveladas = set()
    
    @property
    def texto(self):
        """Retorna o texto da palavra."""
        return self.__texto
    
    def revelar_letra(self, letra):
        """
        Revela uma letra na palavra, se ela existir.
        
        Args:
            letra (str): A letra a ser verificada e revelada.
            
        Returns:
            bool: True se a letra estiver na palavra, False caso contrário.
        """
        letra = letra.upper()
        if letra in self.__texto:
            self.__letras_reveladas.add(letra)
            return True
        return False
    
    def esta_completa(self):
        """
        Verifica se todas as letras da palavra foram reveladas.
        
        Returns:
            bool: True se todas as letras foram reveladas, False caso contrário.
        """
        return all(letra in self.__letras_reveladas for letra in self.__texto)
    
    def mostrar_progresso(self):
        """
        Retorna uma string representando o progresso atual da adivinhação.
        Letras reveladas são mostradas, as demais são substituídas por underscores.
        
        Returns:
            str: Representação do progresso atual.
        """
        return ' '.join(letra if letra in self.__letras_reveladas else '_' for letra in self.__texto)