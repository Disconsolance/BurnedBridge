import vk_api, traceback, time
from datetime import datetime
from vk_api.longpoll import VkEventType, VkLongPoll
from VK import Handling
from config import TOKEN
import asyncio

_vk_=vk_api.VkApi(token=TOKEN)
vk=_vk_.get_api()
longpoll=VkLongPoll(_vk_)

async def listen():
    while True:
        try:
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW:
                    print(event)
                    if event.from_chat is True:
                        print(f"This message came from a group chat! It's {event.peer_id}")
                    else:
                        print(f"This message came from a user! It's {event.peer_id}")
                    text=event.text.lower()
                    peer_id=event.peer_id
                    time_=event.raw[4]
                    message_id=event.message_id
                    print(text)
        except:
            print('LongPoll has crashed! Awaiting 5 seconds before resuming!')
            traceback.print_exc()
            asyncio.sleep(5)