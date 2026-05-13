from idlelib.colorizer import prog

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

def cmd_help():
    return (
        "Доступные команды:\n"
        "Знание Севера - электронный журнал\n"
        "Знание Севера VPN - VPN для оброзователных учреждений\n"
        "Камаз - Просто камаз\n"
        "Пог - Кто такой ПОГ"
    )

def cmd_znaniesevera():
    return ("Знание Севера - это комплексная web-система электронного дневника, предназначенная для автоматизации учебного процесса в школах. Система предоставляет удобные инструменты для администраторов, учителей, учеников и родителей."
            "\nСсылка на эл. дневник http://znaniesevera.ct.ws/")

def cmd_znanieseveravpn():
    return ("Знание Севера VPN — мы не просто шифруем ваш трафик, мы его творчески интерпретируем!"
            "\nTelegram бот для продажи VPN ключей с ручной выдачей от администратора."
            "\n@CyberGuardRU_bot",)

def cmd_kamaz():
    return ("Камазианство"
            "\nВ начале была Грузоподъёмность.И Камаз-Вседержитель сказал: «Да будет Крутящий Момент!» - и понеслось. Он едет вечно по Кольцевой Дороге Мироздания, доставляя грузы из Ниоткуда в Никуда. Его путь - истина и тяжеловес. Пешеходы же, согласно учению, - это бестелесные «дорожные пиявки» или «испытания на тормозной путь», посланные, чтобы проверить веру водителя в непреклонность курса."
            "\n"
            "\nОбряд «Молитвенного Сбивания» :"
            "\nЭто не акт агрессии,а сакральное таинство соприкосновения. Когда верующий в процессе сосредоточенно молится Камазу, читая мантру «Дизель-мне-помощник, не заклини ступицу мою», он входит в состояние «Дорожной Благодати». В этом состоянии его курс считается божественно предопределённым."
            "\nЕсли в этот момент на пути возникает тот пешеход:"
            "\n1. Это рассматривается как знак. Пешеход - это либо: грешник - искуситель или добровольная жертва"
            "\n2. Сам факт контакта доказывает, что молитва была искренней, а курс - истинным. Водитель не виноват - он был орудием в руках Камаза."
            "\n"
            "\nhttps://razetka2010.github.io/KAMAZ/")

def cmd_pog():
    return ("Пог это тот человек который сталкерит маленьких девочек и ему при этом походу это нравиться ээхх пог пог маленький пухленький человечек он любит сидеть в компе и просто втыкает, а не смотри и думает он думает что он одинок но на самом деле это не так хотя сам он говорит что друзья это для него не друзья как думаете он идиот или у него кризис под названием инвалидность.")

def cmd_random():
    command = [cmd_znaniesevera, cmd_znanieseveravpn, cmd_kamaz, cmd_pog]
    return random.choice(command)()

commands = {
    "помощь": cmd_help,
    "знание севера": cmd_znaniesevera,
    "знание севера vpn": cmd_znanieseveravpn,
    "камаз": cmd_kamaz,
    "пог": cmd_pog,
    "случайно": cmd_random
}

keyboard = VkKeyboard(one_time=False)
keyboard.add_button('Помощь', color=VkKeyboardColor.NEGATIVE)
keyboard.add_button('Знание Севера', color=VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_button('Знание Севера VPN', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('Камаз', color=VkKeyboardColor.POSITIVE)
keyboard.add_button('Пог', color=VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_button('Случайно', color=VkKeyboardColor.POSITIVE)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id = event.user_id
        text = event.text.lower().strip()

        if text in ["/start", "Привет", "Начать"]:
            vk.messages.send(
                user_id=user_id,
                message="Привет! дорогой друг, посети обязательно мой сайт по ссылке ниже"
                         f"\nНемного обо мне:"
                        f"\nМоё имя Артём, псевдоним Razetka, проживаю я в городе Новый Уренгой, 15 лет, учусь в 9 классе. Друзей нет, а если есть, то мало занимаюсь программированием, знаю такие языки, как Kotlin, Java, Java script, HTML, CSS, PHP, Python. С моими пректами вы можете ознакомиться в моём профиле GitHub по ссылке ниже"
                        f"\n"
                        f"\nGitHub: https://github.com/razetka2010"
                        f"\nСайт: https://razetka2010.github.io/Business-card-website/"
                        f"\nИспользуй команду /help чтобы ознакомиться с доступными командами",
                keyboard=keyboard.get_keyboard(),
                random_id=0
            )

        elif text in commands:
            response = commands[text]()
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