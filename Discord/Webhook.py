import requests
from VK import User
from config import WEBHOOKURL

async def SendMessage(User, Message):
    payload = await FormData(User, Message)
    requests.post(WEBHOOKURL, payload)

async def FormData(User, Message):
    TaggedMessage = f"{Message}\n\n`Username/User ID: {User.Username}/{User.Identity}`"
    data={'content': TaggedMessage, 'username': f'{User.Name} {User.Surname}', 'avatar_url': User.ProfilePicture}
    return data
