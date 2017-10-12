import time
import random
import re

from .state import State

import constantes 

class Menu(State):
    """
    Comportamento associado à tela Menu.
    """
    __instance = None
    def __new__(cls):
        if Menu.__instance is None:
            Menu.__instance = object.__new__(cls)
        return Menu.__instance
    
    def __init__(self):
        self.feedback = False
        self.tempoEspera = 0
        self.timerConstrucoes = 0
        self.timerEquipamento = 0


    def parse(self, bot, msg):
        m = re.search('^Cidade.*🏙 \(Lvl ([0-9]{1,})\).*', msg)
        if m != None :
            bot.level = int(m.group(1))
            m = re.search('Energia: ([0-9]{1,}).*', msg)
            bot.energy = int(m.group(1))
            m = re.search('Stamina: ([0-9]{1,}).*', msg)
            bot.stamina = int(m.group(1))

            return True
        return False


    def receive(self, bot, message):        
        okMenu = self.parse(bot, message)
        if okMenu :
            self.timerConstrucoes = self.timerConstrucoes + 1
            self.timerEquipamento = self.timerEquipamento + 1
            if int(bot.energy) >= 100 : #random.randrange(70, 100, 5) :
                bot.destino = constantes.DESTINO_BATALHA_CHEFE
                bot._state = constantes.ESTADOS[constantes.ESTADO_NAVEGANDO]

            elif int(bot.stamina) >= random.randrange(3, 5, 1) :
                bot.destino = constantes.DESTINO_BATALHA_ARENA
                bot._state = constantes.ESTADOS[constantes.ESTADO_NAVEGANDO]

            elif self.timerConstrucoes > 30 :
                self.timerConstrucoes = 0
                bot.destino = constantes.DESTINO_CONSTRUCOES
                bot._state = constantes.ESTADOS[constantes.ESTADO_NAVEGANDO]

            elif self.timerEquipamento > 30 :
                self.timerEquipamento = 0
                bot.destino = constantes.DESTINO_EQUIPAMENTO
                bot._state = constantes.ESTADOS[constantes.ESTADO_NAVEGANDO]

            self.feedback = True
                

    def act(self, bot):
        if self.tempoEspera <= 0 :
            self.tempoEspera = random.randrange(45, 95, 1)
            if self.feedback :
                #if random.randrange(1, 7, 1) % 3 == 0: # simula se pesquisa um novo oponente ou aguarda mais um pouco
                """ De tempos em tempos atualizar a tela para atualizar valores do bot """
                print("Act menu ...")
                self.feedback = False
                return "Atualizar 🔄"
            else :
                print ("Ops sem feedback ...")
            
        else :
            self.tempoEspera = self.tempoEspera - 1
            if self.tempoEspera % 10 == 0:
                print ("Esperando ... " + str(self.tempoEspera))

        return None

        #bot._state = constantes.ESTADOS[constantes.ESTADO_EQUIPAMENTO]
        #bot._state.nascimento = "MENU"
