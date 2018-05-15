from telethon import TelegramClient, events
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

client = TelegramClient('session_name3', api_id, api_hash, update_workers=1)
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

@client.on(events.NewMessage(incoming=True))
def update_handler(event):
    global doAttack
    global doSearchOpponent

    if checkUser(event.message.from_id) :
        sprint('<<<<<<<\nUser #{}\n#{}\n<<<<<<<\n'.format(event.message.from_id, event.message.message))
        msg=event.message.message
        context.receive(msg)


client.send_message('@IdleTownBot', "Menu 📜")

while True:
    time.sleep( 2 )
    resp = context.act()
    if resp != None :
        print ("Enviando ... "+ resp)
        client.send_message('@IdleTownBot', resp)

