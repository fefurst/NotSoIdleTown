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


context = Bot(constantes.ESTADO_MENU)

def valor(recurso, msg):
    m = re.search(recurso+': ([0-9]*\.[0-9]*) ([K|M])', msg)
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

def checkUser(id) :
    if id == 271141703 :
        return True
    return False

def update_handler(update_object):
    global doAttack
    global doSearchOpponent
    if isinstance(update_object, UpdateShortMessage) :
        if checkUser(update_object.user_id) :
            #print(update_object)
            if update_object.out:
                sprint('1 You sent {} to user #{}'.format(update_object.message, update_object.user_id))
            else:
                sprint('2 [User #{} sent {}]'.format(update_object.user_id, update_object.message))
                context.receive(update_object.message)
    elif isinstance(update_object, UpdateShortChatMessage):
        if update_object.out:
            sprint('3 You sent {} to chat #{}'.format(update_object.message, update_object.chat_id))
        else:
            sprint('4 [Chat #{}, user #{} sent {}]'.format(update_object.chat_id, update_object.from_id, update_object.message))
    elif isinstance(update_object, Updates):
        if len(update_object.updates) > 0:
            if isinstance(update_object.updates[0], UpdateNewMessage):
                if checkUser(update_object.updates[0].message.from_id) :
                    sprint('5 User #{} sent #{}'.format(update_object.updates[0].message.from_id, update_object.updates[0].message.message))
                    #print(update_object)
                    msg=update_object.updates[0].message.message
                    context.receive(msg)


client.add_update_handler(update_handler)

while True:
    time.sleep( 1 )
    resp = context.act()
    if resp != None :
        print ("Enviando ... "+ resp)
        client.send_message('@IdleTownBot', resp)

