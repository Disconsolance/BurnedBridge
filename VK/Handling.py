import vk_api
from VK import User

async def Process(vk, event):
    print(event)
    if event.from_chat is True:
        print(f"This message came from a group chat! It's {event.peer_id}, but came from {event.user_id}!")
        User = await CreateUser(vk, event.user_id)
    else:
        print(f"This message came from a user! It's {event.user_id}")
        User = await CreateUser(vk, event.user_id)
    print(event.text)

async def CreateUser(vk, ID):
    userinfo = vk.users.get(userids=ID, fields="first_name, last_name, screen_name, photo_50")[0]
    print(userinfo)
    return User.User(userinfo['first_name'], userinfo['last_name'], userinfo['id'], userinfo['screen_name'], userinfo['photo_50'])