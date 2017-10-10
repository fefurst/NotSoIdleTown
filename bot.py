import constantes

class Bot:

    def __init__(self, state):
        self._state = constantes.ESTADOS[state]
        
        self.level = 0
        self.xp = 0
        self.energy = 0
        self.stamina = 0

        self.destino = None

    def receive(self, message):
        self._state.receive(self, message)
    
    def act(self):
        return self._state.act(self)

def main():
    context = Bot(constantes.ESTADO_MENU)
    context.act()
    context.act()
    context.act()
    context.act()


if __name__ == "__main__":
    main()
