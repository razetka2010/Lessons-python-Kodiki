import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import TOKEN
from datetime import datetime

vk_ssesion = vk_api.VkApi(token=TOKEN)
vk = vk_ssesion.get_api()

longpoll = VkLongPoll(vk_ssesion)
print("Бот запущен и слушает сообщения")

def time_period():
    h = datetime.now().hour
    if 5 <= h < 12:
        return "Утро"
    elif 12 <= h < 17:
        return "День"
    elif 17 <= h < 22:
        return "Вечер"
    else:
        return "Ночь"

def hello_by_time():
    p = time_period()
    mapping = {
        "Утро": "Доброе утро!",
        "День": "Добрый день!",
        "Вечер": "Добрый вечер!",
        "Ночь": "Доброй ночи!"
    }
    return mapping[p]

def cmd_start():
    return (f"{hello_by_time()} дорогой друг, посети обязательно мой сайт по ссылке ниже"
            f"\nНемного обо мне:"
            f"\nМоё имя Артём, псевдоним Razetka, проживаю я в городе Новый Уренгой, 15 лет, учусь в 9 классе. Друзей нет, а если есть, то мало занимаюсь программированием, знаю такие языки, как Kotlin, Java, Java script, HTML, CSS, PHP, Python. С моими пректами вы можете ознакомиться в моём профиле GitHub по ссылке ниже"
            f"\n "
            f"\nGitHub: https://github.com/razetka2010"
            f"\nСайт: https://razetka2010.github.io/Business-card-website/"
            f"\nИспользуй команду /help чтобы ознакомиться с доступными командами")

def cmd_help():
    return ("Доступные команды:"
            "\n/start"
            "\n/znaniesevera"
            "\n/znanieseveravpn")

def cmd_znaniesevera():
    return ("Знание Севера - это комплексная web-система электронного дневника, предназначенная для автоматизации учебного процесса в школах. Система предоставляет удобные инструменты для администраторов, учителей, учеников и родителей."
            "\nСсылка на эл. дневник http://znaniesevera.ct.ws/")

def cmd_znanieseveravpn():
    return ("Знание Севера VPN — мы не просто шифруем ваш трафик, мы его творчески интерпретируем!"
            "\nTelegram бот для продажи VPN ключей с ручной выдачей от администратора."
            "\n@CyberGuardRU_bot",)

commands = {
    "/start": cmd_start,
    "/help": cmd_help,
    "/znaniesevera": cmd_znaniesevera,
    "/znanieseveravpn": cmd_znanieseveravpn
}

def handle_command(text):
    cmd = text.lower().strip()
    if cmd in commands:
        if callable(commands[cmd]):
            return commands[cmd]()
        return commands[cmd]
    else:
        return "Не знаю такой команды, Попробуй /help"

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id = event.user_id
        text = (event.text or "").strip().lower().lower()
        response = handle_command(text)
        vk.messages.send(user_id=user_id, message=response, random_id=0)
