#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo contendo a classe principal do jogo da forca.
"""

import datetime
import random
from .jogador import JogadorHumano
from .palavra import Palavra
from .banco_dados import BancoDados
from .mixins import DisplayMixin

class Jogo(DisplayMixin):
    """
    Classe principal que controla o fluxo do jogo da forca.
    Implementa composição com Palavra e Jogador.
    """
    
    def __init__(self):
        """Inicializa o jogo com valores padrão."""
        self.__banco_dados = BancoDados()
        self.__jogador = None
        self.__palavra = None
        self.__tentativas_max = 6
        self.__tentativas_restantes = self.__tentativas_max
        self.__letras_tentadas = set()
        self.__estado_jogo = "menu"  # Estados: menu, jogando, vitoria, derrota
        self.__data_inicio = None
    
    @property
    def tentativas_restantes(self):
        """Retorna o número de tentativas restantes."""
        return self.__tentativas_restantes
    
    @property
    def letras_tentadas(self):
        """Retorna o conjunto de letras já tentadas."""
        return self.__letras_tentadas
    
    def iniciar(self):
        """Inicia o fluxo principal do jogo."""
        while True:
            if self.__estado_jogo == "menu":
                self._mostrar_menu()
            elif self.__estado_jogo == "jogando":
                self._jogar_rodada()
            elif self.__estado_jogo == "vitoria":
                self._finalizar_jogo(True)
            elif self.__estado_jogo == "derrota":
                self._finalizar_jogo(False)
            elif self.__estado_jogo == "historico":
                self._mostrar_historico()
            elif self.__estado_jogo == "sair":
                print("\nObrigado por jogar! Até a próxima!")
                break
    
    def _mostrar_menu(self):
        """Exibe o menu principal e processa a escolha do jogador."""
        self.limpar_tela()
        print("\n=== MENU PRINCIPAL ===")
        print("1. Novo Jogo")
        print("2. Ver Histórico")
        print("3. Sair")
        
        opcao = input("\nEscolha uma opção (1-3): ").strip()
        
        if opcao == "1":
            self._iniciar_novo_jogo()
        elif opcao == "2":
            self.__estado_jogo = "historico"
        elif opcao == "3":
            self.__estado_jogo = "sair"
        else:
            print("\nOpção inválida! Tente novamente.")
            input("\nPressione ENTER para continuar...")
    
    def _iniciar_novo_jogo(self):
        """Prepara e inicia um novo jogo."""
        self.limpar_tela()
        nome = input("Digite seu nome: ").strip()
        self.__jogador = JogadorHumano(nome)
        
        # Seleciona uma palavra aleatória
        palavras = self.__banco_dados.carregar_palavras()
        palavra_escolhida = random.choice(palavras)
        self.__palavra = Palavra(palavra_escolhida)
        
        # Reinicia o estado do jogo
        self.__tentativas_restantes = self.__tentativas_max
        self.__letras_tentadas = set()
        self.__estado_jogo = "jogando"
        self.__data_inicio = datetime.datetime.now()
        
        # Mostra as instruções
        self.limpar_tela()
        print(f"\nBem-vindo ao Jogo da Forca, {self.__jogador.nome}!")
        print("\nVocê tem 6 tentativas para adivinhar a palavra secreta.")
        print("Boa sorte!\n")
        input("Pressione ENTER para começar...")
    
    def _jogar_rodada(self):
        """Executa uma rodada do jogo."""
        self.limpar_tela()
        
        # Exibe o estado atual do jogo
        self.mostrar_forca(self.__tentativas_max - self.__tentativas_restantes)
        print(f"\nPalavra: {self.__palavra.mostrar_progresso()}")
        print(f"Letras tentadas: {', '.join(sorted(self.__letras_tentadas)) if self.__letras_tentadas else 'Nenhuma'}")
        print(f"Tentativas restantes: {self.__tentativas_restantes}")
        
        # Solicita uma letra ao jogador
        letra = self.__jogador.escolher_letra(self.__letras_tentadas)
        self.__letras_tentadas.add(letra)
        
        # Verifica se a letra está na palavra
        if self.__palavra.revelar_letra(letra):
            print(f"\nBoa! A letra '{letra}' está na palavra.")
        else:
            self.__tentativas_restantes -= 1
            print(f"\nOps! A letra '{letra}' não está na palavra.")
        
        input("\nPressione ENTER para continuar...")
        
        # Verifica se o jogo terminou
        if self.__palavra.esta_completa():
            self.__estado_jogo = "vitoria"
        elif self.__tentativas_restantes <= 0:
            self.__estado_jogo = "derrota"
    
    def _finalizar_jogo(self, vitoria):
        """Finaliza o jogo e salva o resultado no histórico."""
        self.limpar_tela()
        self.mostrar_forca(self.__tentativas_max - self.__tentativas_restantes)
        
        if vitoria:
            print("\n🎉 PARABÉNS! VOCÊ VENCEU! 🎉")
            print(f"Você adivinhou a palavra: {self.__palavra.texto}")
        else:
            print("\n☠️ GAME OVER! VOCÊ PERDEU! ☠️")
            print(f"A palavra era: {self.__palavra.texto}")
        
        # Calcula estatísticas
        tentativas_usadas = len(self.__letras_tentadas)
        duracao = datetime.datetime.now() - self.__data_inicio
        
        print(f"\nEstatísticas:")
        print(f"- Tentativas utilizadas: {tentativas_usadas}")
        print(f"- Letras erradas: {tentativas_usadas - (len(self.__palavra.texto) - len(set(self.__palavra.texto)) + len(set(self.__palavra.texto)))}")
        print(f"- Duração: {duracao.seconds // 60} minutos e {duracao.seconds % 60} segundos")
        
        # Salva no histórico
        resultado = {
            "jogador": self.__jogador.nome,
            "palavra": self.__palavra.texto,
            "resultado": "vitória" if vitoria else "derrota",
            "tentativas": tentativas_usadas,
            "data": self.__data_inicio.strftime("%Y-%m-%d %H:%M:%S"),
            "duracao_segundos": duracao.seconds
        }
        self.__banco_dados.salvar_historico(resultado)
        
        # Pergunta se quer jogar novamente
        print("\nDeseja jogar novamente?")
        print("1. Sim")
        print("2. Não (voltar ao menu)")
        
        opcao = input("\nEscolha uma opção (1-2): ").strip()
        if opcao == "1":
            self._iniciar_novo_jogo()
        else:
            self.__estado_jogo = "menu"
    
    def _mostrar_historico(self):
        """Exibe o histórico de jogos."""
        self.limpar_tela()
        print("\n=== HISTÓRICO DE JOGOS ===\n")
        
        historico = self.__banco_dados.carregar_historico()
        
        if not historico:
            print("Nenhum jogo registrado ainda.")
        else:
            # Exibe os jogos em ordem cronológica inversa (mais recente primeiro)
            for i, jogo in enumerate(reversed(historico), 1):
                print(f"Jogo #{i}:")
                print(f"- Data: {jogo['data']}")
                print(f"- Jogador: {jogo['jogador']}")
                print(f"- Palavra: {jogo['palavra']}")
                print(f"- Resultado: {jogo['resultado']}")
                print(f"- Tentativas: {jogo['tentativas']}")
                
                # Calcula minutos e segundos
                minutos = jogo['duracao_segundos'] // 60
                segundos = jogo['duracao_segundos'] % 60
                print(f"- Duração: {minutos} minutos e {segundos} segundos")
                print("-" * 30)
        
        input("\nPressione ENTER para voltar ao menu...")
        self.__estado_jogo = "menu"