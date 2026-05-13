from vkbottle.bot import Bot, Message
from config import TOKEN
import random
import json
import requests

bot = Bot(token=TOKEN)
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

@bot.on.message(text="/fact")
async def fact_handler(message: Message):
    fact = random.choice(data["facts"])
    await message.answer(f"Факт дня:\n\n{fact}")

@bot.on.message(text="/mood")
async def mood_handler(message: Message):
    mod = random.choice(data["moods"])
    await message.answer(f"Настроение дня: {mod}")

@bot.on.message(text="/joke_local")
async def joke_handler(message: Message):
    joke = random.choice(data["jokes"])
    await message.answer(f"Шутка:\n{joke}")

@bot.on.message(text="/quote_api")
async def quote_handler(message: Message):
    try:
        resp = requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=ru")
        data = resp.json()

        author = data["quoteAuthor"] or "Неизвестный автор"
        text = f"{data["quoteText"]}\n- {author}"
    except Exception:
        text = "Не смог получить цитату"

    await message.answer(text)

@bot.on.message(text="/catfact")
async def quote_handler(message: Message):
    try:
        resp = requests.get("https://catfact.ninja/fact")
        data = resp.json()

        fact_en = data["fact"]
        text = f"Факт о котиках {fact_en}"
    except Exception:
        text = "Не смог получить цитату"

    await message.answer(text)

@bot.on.message(text="/help")
async def help_handler(message: Message):
    await message.answer(
        "Команды бота:\n\n"
        "/fact - Случайный интересный факт\n"
        "/mood - Настроение дня\n"
        "/joke_local - Шутка из списка\n"
        "/quote_api - Факт Api\n"
        "/catfact - Факт ро котиков Api\n"
    )


bot.run_forever()
