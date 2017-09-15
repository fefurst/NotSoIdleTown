from telethon import TelegramClient
from telethon.tl.types import UpdateShortChatMessage, UpdateShortMessage, Updates, UpdateNewMessage
import time
import random
import re
from pprint import pprint

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 99999
api_hash = 'abcdef1234567890abcdef1234567890'
phone = '+5555999998888'

client = TelegramClient('session_name', api_id, api_hash, process_updates=True)
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone)
    # .sign_in() may raise PhoneNumberUnoccupiedError
    # In that case, you need to call .sign_up() to get a new account
    client.sign_in(phone, input('Digite o código: '))

#client.send_message('@userrrrr', 'Testando ...')


doAttack=False
doSearchOpponent=True
level=0


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
                sprint('You sent {} to user #{}'.format(update_object.message, update_object.user_id))
            else:
                sprint('[User #{} sent {}]'.format(update_object.user_id, update_object.message))
        elif isinstance(update_object, UpdateShortChatMessage):
            if update_object.out:
                sprint('You sent {} to chat #{}'.format(update_object.message, update_object.chat_id))
            else:
                sprint('[Chat #{}, user #{} sent {}]'.format(update_object.chat_id, update_object.from_id,
			update_object.message))
        elif isinstance(update_object, Updates):
            if len(update_object.updates) > 0:
                if isinstance(update_object.updates[0], UpdateNewMessage):
                    sprint('User #{} sent #{}'.format(
                        update_object.updates[0].message.from_id, update_object.updates[0].message.message))
                    msg=update_object.updates[0].message.message
                    m = re.search('\(Lvl ([0-9]*)\)', msg)
                    if msg.find("Inimigo Encontrado") > -1 and int(m.group(1)) < 36:
                        doAttack=True

                    doSearchOpponent=True

client.add_update_handler(update_handler)

tempoAttack=0
while True:
    time.sleep( 1 )
    if doAttack:
        doAttack=False
        tempoAttack=random.randrange(601, 620, 1) # tempo aleatório para o próximo ataque
        print("Enviando comando")
        client.send_message('@IdleTownBot', 'Atacar ⚔')
        
    if tempoAttack <= 0 and doSearchOpponent:
        if random.randrange(1, 7, 1) % 3 == 0: # simula se pesquisa um novo oponente ou aguarda mais um pouco
            doSearchOpponent=False
            client.send_message('@IdleTownBot', 'Jogador Aleatório')
    elif tempoAttack > 0:  # aguardando a próxima luta, decrementa o contador
        if tempoAttack % 30 == 0:
            print("Aguardando a próxima luta ...")
        tempoAttack=tempoAttack-1
        
    
    
