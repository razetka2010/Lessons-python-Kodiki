#TODO: Подключаем библиотеки для работы нашего помощника!
from idlelib import query
from unittest import result

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#TODO: База для рекомендации
items = [
    {
        "title": "Гарри Поттер",
        "tags": "магия школа дружба приключения волшебник",
        "mood": "neutral"
    },

    {
        "title": "Марвел: Мстители",
        "tags": "герои битва спасение мира экшен команда",
        "mood": "positive"
    },

{
        "title": "Детектив: Тайна исчезновения",
        "tags": "детекстив расследования загадка преступления логика",
        "mood": "neutral"
    }
]

#TODO: Достаем только текст
corpus = [it["tags"] for it in items]

#TODO: Переводим текста в числа
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

#TODO: Функция ркекомендации
def recommend(query_text, pref_mood=None, top_n=3):
    q_vec = vectorizer.transform([query_text])
    sims = cosine_similarity(q_vec, X) # Похожесть на объект

    result = []

    for i, score in enumerate(sims):
        item = items[i]

        bonus = 0.0
        if pref_mood is not None and item["mood"] == pref_mood:
            bonus = 0.10 # Условно 10% к схожести
        final_score = score + bonus

        result.append((item["title"], final_score, item["mood"]))

    result.sort(key=lambda x: x[1], reverse=True)
    return result[:top_n]

#TODO: Просто выводим информацию от ИИ
print("🎬 ИИ-рекомендатор: я посоветую вам фильм/книгу по вашему запросу.")
print("Настроение можно указать: positive / neutral / negative (или просто пустую строку)\n")

while True:
    query = input("Введите, что вы хотите (или 'выход'): ").strip()
    if query.lower() in ("выход", "exit", "quit"):
        print("ПОКА!")
        break

    mood = input("Какое настроение препочитаете? (positive / neutral / negative или Enter): ").strip().lower()
    if mood == "":
        mood = None
    elif mood not in ("positive", "neutral", "negative"):
        print("Не понял вашего настроения, тогда будет пусто!")
        mood = None

    rec = recommend(query, pref_mood=mood, top_n=3)
    print("\n ✅ Рекомендации: ")
    for title, score, mood in rec:
        print(f" - {title} | похожесть: {score[0]*100:.1f}% | mood: {mood}")
    print()