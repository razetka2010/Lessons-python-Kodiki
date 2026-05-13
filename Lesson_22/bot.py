from vkbottle.bot import Bot, Message
from config import TOKEN
import json
import os

if os.path.exists("new_user.json"):
    with open("new_user.json", encoding="utf-8") as f:
        users = json.load(f)
else:
    users = {}

def save_users():
    with open("new_user.json", "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)

bot = Bot(token=TOKEN)

user_state = {}

@bot.on.message(text="/start")
async def start_handler(message: Message):
    user_id = message.from_id
    user_state[user_id] = "ask_name"
    await message.answer("Привет! Давай познакомимся. Как тебя зовут")

@bot.on.message()
async def dialog_handler(message: Message):
    user_id = message.from_id
    text = (message.text or "").strip()
    state = user_state.get(user_id)

    if state == "ask_name":
        name = text

        users[str(user_id)] = {
            "name": name
        }

        save_users()

        user_state[user_id] = None
        await message.answer(f"Приятно познакомиться, {name}!")
        await message.answer(f"Сколько тебе лет, {name}?")
        user_state[user_id] = "ask_age"
    elif state == "ask_age":
        age = text
        users[str(user_id)]["age"] = age
        save_users()
        user_state[user_id] = None
        await message.answer(f"Круто! тебе {age} лет")
    else:
        await message.answer("Я пока не понимаю, что ты хочешь. Напиши /start, что начать знакомство")
bot.run_forever()
