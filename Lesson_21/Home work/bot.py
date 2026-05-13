from vkbottle.bot import Bot, Message
from config import TOKEN
import json
import requests

bot = Bot(token=TOKEN)

with open("data_homework.json", "r", encoding="utf-8") as f:
    data = json.load(f)

@bot.on.message(text="/user")
async def users_command(message: Message):
    text = (data["users"])
    await message.answer(text)

@bot.on.message(text="/products")
async def products_command(message: Message):
    text = (data["products"])
    await message.answer(text)


@bot.on.message(text="/rates")
async def rates_handler(message: Message):
    try:
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        rates_data = requests.get(url).json()

        usd = rates_data["Valute"]["USD"]["Value"]
        eur = rates_data["Valute"]["EUR"]["Value"]

        text = (
            "Курсы валют ЦБ РФ:\n\n"
            f"💵 Доллар: {usd} ₽\n"
            f"💶 Евро: {eur} ₽"
        )
    except Exception:
        text = "Не смог получить курсы валют 😭"

    await message.answer(text)

bot.run_forever()
