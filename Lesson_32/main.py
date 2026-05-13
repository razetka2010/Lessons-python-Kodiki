from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

data = [
    ("Мне очень понравился урок", "positive"),
    ("Это было интересно", "positive"),
    ("Я рад что пришёл", "positive"),
    ("Классно получилось", "positive"),
    ("Алоо", "positive"),
    ("Отличное занятие!", "positive"),
    ("Преподаватель супер", "positive"),
    ("Всё понятно и доступно", "positive"),
    ("Лучший урок в моей жизни", "positive"),
    ("Спасибо большое!", "positive"),
    ("Очень познавательно", "positive"),
    ("Буду рекомендовать друзьям", "positive"),
    ("Суперский материал", "positive"),
    ("Я в восторге", "positive"),
    ("Круто!", "positive"),
    ("Здорово объясняете", "positive"),
    ("Прогресс налицо", "positive"),
    ("Огромное спасибо за урок", "positive"),
    ("Теперь я всё понял", "positive"),
    ("Потрясающе!", "positive"),
    ("Лучшее объяснение темы", "positive"),
    ("Хочу ещё таких уроков", "positive"),
    ("Прекрасно провёл время", "positive"),
    ("Очень полезно", "positive"),
    ("С удовольствием посещаю", "positive"),

    ("Мне было скучно", "negative"),
    ("Это ужасно", "negative"),
    ("Мне не понравилось", "negative"),
    ("Как то не", "negative"),
    ("Впустую потраченное время", "negative"),
    ("Ничего не понял", "negative"),
    ("Преподаватель неинтересно объясняет", "negative"),
    ("Слишком сложно", "negative"),
    ("Скучная подача материала", "negative"),
    ("Не рекомендую", "negative"),
    ("Разочарование полное", "negative"),
    ("Трата времени", "negative"),
    ("Непонятная тема", "negative"),
    ("Хотел уйти посреди урока", "negative"),
    ("Много воды и мало пользы", "negative"),
    ("Не оправдал ожиданий", "negative"),
    ("Уснул на уроке", "negative"),
    ("Никакого интереса", "negative"),
    ("Зря пришёл", "negative"),
    ("Слабый преподаватель", "negative"),
    ("Материал устарел", "negative"),
    ("Непонятные примеры", "negative"),
    ("Слишком быстрый темп", "negative"),
    ("Не для начинающих", "negative"),
    ("Разочарован", "negative"),

    ("Сегодня был урок", "neutral"),
    ("Мы изучали нейросети", "neutral"),
    ("Сейчас идёт занятие", "neutral"),
    ("ПОГ", "neutral"),
    ("Обычное занятие", "neutral"),
    ("Ничего особенного", "neutral"),
    ("Как обычно", "neutral"),
    ("Записал основные тезисы", "neutral"),
    ("Присутствовал на лекции", "neutral"),
    ("Выполнил домашнее задание", "neutral"),
    ("Тема про искусственный интеллект", "neutral"),
    ("Обсудили новые термины", "neutral"),
    ("Разобрали примеры", "neutral"),
    ("Стандартный урок", "neutral"),
    ("Без восторгов, но терпимо", "neutral"),
    ("Посмотрим, что будет дальше", "neutral"),
    ("Пока не могу оценить", "neutral"),
    ("Информация к размышлению", "neutral"),
    ("Продолжим на следующем занятии", "neutral"),
    ("Было нормально", "neutral"),
    ("Приемлемо", "neutral"),
    ("Средний уровень", "neutral"),
    ("Не хуже и не лучше обычного", "neutral"),
    ("Без эмоций", "neutral"),
    ("Констатация фактов", "neutral"),
]

text = [t for t, y in data]
labels = [y for t, y in data]

x_train, x_test, y_train, y_test = train_test_split(
    text, labels, test_size=0.5, random_state=42, stratify=labels
)

model = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
    ("clf", LogisticRegression(max_iter=1000))
])

model.fit(x_train, y_train)

print("=== Проверка ===")
print(classification_report(y_test, model.predict(x_test), digits=3))

print("\nВВедите фразу (Или 'Выход')")

while True:
    text = input(">>> ").strip()

    if text.lower() in ("выход", "exit", "quit"):
        print("Работа завершена.")
        break

    probs = model.predict_proba([text])[0]
    classes = model.classes_

    print("\nРезультаты анализа:")
    for cls, p in zip(classes, probs):
        print(f"{cls:8s} - {p * 100:.1f}%")

    best = probs.argmax()
    emoji = {"positive": "😊", "neutral": "😐", "negative": "😡"}[classes[best]]

    print(f"\n{emoji} Итог: {classes[best]} ({probs[best] * 100:.1f}%)\n")