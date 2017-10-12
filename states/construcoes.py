from .state import State
import re

import constantes 

class Construcoes(State):
    """
    Comportamento associado à tela Menu.
    """
    __instance = None
    def __new__(cls):
        if Construcoes.__instance is None:
            Construcoes.__instance = object.__new__(cls)
        return Construcoes.__instance

    def __init__(self):
        self.feedback = True
        self.idxUp = 0
        self.upOrder = ['Arsenal 🛡', 'Serraria 🌳', 'Serraria 🌳', 'Serraria 🌳', 'Serraria 🌳', 'Ferreiro 🗡', 'Mina de Ouro 💰']
        self.insuficiente = False

    def receive(self, bot, message):
        self.insuficiente = False
        m = re.search('.*melhorado com Sucesso.*', message)
        m2 = re.search('^Você não tem.*', message)
        if m != None :
            self.idxUp = self.idxUp + 1
            if self.idxUp >= len(self.upOrder) :
                self.idxUp = 0

            self.insuficiente = False
            self.feedback = True            
        elif m2 != None :
            self.insuficiente = True
            self.feedback = True
            

    def act(self, bot):
        print("Act Contrucoes ...")
        if self.feedback :
            if self.insuficiente :
                self.insuficiente = False
                bot.destino = constantes.DESTINO_MENU
                bot._state = constantes.ESTADOS[constantes.ESTADO_NAVEGANDO]
            else :
                self.feedback = False
                return self.upOrder[self.idxUp]
                
        return None
