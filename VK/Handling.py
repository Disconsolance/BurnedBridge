import vk_api
from VK import User
from Discord import Webhook
from config import CHATID


async def Process(vk, event):
    if event.from_chat is False or event.peer_id != 2000000000+CHATID:
        return
    Message = event.text
    User = await CreateUser(vk, event.user_id)
    if len(event.attachments) != 0: # Does this message even have attachments?
        tmp = vk.messages.getById(message_ids=event.message_id)['items'][0]['attachments']
        Attachments = await FetchPhotos(tmp, event.attachments)
        Message = await AppendAttachmentURL(Message, Attachments)
    Message = await ScrubMasspings(Message)
    await Webhook.SendMessage(User, Message)

async def CreateUser(vk, ID):
    userinfo = vk.users.get(user_ids=ID, fields="first_name, last_name, screen_name, photo_50")[0]
    return User.User(userinfo['first_name'], userinfo['last_name'], userinfo['id'], userinfo['screen_name'], userinfo['photo_50'])

async def FetchPhotos(tmp, AttachmentsList):
    PhotoURLList=[]
    ATTLEN=int(len(AttachmentsList)/2)
    for i in range(ATTLEN):
        if AttachmentsList[f'attach{i+1}_type'] == 'photo':
            PhotoURLList.append(tmp[i]['photo']['sizes'][4]['url'])
    return PhotoURLList

async def AppendAttachmentURL(Message, Attachments):
    Message += "\n\nAttachments:```\n"
    for URL in Attachments:
        Message += f"{URL}\n"
    Message += "```"
    return Message

async def ScrubMasspings(Message):
    result = Message.replace("@here", "!MASSPING!")
    result = result.replace("@everyone", "!MASSPING!")
    return result