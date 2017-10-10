from states.menu import Menu
from states.equipamento import Equipamento
from states.navegando import Navegando
from states.batalhachefe import Batalhachefe
from states.batalhaarena import Batalhaarena
from states.construcoes import Construcoes

DESTINO_MENU = ["Menu 📜"]
DESTINO_EQUIPAMENTO = ["Herói 💂", "Equipamento"]
DESTINO_CONSTRUCOES = ["Construções 🏢"]
DESTINO_BATALHA_CHEFE = ["Batalhar ⚔️", "Chefões 👾"]
DESTINO_BATALHA_ARENA = ["Batalhar ⚔️", "Arena 🏛️"]

ESTADO_MENU = 0
ESTADO_NAVEGANDO = 1
ESTADO_EQUIPAMENTO = 2
ESTADO_CONSTRUCOES = 3
ESTADO_BATALHA_CHEFE = 4
ESTADO_BATALHA_ARENA = 5
ESTADOS = [Menu(), Navegando(), Equipamento(), Construcoes(), Batalhachefe(), Batalhaarena()]
