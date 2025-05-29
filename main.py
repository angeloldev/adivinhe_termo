#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ponto de entrada principal para o Jogo da Forca.
Este módulo inicializa e executa o jogo.
"""

from package.jogo import Jogo

def main():
    """Função principal que inicia o jogo."""
    print("=" * 40)
    print("       JOGO DA FORCA - UnB Gama")
    print("=" * 40)
    
    # Inicializa e executa o jogo
    jogo = Jogo()
    jogo.iniciar()

if __name__ == "__main__":
    main()