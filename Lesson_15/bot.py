import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from config import TOKEN
import random
from datetime import datetime

vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()

longpoll = VkLongPoll(vk_session)
print("Бот с клавиатурой запущен!")

def cmd_fact():
    facts = [
        "Python назван в честь шоу 'Monty Python'",
        "Первый сайт в интернете всё ещё работает!",
        "Бот - это просто программа, кторая общается с человеком",
        "Во ВКонтакте можно создавать 100 кнопок в одном меню!",
        "Почти 85% мирового кислорода производит в океане",
        "Весь гелий в атмосфере Земли уже улетучился в космос",
        "Леонардо да Винчи нарисовал эскизы ноутбука задолго до изобретения современных компьютеров.",
        "Вы слишком Пог",
        "Бокс стал официальным спортом только в 1900 году, раньше его считали слишком жестоким",
    ]
    return random.choice(facts)

def cmd_weather():
    weathers = ["+22°C", "+17°C", "-5°C", "+19°C"]
    return f"Погода сегодня: {random.choice(weathers)}"

def cmd_mods():
    mods = [
        "Ты - молодец",
        "Сегодня отличный день для кода!",
        "Улыбнись, и всё получится",
        "Продолжай, ты на верном пути!",
    ]
    return random.choice(mods)

def cmd_time():
    return f"Сейчас {datetime.now().strftime('%H:%M %S')}"

def cmd_music():
    return "    Любишь музыку? Попробуй жанры: рок, поп, джаз, классика!"

def cmd_help():
    return (
        "Доступные команды:\n"
        "факт - случайный факт\n"
        "погода - узнать шуточную погоду\n"
        "музыка - узнать про музыку\n"
        "время - узнать время\n"
        "настроение - случайное настроение на день\n"
        "помощь - список команд\n"
    )

command = {
    "факт": cmd_fact,
    "погода": cmd_weather,
    "настроение": cmd_mods,
    "время": cmd_time,
    "музыка": cmd_music,
    "помощь": cmd_help,
}

keyboard = VkKeyboard(one_time=False)
keyboard.add_button('Факт', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('Погода', color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_button('Настроение', color=VkKeyboardColor.SECONDARY)
keyboard.add_button('Музыка', color=VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_button('Время', color=VkKeyboardColor.SECONDARY)
keyboard.add_button('Помощь', color=VkKeyboardColor.NEGATIVE)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id = event.user_id
        text = event.text.lower().strip()

        if text in ["/start", "Привет", "Начать"]:
            vk.messages.send(
                user_id=user_id,
                message="Привет! Выбери, что хочешь сделать",
                keyboard=keyboard.get_keyboard(),
                random_id=0
            )

        elif text in command:
            response = command[text]()
            vk.messages.send(
                user_id=user_id,
                message=response,
                random_id=0
            )
        else:
            vk.messages.send(
                user_id=user_id,
                message="Не знаю такой команды",
                random_id=0
            )