from telethon import TelegramClient
from telethon.tl.types import UpdateShortChatMessage, UpdateShortMessage, Updates, UpdateNewMessage
import time
import random
import re
from pprint import pprint

from bot import Bot
import constantes

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 99999
api_hash = 'abcdef1234567890abcdef1234567890'
phone = '+5555999998888'

client = TelegramClient('session_name3', api_id, api_hash)
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Digite o código: '))

qtdRecursoAlvo=120
nivelAlvo=47


doAttack=False
doSearchOpponent=True
level=0

context = Bot(constantes.ESTADO_MENU)

def valor(recurso, msg):
    m = re.search(recurso+': ([0-9]*\.[0-9]*) ([K|M])', msg)
    #print(m.group(1))
    #print(m.group(2))
    valor = 0.0
    if m != None:
        valor = float(m.group(1))
        if m.group(2) == 'M':
            valor = valor * 1000    

    return valor

def sprint(string, *args, **kwargs):
    """Safe Print (handle UnicodeEncodeErrors on some terminals)"""
    try:
        print(string, *args, **kwargs)
    except UnicodeEncodeError:
        string = string.encode('utf-8', errors='ignore')\
                       .decode('ascii', errors='ignore')
        print(string, *args, **kwargs)


def update_handler(update_object):
        global doAttack
        global doSearchOpponent
        if isinstance(update_object, UpdateShortMessage):
            if update_object.out:
                sprint('You sent {} to user #{}'.format(
                    update_object.message, update_object.user_id))
            else:
                sprint('[User #{} sent {}]'.format(
                    update_object.user_id, update_object.message))
        elif isinstance(update_object, UpdateShortChatMessage):
            if update_object.out:
                sprint('You sent {} to chat #{}'.format(
                    update_object.message, update_object.chat_id))
            else:
                sprint('[Chat #{}, user #{} sent {}]'.format(
                       update_object.chat_id, update_object.from_id,
			update_object.message))
        elif isinstance(update_object, Updates):
            if len(update_object.updates) > 0:
                if isinstance(update_object.updates[0], UpdateNewMessage):
                    sprint('User #{} sent #{}'.format(
                        update_object.updates[0].message.from_id, update_object.updates[0].message.message))
                    print(update_object)
                    msg=update_object.updates[0].message.message
                    context.receive(msg)
#                    m = re.search('\(Lvl ([0-9]*)\)', msg)
#                    if m != None:
#                        if msg.find("Inimigo Encontrado") > -1 and int(m.group(1)) < nivelAlvo:
#                            if valor("Comida", msg) > qtdRecursoAlvo or \
#                               valor("Madeira", msg) > qtdRecursoAlvo or \
#                               valor("Ouro", msg) > qtdRecursoAlvo:
#                                if valor("Ouro", msg) == valor("Madeira", msg) or \
#                                   valor("Madeira", msg) == valor("Comida", msg) or \
#                                   valor("Ouro", msg) == valor("Comida", msg):
#                                    doAttack=True

#                    doSearchOpponent=True

client.add_update_handler(update_handler)

#tempoAttack=0
while True:
    time.sleep( 1 )
    resp = context.act()
    if resp != None :
        print ("Enviando ... "+ resp)
        client.send_message('@IdleTownBot', resp)
#    if doAttack:
#        doAttack=False
#        tempoAttack=random.randrange(601, 620, 1) # tempo aleatório para o próximo ataque
#        print("Enviando comando")
#        client.send_message('@IdleTownBot', 'Atacar ⚔')
        
#    if tempoAttack <= 0 and doSearchOpponent:
#        if random.randrange(1, 7, 1) % 3 == 0: # simula se pesquisa um novo oponente ou aguarda mais um pouco
#            doSearchOpponent=False
#            client.send_message('@IdleTownBot', 'Jogador Aleatório')
#    elif tempoAttack > 0:  # aguardando a próxima luta, decrementa o contador
#        if tempoAttack % 30 == 0:
#            print("Aguardando a próxima luta ...")
#        tempoAttack=tempoAttack-1
        
    
    
