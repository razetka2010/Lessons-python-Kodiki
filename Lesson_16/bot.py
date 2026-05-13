import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import TOKEN

vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()

longpoll = VkLongPoll(vk_session)
print("Бот с медиа запущен!")

def send(user_id, text=None, attachment=None):
    vk.messages.send(
        user_id=user_id,
        message=text or "",
        attachment=attachment or "",
        random_id=0
    )

POG = "photo-234450844_456239021"

def cmd_thefirstphoto():
    return "Я люблю Вк 💕", POG

commands = {
    "/vk": cmd_thefirstphoto
}

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id = event.user_id
        text = (event.text or "").strip().lower()

        if text in commands:
            msg, attach = commands[text]()
            send(user_id, text=msg, attachment=attach)
        else:
            send(user_id, "Не знаю такой команды.")