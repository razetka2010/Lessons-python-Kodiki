import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import TOKEN
from datetime import datetime
import random

vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()

longpoll = VkLongPoll(vk_session)
print("Бот запущен и слушает сообщения")

def get_time():
    now = datetime.now()
    return f"Сейчас {now.strftime('%H:%M:%S')}"

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
    return f"{hello_by_time()} я бот написанный на python напиши команду /help чтобы ознакомиться со всеми доступными командами"

def cmd_help():
    return "Доступные команды:\n/start\n/help\n/about\n/news\n/joke"

def cmd_about():
    return "Я - бот, созданный на Python."

def cmd_news():
    news = [
        "В Екатеринбурге откроется визовый центр Кипра",
        "Американские ученые: недосып убивает",
        "В курском приграничье дрон атаковал гражданский автомобиль: ранен один человек",
        "Приложение «Купер» исчезло из App Store"
    ]
    return random.choice(news)

def cmd_joke():
    shutka = [
        "Как заставить змею плакать? — Отобрать у нее погремушку.",
        "Зачем птицы летают в теплые края? — Потому что идти пешком долго.",
        "Британские ученые выяснили: если долго смотреть на кота, он начнет смотреть в ответ… с осуждением.",
        "Почему крокодил не пишет стихи? — Слез хватает, а рифм нет.",
        "Почему рыбы живут в соленой воде? — Потому что перченая вода заставляет их чихать."
    ]
    return random.choice(shutka)

commands = {
    "/start": cmd_start,
    "/help": cmd_help,
    "/about": cmd_about,
    "/news": cmd_news,
    "/joke": cmd_joke,
    "/time": get_time,
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