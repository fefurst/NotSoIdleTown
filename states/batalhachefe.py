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

    def receive(self, bot, message):
        if self.parseAtkNormal(bot, message) :
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
        
