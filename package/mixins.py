#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo contendo classes de mixins para funcionalidades auxiliares.
"""

import os
import sys
import subprocess

class DisplayMixin:
    """
    Mixin que fornece métodos para exibição e formatação no terminal.
    """
    
    def limpar_tela(self):
        """Limpa o terminal."""
        try:
            comando = 'cls' if os.name == 'nt' else 'clear'
            subprocess.run([comando], shell=True, check=True)
        except subprocess.SubprocessError as e:
            LogMixin.aviso(f"Não foi possível limpar a tela: {str(e)}")
    
    def mostrar_forca(self, erros):
        """
        Exibe o desenho da forca baseado no número de erros.
        
        Args:
            erros (int): Número de erros cometidos.
        """
        # Desenhos da forca em ASCII art para cada estágio
        estagios = [
            # 0 erros
            """
              +---+
              |   |
                  |
                  |
                  |
                  |
            =========
            """,
            # 1 erro: cabeça
            """
              +---+
              |   |
              O   |
                  |
                  |
                  |
            =========
            """,
            # 2 erros: cabeça e tronco
            """
              +---+
              |   |
              O   |
              |   |
                  |
                  |
            =========
            """,
            # 3 erros: cabeça, tronco e braço esquerdo
            """
              +---+
              |   |
              O   |
             /|   |
                  |
                  |
            =========
            """,
            # 4 erros: cabeça, tronco e ambos braços
            """
              +---+
              |   |
              O   |
             /|\\  |
                  |
                  |
            =========
            """,
            # 5 erros: cabeça, tronco, ambos braços e perna esquerda
            """
              +---+
              |   |
              O   |
             /|\\  |
             /    |
                  |
            =========
            """,
            # 6 erros: enforcado completo
            """
              +---+
              |   |
              O   |
             /|\\  |
             / \\  |
                  |
            =========
            """
        ]
        
        # Limita o índice ao número de desenhos disponíveis
        indice = min(erros, len(estagios) - 1)
        print(estagios[indice])


class LogMixin:
    """
    Mixin que fornece métodos para logging.
    """
    
    @staticmethod
    def log(mensagem, nivel="INFO"):
        """
        Registra uma mensagem de log.
        
        Args:
            mensagem (str): A mensagem a ser registrada.
            nivel (str): O nível do log (INFO, WARNING, ERROR).
        """
        niveis_validos = ["INFO", "WARNING", "ERROR"]
        if nivel not in niveis_validos:
            nivel = "INFO"
        
        print(f"[{nivel}] {mensagem}", file=sys.stderr)
    
    @staticmethod
    def info(mensagem):
        """
        Registra uma mensagem informativa.
        
        Args:
            mensagem (str): A mensagem a ser registrada.
        """
        LogMixin.log(mensagem, "INFO")
    
    @staticmethod
    def aviso(mensagem):
        """
        Registra uma mensagem de aviso.
        
        Args:
            mensagem (str): A mensagem a ser registrada.
        """
        LogMixin.log(mensagem, "WARNING")
    
    @staticmethod
    def erro(mensagem):
        """
        Registra uma mensagem de erro.
        
        Args:
            mensagem (str): A mensagem a ser registrada.
        """
        LogMixin.log(mensagem, "ERROR")