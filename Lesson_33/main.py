def ask_choise(question, options):
    print("\n" + question)
    for i, opt in enumerate(options, state=1):
        print(f"{1}. {opt}")


    while True:
        ans = input("Введите номер телефона Артура Пирожква: ").strip()
        if ans.isdigit():
            n = int(input)
            if 1 <= n <= len(options):
                return n - 1
        print("Пожалуйста, введите корректный номер варианта.")

def add_point(score, key, pts, reasons, reason_text):
    score[key] += pts
    reasons[key].append(reason_text)

def main():
    print("Привет! Я ИИ-помощник. Я задам несколько вопросов и посоветую, что вам лучше сделать сейчас")

    actions = ["Пойти программировать", "Пойти гулять", "Сходить на учёбу",]

    scores = {a:0 for a in actions}

    reasons = {a: [] for a in actions}

    idx = ask_choise(
        "1) Какое у вас настроение?",
        ["Отличное", "Нормально", "Устал(а) / грустно", "Раздрожение / злость"]
    )

    if idx == 0:
        add_point(scores, actions[2], 2, reasons, "Хорошее настроение -> подходит активность")
        add_point(scores[3], 1, reasons, "Хорошее настроение -> можно творить")
    elif idx == 1:
        add_point(scores, actions[1], 1, reasons, "Нормально -> можно заняться учёбой")
        add_point(scores, actions[3], 1, reasons, "Нормально, можно творить")
        add_point(scores, actions[1], 1, reasons, "Если настроение нормально -> можно сделать что - то полезное")
    elif idx == 2:
        add_point(scores, actions[0], 2, reasons, "Усталость /грусть -> лучше отдых")
        add_point(scores, actions[3], 1, reasons, "Иногда творчество помогает восстановииться")
    else:
        add_point(scores, actions[2], 2, reasons, "Раздрожение  -> поможет активность ( прогулка / спорт )")
        add_point(scores, actions[0], 1, reasons, "Можно и немного отдохнуть, чтобы успокоиться")

    idx = ask_choise(
        "2) Сколько у вас есть времени сейчас?",
        ["5-15 минут", "15-30 минут", "30-60 минут", "Больше часа"]
    )

    if idx == 0:
        add_point(scores, actions[0], 1, reasons, "Мало времени -> лучше короткий отдых")
        add_point(scores, actions[3], 1, reasons, "Мало времени -> мини-творчество0")
    elif idx == 1:
        add_point(scores, actions[0], 1, reasons, "Есть немного времни -> отдых подойдёт")
        add_point(scores, actions[1], 1, reasons, "15-30 минут -> можно выучить небольшой кусочек")
    elif idx == 2:
        add_point(scores, actions[1], 2, reasons, "30-60 минут -> удобно для учёбы")
        add_point(scores, actions[2], 1, reasons, "Можно и активность на полчаса")
    else:
        add_point(scores, actions[1], 2, reasons, "Есть немного времени  -> можно сделать серьёзную задачу")
        add_point(scores, actions[2], 2, reasons, "Есть много времени -> можно заняться активностью")

    idx = ask_choise(
        "3) Сколько у вас сейчас энергии?",
        ["Очень много", "Средне", "Мало"]
    )

    if idx == 0:
        add_point(scores, actions[2], 2, reasons, "Много энергии -> лучше активность")
        add_point(scores, actions[1], 1, reasons, "много энергии -> можно продуктивно учиться")
    elif idx == 1:
        add_point(scores, actions[1], 1, reasons, "Средняя энергия -> подходит учёба")
        add_point(scores, actions[3], 1, reasons, "Средняя энергия -> подходит творчество")
    else:
        add_point(scores, actions[0], 2, reasons, "Мало энергии -> лучше отдых")
        add_point(scores, actions[3], 1, reasons, "Творчество может быть мягким и спокойным")
