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
                    await Handling.Process(vk, event)
        except:
            print('LongPoll has crashed! Awaiting 5 seconds before resuming!')
            traceback.print_exc()
            await asyncio.sleep(5)