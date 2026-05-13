from vkbottle.bot import Bot, Message
from config import TOKEN
from datetime import datetime

bot = Bot(token=TOKEN)
HELLO_WORD = ["привет", "здравствуй", "здравствуйте", "добрый день"]
BYE_WORD = ["пока", "до свидания", "прощай", "давай пока"]
THANKYOU_WORD = ["спасибо", "благодарю", "спс"]
ABOUT_WORD = ["ты кто", "как тебя"]
ABOUT1_WORD = ["как дела", "как ты", "как настроение"]
DATETAME = ["сколько время", "который час", "сколько времени"]


@bot.on.message(text="/start")
async def start_handler(message: Message):
    await message.answer("Привет!")

@bot.on.message()
async def text_handler(message: Message):
    text = message.text.lower()
    if any(word in text for word in HELLO_WORD):
        await message.answer("Привет! Рад тебя видеть.")

    elif any(word in text for word in BYE_WORD):
        await message.answer("Давай удачи тебе! Ещё встретимся.")

    elif any(word in text for word in THANKYOU_WORD):
        await message.answer("Было приятно помочь, приходи ещё.")

    elif any(word in text for word in ABOUT_WORD):
        await message.answer("Я ВК бот написанный на языке python при помощи фреймворка VKbottle")

    elif any(word in text for word in ABOUT1_WORD):
        await message.answer("У меня всё хорошо, ты как?")

    elif "сколько времени" in text or "который час" in text or "сколько время" in text:
        now = datetime.now()
        currect_time = now.strftime("%H:%M")
        await message.answer(f"Сечас примерно {currect_time}")

    else:
        await message.answer("Я тебя не понял(")
bot.run_forever()
