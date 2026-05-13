import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import TOKEN

vk_ssesion = vk_api.VkApi(token=TOKEN)
vk = vk_ssesion.get_api()

longpoll = VkLongPoll(vk_ssesion)
print("Бот запущен и слушает сообщения")

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id = event.user_id
        text = (event.text or "").strip().lower().lower()

        if text == '/start':
            vk.messages.send(
                user_id=user_id,
                message="Привет, я бот написанный на python напиши команду /help чтобы ознакомиться со всеми доступными командами",
                random_id=0
            )
        elif text == '/help':
            vk.messages.send(
                user_id=user_id,
                message="Доступные команды /start, /help, /about",
                random_id=0
            )
        elif text == '/about':
            vk.messages.send(
                user_id=user_id,
                message="Я - первый бот, созданный на Python!",
                random_id=0
            )
        else:
            vk.messages.send(
                user_id=user_id,
                message="Я ещё не знаю этой команды попробуйте что-то другое! /help",
                random_id=0
            )

    
