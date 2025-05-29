#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo contendo as classes relacionadas ao jogador.
Implementa herança e polimorfismo.
"""

class Jogador:
    """
    Classe base para representar um jogador.
    """
    
    def __init__(self, nome):
        """
        Inicializa um jogador.
        
        Args:
            nome (str): Nome do jogador.
        """
        self._nome = nome
        self._tentativas = []
    
    @property
    def nome(self):
        """Retorna o nome do jogador."""
        return self._nome
    
    @property
    def tentativas(self):
        """Retorna as tentativas realizadas pelo jogador."""
        return self._tentativas
    
    def tentar_letra(self, letra):
        """
        Registra uma tentativa de letra.
        
        Args:
            letra (str): A letra tentada.
        """
        self._tentativas.append(letra.upper())
    
    def reset(self):
        """Reinicia as tentativas do jogador."""
        self._tentativas = []


class JogadorHumano(Jogador):
    """
    Classe que representa um jogador humano.
    Herda da classe Jogador e implementa métodos específicos.
    """
    
    def escolher_letra(self, letras_tentadas):
        """
        Solicita ao jogador humano que escolha uma letra.
        
        Args:
            letras_tentadas (set): Conjunto de letras já tentadas.
            
        Returns:
            str: A letra escolhida pelo jogador.
        """
        while True:
            letra = input("\nEscolha uma letra: ").strip().upper()
            
            # Verifica se a entrada é válida
            if not letra:
                print("Por favor, digite uma letra.")
            elif len(letra) > 1:
                print("Por favor, digite apenas uma letra.")
            elif not letra.isalpha():
                print("Por favor, digite uma letra válida.")
            elif letra in letras_tentadas:
                print(f"A letra '{letra}' já foi tentada. Escolha outra.")
            else:
                self.tentar_letra(letra)
                return letra
    
    def jogar(self, jogo):
        """
        Método que implementa a lógica de jogo para um jogador humano.
        
        Args:
            jogo: Referência ao jogo atual.
            
        Returns:
            str: A letra escolhida pelo jogador.
        """
        # Este método demonstra polimorfismo, pois pode ser implementado
        # diferentemente em outras subclasses de Jogador
        return self.escolher_letra(jogo.letras_tentadas)


class JogadorComputador(Jogador):
    """
    Classe que representa um jogador controlado pelo computador.
    Herda da classe Jogador e implementa métodos específicos.
    
    Esta classe é uma extensão que poderia ser implementada futuramente
    para permitir que o computador tente adivinhar palavras.
    """
    
    def __init__(self, nome="Computador", dificuldade="normal"):
        """
        Inicializa um jogador computador.
        
        Args:
            nome (str): Nome do jogador computador.
            dificuldade (str): Nível de dificuldade do jogador computador.
        """
        super().__init__(nome)
        self._dificuldade = dificuldade
        self._alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def escolher_letra(self, letras_tentadas):
        """
        Escolhe uma letra automaticamente.
        
        Args:
            letras_tentadas (set): Conjunto de letras já tentadas.
            
        Returns:
            str: A letra escolhida pelo computador.
        """
        # Implementação básica: escolhe a primeira letra não tentada
        # Poderia ser melhorada com estratégias baseadas em frequência de letras
        for letra in self._alfabeto:
            if letra not in letras_tentadas:
                self.tentar_letra(letra)
                return letra
        return None
    
    def jogar(self, jogo):
        """
        Método que implementa a lógica de jogo para um jogador computador.
        
        Args:
            jogo: Referência ao jogo atual.
            
        Returns:
            str: A letra escolhida pelo computador.
        """
        # Demonstração de polimorfismo: implementação diferente do mesmo método
        letra = self.escolher_letra(jogo.letras_tentadas)
        print(f"\nO computador escolheu a letra: {letra}")
        return letra