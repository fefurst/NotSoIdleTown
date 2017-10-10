from .state import State

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

    def receive(self, bot, message):
        pass

    def act(self, bot):
        print("Act Contrucoes ...")
        bot._state = constantes.ESTADOS[constantes.ESTADO_MENU]
