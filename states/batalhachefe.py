from .state import State
import re

import constantes 

class Batalhachefe(State):
    """
    Comportamento associado à tela Batalha chefe.
    """
    __instance = None
    def __new__(cls):
        if Batalhachefe.__instance is None:
            Batalhachefe.__instance = object.__new__(cls)
        return Batalhachefe.__instance

    def __init__(self):
        self.feedback = True

    def parseAtkNormal(self, bot, msg):
        m = re.search('^Atacado.*', msg)
        if m != None :
            return True
        return False

    def parseMorte(self, bot, msg):
        m = re.search('^Você matou o.*', msg)
        if m != None :
            return True
        return False


    def receive(self, bot, message):
        atacou = False
        if self.parseAtkNormal(bot, message) :
            atacou = True

        if self.parseMorte(bot, message) :
            bot.destino = constantes.DESTINO_FROM_BATALHA_CHEFE_TO_EQUIP
            bot._state = constantes.ESTADOS[constantes.ESTADO_NAVEGANDO]

        if atacou :
            bot.energy = 0
            self.feedback = True

    def act(self, bot):
        print("Act Batalhachefe ...")
    
    
        if bot.energy > 0 :
            return "Atacar Max"
        else :
            bot.destino = constantes.DESTINO_MENU
            bot._state = constantes.ESTADOS[constantes.ESTADO_NAVEGANDO]

        return None
        
