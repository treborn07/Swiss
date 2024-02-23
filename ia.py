import json
from difflib import SequenceMatcher
from textblob import TextBlob
import random

class SimpleChatbot:
    def __init__(self):
        self.data_file = 'conversas.json'
        self.pares = self.carregar_pares()
        self.perguntas_feedback = []

    def carregar_pares(self):
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def salvar_pares(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.pares, file, indent=4)

    def corrigir_ortografia(self, texto):
        return str(TextBlob(texto).correct())

    def similaridade(self, a, b):
        return SequenceMatcher(None, a, b).ratio()

    def encontrar_resposta(self, pergunta):
        for par in self.pares:
            if self.similaridade(pergunta.lower(), par['pergunta'].lower()) > 0.7:
                return par['resposta']
        return None

    def adicionar_par(self, pergunta, resposta):
        novo_par = {'pergunta': pergunta, 'resposta': resposta}
        self.pares.append(novo_par)
        self.salvar_pares()

    def interagir(self):
        print("Olá! Eu sou um chatbot. Vamos conversar!")
        while True:
            pergunta = input("Você: ")
            resposta = self.encontrar_resposta(pergunta)
            if resposta:
                print("ChatBot:", resposta)
            elif 'contar história' in pergunta.lower():
                self.contar_historia_aleatoria()
            else:
                print("ChatBot: Desculpe, não sei responder a essa pergunta.")
                if pergunta not in self.perguntas_feedback:
                    feedback = input("Esta resposta foi útil? (sim/não): ").lower()
                    if feedback == "não":
                        nova_resposta = input("Como você gostaria de responder a esta pergunta? ")
                        self.adicionar_par(pergunta, nova_resposta)
                        print("Obrigado pelo seu feedback! A resposta foi atualizada.")
                    self.perguntas_feedback.append(pergunta)

    def contar_historia_aleatoria(self):
        print("ChatBot: Claro! Aqui está uma história para você:")
        historias = [
            "Era uma vez um reino distante onde vivia um bravo cavaleiro...",
            "Numa floresta encantada, existia um elfo muito curioso...",
            "Numa cidade movimentada, um detetive investigava um misterioso caso..."
        ]
        historia_escolhida = random.choice(historias)
        print(historia_escolhida)

chatbot = SimpleChatbot()
chatbot.interagir()
