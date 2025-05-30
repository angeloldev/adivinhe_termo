import os
import json
import pickle
from .mixins import LogMixin

class BancoDados(LogMixin):

    def __init__(self):
        self.__arquivo_palavras = "palavras.txt"
        self.__arquivo_historico = "historico.pickle"
        
        # Garante que o arquivo de palavras existe
        self.__verificar_arquivo_palavras()
    
    def __verificar_arquivo_palavras(self):
        if not os.path.exists(self.__arquivo_palavras):
            self.info(f"Criando arquivo de palavras padrão: {self.__arquivo_palavras}")
            palavras_padrao = [
                "PYTHON", "PROGRAMACAO", "ORANGOTANGO", "GORILA", "CACHORRO",
                "FLAMENGO", "PALMEIRAS", "BARCELONA", "CRUZEIRO", "SANTOS",
                "COMPUTADOR", "ALGORITMO", "NOTEBOOK", "ARANHA", "ARIRANHA",
                "TELEVISAO", "SOFTWARE", "ARMARIO", "CORTINA", "ELEVADOR",
                "GUITARRA", "TROMPETE", "SAXOFONE", "TECLADO", "FLAUTA",
                "INTERNET", "MOLDURA", "CHOCOLATE", "BRIGADEIRO", "TRANSPORTE",
                "UNIVERSIDADE", "BRASILIA", "PROFESSOR", "GARRAFA", "JESUS"
            ]
            with open(self.__arquivo_palavras, 'w', encoding='utf-8') as arquivo:
                for palavra in palavras_padrao:
                    arquivo.write(f"{palavra}\n")
    
    def carregar_palavras(self):
        try:
            with open(self.__arquivo_palavras, 'r', encoding='utf-8') as arquivo:
                # Lê as palavras, remove espaços em branco e filtra linhas vazias
                palavras = [linha.strip().upper() for linha in arquivo.readlines()]
                palavras = [p for p in palavras if p]
            
            if not palavras:
                self.aviso("Arquivo de palavras vazio ou com formato inválido.")
                return ["PYTHON"]
            
            return palavras
        
        except Exception as e:
            self.erro(f"Erro ao carregar palavras: {str(e)}")
            return ["PYTHON"]
    
    def adicionar_palavra(self, palavra):
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
        try:
            historico = self.carregar_historico()
            
            with open(arquivo_saida, 'w', encoding='utf-8') as arquivo:
                json.dump(historico, arquivo, indent=4, ensure_ascii=False)
            
            return True
        
        except Exception as e:
            self.erro(f"Erro ao exportar histórico para JSON: {str(e)}")
            return False