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
                message="Привет, дорогой друг, посети обязательно мой сайт по ссылке ниже"
                        "\nНемного обо мне:"
                        "\nМоё имя Артём, псевдоним Razetka, проживаю я в городе Новый Уренгой, 15 лет, учусь в 9 классе. Друзей нет, а если есть, то мало занимаюсь программированием, знаю такие языки, как Kotlin, Java, Java script, HTML, CSS, PHP, Python. С моими пректами вы можете ознакомиться в моём профиле GitHub по ссылке ниже"
                        "\n "
                        "\nGitHub: https://github.com/razetka2010"
                        "\nСайт: https://razetka2010.github.io/Business-card-website/"
                        "\nИспользуй команду /help чтобы ознакомиться с доступными командами",
                random_id=0
            )
        elif text == '/help':
            vk.messages.send(
                user_id=user_id,
                message="Доступные команды:"
                        "\n/start"
                        "\n/znaniesevera"
                        "\n/znanieseveravpn",
                random_id=0
            )
        elif text == '/znaniesevera':
            vk.messages.send(
                user_id=user_id,
                message="Знание Севера - это комплексная web-система электронного дневника, предназначенная для автоматизации учебного процесса в школах. Система предоставляет удобные инструменты для администраторов, учителей, учеников и родителей."
                        "\nСсылка на эл. дневник http://znaniesevera.ct.ws/",
                random_id=0
            )
        elif text == '/znanieseveravpn':
            vk.messages.send(
                user_id=user_id,
                message="Знание Севера VPN — мы не просто шифруем ваш трафик, мы его творчески интерпретируем!"
                        "\nTelegram бот для продажи VPN ключей с ручной выдачей от администратора."
                        "\n@CyberGuardRU_bot",
                random_id=0
            )
        else:
            vk.messages.send(
                user_id=user_id,
                message="Я ещё не знаю этой команды попробуйте что-то другое! /help",
                random_id=0
            )

    
