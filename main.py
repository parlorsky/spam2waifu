from telethon import TelegramClient
import telethon.sync
import time
from prompts import construct_prompt
from config.py import NAME_OF_SESSION,API_ID,API_HASH,LINK_TO_CHAT


client = TelegramClient(NAME_OF_SESSION, API_ID, API_HASH)
client.start()
entity=client.get_entity(LINK_TO_CHAT)

i = 0
while True:
    i += 1
    
    if i%1000 == 0: print(i)
    try:
        client.send_message(entity=entity,message=construct_prompt())
        time.sleep(10)
    except:
        time.sleep(3)
        if i%200 == 0: print(i)
        
