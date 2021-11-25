import vk_api
from VK import User

async def CreateUser(vk, ID):
    userinfo = vk.users.get(userids=ID, fields="first_name, last_name, screen_name, photo_50")[0]
    print(userinfo)
    return User.User(userinfo['first_name'], userinfo['last_name'], userinfo['id'], userinfo['screen_name'], userinfo['photo_50'])