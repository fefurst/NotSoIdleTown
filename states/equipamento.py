from .state import State

import constantes 

class Equipamento(State):
    """
    Comportamento associado à tela Equipamento.
    """
    __instance = None
    def __new__(cls):
        if Equipamento.__instance is None:
            Equipamento.__instance = object.__new__(cls)
        return Equipamento.__instance


    def receive(self, bot, message):
        pass

    def act(self, bot):
        print("Act equipamento ...")
        bot._state = constantes.ESTADOS[constantes.ESTADO_MENU]
