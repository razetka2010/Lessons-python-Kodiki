from vkbottle.bot import Bot, Message
from config import TOKEN
from datetime import datetime

bot = Bot(token=TOKEN)

HELLO_WORD = ["привет", "здравствуй", "хай"]
BYE_WORD = ["пока", "до свидания", "увидимся", "бай"]
ABOUT_WORD = ["как дела", "как ты", "как настроение"]
DO_WORD = ["что делаешь", "что делал", "что будешь делать"]
Pog = ["ты пог", "пог", "ты пог или пог", "ты пог или не пог"]
HELP = ["помоги", "я не понимаю", "что", "помогите"]

@bot.on.message(text="/start")
async def start_handler(message: Message):
    await message.answer("Привет!")

@bot.on.message()
async def text_handler(message: Message):
    text = message.text.lower()
    # await message.answer(f"Ты написал: {text}")
    #
    # if "привет" in text or "здравствуй" in text:
    #     await message.answer("Привет!")
    #
    # elif "пока" in text:
    #     await message.answer("До скорой встречи!")
    #
    # elif "Как дела" in text:
    #     await message.answer("Всё хорошо, у тебя как?")
    #
    # elif "Как ты" in text:
    #     await message.answer("Всё хорошо, у ты как?")
    #
    # elif "Что ты умеешь" in text:
    #     await message.answer("Я умею многое, что ты хочешь узнать?")
    #
    # elif "Спасибо" in text:
    #     await message.answer("Всегда пожалуйста! Мне было приятно с тобой общаться")
    #
    # elif "Мне скучно" in text:
    #     await message.answer("Иди в пень, и займись делом")
    #
    # else:
    #     await message.answer("Я тебя пока не понимаю")

    if any(word in text for word in HELLO_WORD):
        await message.answer("Привет! Рад тебя видеть")

    elif any(word in text for word in BYE_WORD):
        await message.answer("Пока! Приходи ещё!")

    elif any(word in text for word in ABOUT_WORD):
        await message.answer("Всё хорошо, а у тебя как?")

    elif any(word in text for word in DO_WORD):
        await message.answer("Я бот, я не могу ничего делать")

    elif any(word in text for word in Pog):
        await message.answer("Всё пог. Как сказал великий и могучий Валерчик: 'Если пог погу не пог то пог пог пог' или как сказал Алмаз: 'Если арбуз арбузу не арбуз то арбуз арбуз арбуз'")

    elif "время" in text or "который час" in text:
        now = datetime.now()
        currect_time = now.strftime("%H:%M")
        await message.answer(f"Сечас примерно {currect_time}")

    elif any(word in text for word in HELP):
        await message.answer("Мои команды:\n1.привет - приветствие,\n2.пока - прощание\n")

    else:
        await message.answer("Я тебя не понял(")

bot.run_forever()