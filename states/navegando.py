from .state import State

import constantes 

class Navegando(State):
    """
    Comportamento associado à navegação.
    """
    __instance = None
    def __new__(cls):
        if Navegando.__instance is None:
            Navegando.__instance = object.__new__(cls)
        return Navegando.__instance

    def __init__(self):
        self.feedback = True
        self.idx = 0

    def receive(self, bot, message):
        self.idx = self.idx + 1
        if self.idx >= len(bot.destino) :
            self.idx = 0
            ## SETAR O ESTADO DE ACORDO COM O DESTINO
            if bot.destino == constantes.DESTINO_MENU :
                bot._state = constantes.ESTADOS[constantes.ESTADO_MENU]
            elif bot.destino == constantes.DESTINO_EQUIPAMENTO :
                bot._state = constantes.ESTADOS[constantes.ESTADO_EQUIPAMENTO]
            elif bot.destino == constantes.DESTINO_CONSTRUCOES :
                bot._state = constantes.ESTADOS[constantes.ESTADO_CONSTRUCOES]
            elif bot.destino == constantes.DESTINO_BATALHA_CHEFE :
                bot._state = constantes.ESTADOS[constantes.ESTADO_BATALHA_CHEFE]
            elif bot.destino == constantes.DESTINO_BATALHA_ARENA :
                bot._state = constantes.ESTADOS[constantes.ESTADO_BATALHA_ARENA]

            print("Chegou em "+str(bot.destino))
            bot.destino = None

        self.feedback = True

    def act(self, bot):
        if self.feedback and bot.destino != None :
            self.feedback = False
            print ("Walking ... " + str(self.idx))
            print ("ON ... "+str(bot.destino))
            return bot.destino[self.idx]
        #bot._state = constantes.ESTADOS[constantes.ESTADO_EQUIPAMENTO]

