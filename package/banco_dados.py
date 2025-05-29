#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo contendo a classe para gerenciar o banco de dados do jogo.
Implementa associação fraca por meio de leitura/escrita de arquivos.
"""

import os
import json
import pickle
from .mixins import LogMixin

class BancoDados(LogMixin):
    """
    Classe responsável por gerenciar o armazenamento e recuperação de dados do jogo.
    Implementa associação fraca por meio de leitura/escrita de arquivos.
    """
    
    def __init__(self):
        """Inicializa o banco de dados."""
        self.__arquivo_palavras = "palavras.txt"
        self.__arquivo_historico = "historico.pickle"
        
        # Garante que o arquivo de palavras existe
        self.__verificar_arquivo_palavras()
    
    def __verificar_arquivo_palavras(self):
        """Verifica se o arquivo de palavras existe e o cria se necessário."""
        if not os.path.exists(self.__arquivo_palavras):
            self.info(f"Criando arquivo de palavras padrão: {self.__arquivo_palavras}")
            palavras_padrao = [
                "PYTHON", "PROGRAMACAO", "ORIENTACAO", "OBJETOS", "ENCAPSULAMENTO",
                "HERANCA", "POLIMORFISMO", "CLASSE", "METODO", "ATRIBUTO",
                "COMPUTADOR", "ALGORITMO", "VARIAVEL", "CONSTANTE", "FUNCAO",
                "DESENVOLVIMENTO", "SOFTWARE", "INTERFACE", "TERMINAL", "COMPILADOR",
                "INTERPRETADOR", "BIBLIOTECA", "FRAMEWORK", "DEBUGGER", "EXCEPTION",
                "INTERNET", "NAVEGADOR", "SERVIDOR", "CLIENTE", "PROTOCOLO",
                "UNIVERSIDADE", "ESTUDANTE", "PROFESSOR", "APRENDIZADO", "CONHECIMENTO"
            ]
            with open(self.__arquivo_palavras, 'w', encoding='utf-8') as arquivo:
                for palavra in palavras_padrao:
                    arquivo.write(f"{palavra}\n")
    
    def carregar_palavras(self):
        """
        Carrega as palavras do arquivo.
        
        Returns:
            list: Lista de palavras disponíveis.
        """
        try:
            with open(self.__arquivo_palavras, 'r', encoding='utf-8') as arquivo:
                # Lê as palavras, remove espaços em branco e filtra linhas vazias
                palavras = [linha.strip().upper() for linha in arquivo.readlines()]
                palavras = [p for p in palavras if p]
            
            if not palavras:
                self.aviso("Arquivo de palavras vazio ou com formato inválido.")
                return ["PYTHON"]  # Palavra padrão em caso de erro
            
            return palavras
        
        except Exception as e:
            self.erro(f"Erro ao carregar palavras: {str(e)}")
            return ["PYTHON"]  # Palavra padrão em caso de erro
    
    def adicionar_palavra(self, palavra):
        """
        Adiciona uma nova palavra ao banco de palavras.
        
        Args:
            palavra (str): A palavra a ser adicionada.
            
        Returns:
            bool: True se a palavra foi adicionada com sucesso, False caso contrário.
        """
        palavra = palavra.strip().upper()
        
        if not palavra:
            return False
        
        try:
            # Verifica se a palavra já existe
            palavras = self.carregar_palavras()
            if palavra in palavras:
                return False
            
            # Adiciona a palavra
            with open(self.__arquivo_palavras, 'a', encoding='utf-8') as arquivo:
                arquivo.write(f"{palavra}\n")
            
            return True
        
        except Exception as e:
            self.erro(f"Erro ao adicionar palavra: {str(e)}")
            return False
    
    def carregar_historico(self):
        """
        Carrega o histórico de jogos.
        
        Returns:
            list: Lista de registros de jogos anteriores.
        """
        if not os.path.exists(self.__arquivo_historico):
            return []
        
        try:
            with open(self.__arquivo_historico, 'rb') as arquivo:
                historico = pickle.load(arquivo)
            return historico
        
        except Exception as e:
            self.erro(f"Erro ao carregar histórico: {str(e)}")
            return []
    
    def salvar_historico(self, registro):
        """
        Salva um novo registro no histórico de jogos.
        
        Args:
            registro (dict): Informações do jogo a serem salvas.
            
        Returns:
            bool: True se o registro foi salvo com sucesso, False caso contrário.
        """
        try:
            # Carrega o histórico existente
            historico = self.carregar_historico()
            
            # Adiciona o novo registro
            historico.append(registro)
            
            # Salva o histórico atualizado
            with open(self.__arquivo_historico, 'wb') as arquivo:
                pickle.dump(historico, arquivo)
            
            return True
        
        except Exception as e:
            self.erro(f"Erro ao salvar histórico: {str(e)}")
            return False
    
    def exportar_historico_json(self, arquivo_saida="historico.json"):
        """
        Exporta o histórico de jogos para um arquivo JSON.
        
        Args:
            arquivo_saida (str): Nome do arquivo JSON de saída.
            
        Returns:
            bool: True se o histórico foi exportado com sucesso, False caso contrário.
        """
        try:
            historico = self.carregar_historico()
            
            with open(arquivo_saida, 'w', encoding='utf-8') as arquivo:
                json.dump(historico, arquivo, indent=4, ensure_ascii=False)
            
            return True
        
        except Exception as e:
            self.erro(f"Erro ao exportar histórico para JSON: {str(e)}")
            return False