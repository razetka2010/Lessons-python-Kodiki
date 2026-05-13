from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = [
    "Здравствуй",
    "Привет",
    "Как дела?",
    "Что ты умеешь?",
    "Пока",
    "До свидания",
    "Пог",
    "Если пог погу не пог то пог не пог",
    "Замечательно",
]

labels = [
    "Приветствие",
    "Приветствие",
    "Вопрос",
    "Вопрос",
    "Прощание",
    "Прощание",
    "Нейтральность",
    "Шутка",
    "Настроение",
]

answers = {
    "Приветствие": "Привет!",
    "Вопрос": "Нормально",
    "Прощание": "Пока",
    "Нейтральность": "Пог",
    "Шутка": "Пог",
    "Настроение": "ну и хорошо"
}

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

print("ИИ готов общаться!")

while True:
    text = input("Ты: ")
    if text.lower() == "выход":
        print("ИИ: Пока!")
        break

    X_test = vectorizer.transform([text])
    result = model.predict(X_test)[0]

    print("ИИ:", answers.get(result, "Я пока не знаю, что мне ответить"))