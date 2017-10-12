from .state import State
import re

import constantes 

class Batalhaarena(State):
    """
    Comportamento associado à tela Menu.
    """
    __instance = None
    def __new__(cls):
        if Batalhaarena.__instance is None:
            Batalhaarena.__instance = object.__new__(cls)
        return Batalhaarena.__instance

    def __init__(self):
        self.feedback = True
        self.nivelMaxLimit = 2.0
        self.janela = 10
        self.atacar = False

        self.lastEnemyLevel = None
        self.lastEnemyRank = None
        self.limitLvlRnk = 17.0
        self.limitLvlRnkThreshold = 0.0

        self.wonLastBattle = False

    def parseAtkNormal(self, bot, msg):
        m = re.search('^Ataque Normal.*', msg)
        if m != None :
            #m = re.search('Oponente.* \(Lvl ([0-9]{1,})\).*', msg)
            m = re.search('\(Lvl ([0-9]{1,})\).*', msg)
            self.lastEnemyLevel = int(m.group(1))
            m = re.search('Arena Rank: ([0-9]{1,}).*', msg)
            self.lastEnemyRank = int(m.group(1))
            return True
        return False
    
    def parseDerrota(self, bot, msg):
        m = re.search('^🔴DERROTA🔴.*', msg)
        if m != None :
            self.wonLastBattle = False
            return True
        return False

    def parseVitoria(self, bot, msg):
        m = re.search('^🔵VITÓRIA🔵.*', msg)
        if m != None :
            self.wonLastBattle = True
            return True
        return False

    def doAttack(self, bot):
        if self.lastEnemyLevel <= (bot.level + int(self.nivelMaxLimit)) and self.lastEnemyLevel >= (bot.level + int(self.nivelMaxLimit)) - self.janela :
            if (self.lastEnemyLevel * 100) / self.lastEnemyRank <= (self.limitLvlRnk + self.limitLvlRnkThreshold) :
                return True
        return False


    def receive(self, bot, message):
        if self.parseAtkNormal(bot, message) :
            self.atacar = True
            self.feedback = True
        
        if self.parseDerrota(bot, message) :
            self.nivelMaxLimit = self.nivelMaxLimit - 0.1
            bot.stamina = bot.stamina - 1
#            self.limitLvlRnkThreshold = 0.0
            self.feedback = True
        
        if self.parseVitoria(bot, message) :
            self.nivelMaxLimit = self.nivelMaxLimit + 0.5
            bot.stamina = bot.stamina - 1
            self.limitLvlRnkThreshold = 0.0
            self.feedback = True
        

    def act(self, bot):
        print("Act Batalhaarena ...")
        if bot.stamina > 0 :
            if self.feedback :
                if self.atacar and self.doAttack(bot) :
                    self.atacar = False
                    return 'Atacar ⚔'
                else :
                    self.limitLvlRnkThreshold = self.limitLvlRnkThreshold + 0.4
                    return 'Ataque Normal'
        else :
            bot.destino = constantes.DESTINO_MENU
            bot._state = constantes.ESTADOS[constantes.ESTADO_NAVEGANDO]

        return None
