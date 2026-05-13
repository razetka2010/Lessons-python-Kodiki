# Короч идея проекта такая есть же корпорация Знание Севера и есть личные проекты такого человека Razetka и создать бота "визитку" для всех проектов - сайтов и для личной информации razetka 
# 
# 1. Проекты которые есть у Razetka:
# 1 - Знание Севера эл. дневник
# 2 - To-do list
# 3 - Религия Kamaz
# 4 - MyCloud
# 
# 2. Что должно быть в боте:
# Команды (смотреть на пункт 4) ✓
# Кнопки 
# Личная информация про Razetka ✓
# Информациия про проекты (смотреть на пункт 1) ✓
# Ссылки на все эти проекты ✓
# Контакты (telegram, github) ✓
# Использование больше эмодзи ✓ ✕
# 
# 3. Стэк технологий который используется в данном проекте
# Язык программирования Python
# Фреймворк под названием VkBottle 
# Приложение на котором пишется бот VsCode
# 
# 4. Команды которые будут в боте:
# /start - приветствие пользователя ✓
# /help - помощь в командах и контакты Rrazetka ✓
# /info - контакты(личная информация про Razetka) ✓
# /projects - существующие проекты ✓
# /znaniesevera - эл. дневник (смотреть на пункт 1) ✓
# /todolist - сервис список дел (смотреть на пункт 1) ✓
# /kamaz- религия (смотреть на пункт 1) ✓
# /mycloud - облачное хранилище (смотреть на пункт 1) ✓
# Второстипенные команды дописывать по приходе идеи 
#

from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor
from vkbottle import Text
from config import TOKEN

bot = Bot(token=TOKEN)

def main_keyboard():
    keyboard = Keyboard(one_time=False, inline=False)

    keyboard.add(Text("Информация", payload={"command": "info"}), color=KeyboardButtonColor.PRIMARY)
    keyboard.add(Text("Проекты", payload={"command": "projects"}), color=KeyboardButtonColor.PRIMARY)

    keyboard.row()

    keyboard.add(Text("Знание Севера", payload={"command": "znaniesevera"}), color=KeyboardButtonColor.SECONDARY)
    keyboard.add(Text("To-Do List", payload={"command": "todolist"}), color=KeyboardButtonColor.SECONDARY)

    keyboard.row()

    keyboard.add(Text("Религия Kamaz", payload={"command": "kamaz"}), color=KeyboardButtonColor.SECONDARY)
    keyboard.add(Text("MyCloud", payload={"command": "mycloud"}), color=KeyboardButtonColor.SECONDARY)

    keyboard.row()

    keyboard.add(Text("Помощь ❓", payload={"command": "help"}), color=KeyboardButtonColor.NEGATIVE)

    return keyboard

def contact_keyboard():
    keyboard = Keyboard(one_time=False, inline=True)
    keyboard.add(Text("Контакты 📞", payload={"command": "info"}), color=KeyboardButtonColor.POSITIVE)
    keyboard.add(Text("Главное меню 🏠", payload={"command": "start"}), color=KeyboardButtonColor.PRIMARY)
    return keyboard

@bot.on.message(text=["/start", "Главное меню 🏠"])
async def start_handler(message: Message):
    keyboard = main_keyboard()
    attachment = "photo-234450844_456239032"
    await message.answer("Привет 🖐️, я бот - портфолио написанный с целью ознакомить вас с личными проектами Razetka и корпорацией Знание Севера\n\nНапиши /help чтобы ознакомиться со списком команд", keyboard=keyboard, attachment=attachment)

@bot.on.message(text=["/help", "Помощь ❓"])
async def help_handler(message: Message):
    await message.answer("Список команд:\n\n"
    "/start - приветстивие пользователя\n"
    "/info - контакты с программистом\n"
    "/projects - список проектов\n"
    "/znaniesevera - информация про электронный дневник\n"
    "/todolist - информация про сервис список дел\n"
    "/kamaz - информация про религию Kamaz\n" 
    "/mycloud - информация про облачное хранилище\n\n"
    "Техническая поддержка:\n"
    "Telegram - @znaniesevera\n"
    "Номер телефона - +7 (921) 094-84-23")

@bot.on.message(text=["/info", "Информация", "Контакты 📞"])
async def info_handler(message: Message):
    await message.answer("С вами на связи Артём под скрытым именем Razetka я ознакомлен с несколькими языками программировани такие как Kotlin, Java, JavaScript, HTML, CSS, PHP и Python за дополнительной информацией можете написать мне контакты указаны ниже\n\n" 
    "Telegram - @znaniesevera\n" 
    "Telegran канал - t.me/razetkaartem\n"
    "Номер телефона - +7 (921) 094-84-23\n"
    "GitHub - https://github.com/razetka2010")

@bot.on.message(text=["/projects", "Проекты"])
async def projects_handler(message: Message):
    keyboard = contact_keyboard()
    await message.answer("Все проекты написанные корпорацией Знание Севера и razetka\n\n"
    "1. Знание Севера - https://znaniesevera.ct.ws/ (Не работает так как закончился домен)\n"
    "2. To-do List - https://to-do-list-pog.ct.ws/\n"
    "3. Религия Kamaz - https://kamazinstvo.ct.ws/\n"
    "4. MyCloud - https://my-clod-nodesj.onrender.com\n\n", keyboard=keyboard)

@bot.on.message(text=["/znaniesevera", "Знание Севера"])
async def znaniesevera_handler(message: Message):
    keyboard = contact_keyboard()
    attachment = "photo-234450844_456239031"
    await message.answer("Знание Севера электронный дневник\n\n"
    "• Знание Севера - это современная образовательная платформа, разработанная специально для учебных заведений северных регионов.\n"
    "• Мы предоставляем удобный инструмент для отслеживания успеваемости, управления расписанием и коммуникации между всеми участниками образовательного процесса.\n"
    "• Наша система обеспечивает безопасный доступ к учебной информации в любое время и с любого устройства.\n\n"
    "Возможности дневника\n"
    "1. Отслеживание текущих оценок и средней успеваемости по всем предметам.\n"
    "2. Актуальное расписание уроков с учетом изменений и замен.\n"
    "3. Полная информация о домашних заданиях, сроках сдачи и требованиях к выполнению\n"
    "4. Важные объявления от учителей и администрации школы\n"
    "5. Родители могут отслеживать успехи ребенка и общаться с преподавателями\n\n"
    "Для кого предназначен дневник\n"
    "• Для учеников\n"
    "• Для учителей\n"
    "• Для родителей\n"
    "• Для администрации\n\n"
    "https://znaniesevera.ct.ws/ (Не работает так как закончился домен)\n\n", keyboard=keyboard, attachment=attachment)

@bot.on.message(text=["/todolist", "To-Do List"])
async def todolist_handler(message: Message):
    keyboard = contact_keyboard()
    attachment = "photo-234450844_456239033"
    await message.answer("Организуйте свою жизнь с нашим TO-DO List\n\n"
    "Умный календарь - просматривайте все свои задачи в удобном календарном формате. Планируйте на день, неделю или месяц вперед.\n"
    "1. Зарегистрируйтесь - создайте бесплатный аккаунт за 30 секунд\n"
    "2. Добавьте задачи - создавайте задачи, устанавливайте сроки и приоритеты\n"
    "3. Достигайте целей - отслеживайте прогресс и повышайте продуктивность\n\n"
    "https://to-do-list-pog.ct.ws/\n\n", keyboard=keyboard, attachment=attachment)

@bot.on.message(text=["/kamaz", "Религия Kamaz"])
async def kamaz_handler(message: Message):
    keyboard = contact_keyboard()
    attachment = "photo-234450844_456239034"
    await message.answer("Религия Kamaz\n\n"
    "Основные принципы:\n"
    "1. Камаз-Вседержитель едет вечно\n"
    "2. Кольцевой Дороге Мироздания\n"
    "3. Крутящий Момент - первичная сила вселенной\n"
    "4. Пешеходы - искусители или добровольные жертвы\n"
    "5. Непоколебимость - главная добродетель\n"
    "6. Пустой кузов - смертный грех\n\n"
    "Ритуалы:\n"
    "Молитвенное Сбивание: сакральное таинство\n"
    "Окропление омывайкой: освящение маршрута\n"
    "Воскурение выхлопами: задабривание духов\n"
    "Пост «Под погрузкой»: аскеза водителя\n\n"
    "https://kamazinstvo.ct.ws/\n\n", keyboard=keyboard, attachment=attachment)

@bot.on.message(text=["/mycloud", "MyCloud"])
async def mycloud_handler(message: Message):
    keyboard = contact_keyboard()
    attachment = "photo-234450844_456239035"
    await message.answer(
        "MyCloud\n\n"
        "• Поддержка файлов до 5GB\n"
        "• Множественная загрузка\n"
        "• Регистрация и авторизация\n"
        "• Генерация публичных ссылок\n"
        "• Срок действия ссылок: 7 дней\n\n"
        "Безопасность:\n"
        "• Хеширование паролей\n"
        "• Валидация файлов\n"
        "• Защита от опасных расширений\n\n"
        "https://my-clod-nodesj.onrender.com\n\n", keyboard=keyboard, attachment=attachment)

@bot.on.message()
async def unknown_handler(message: Message):
    keyboard = main_keyboard()
    await message.answer("Извините, я не понимаю эту команду. Напишите /help для списка доступных команд.", keyboard=keyboard)

bot.run_forever()
