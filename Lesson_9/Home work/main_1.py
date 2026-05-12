quiz = [
    {"text": "Ты пог или пог?", "options": ["пог", "не я не пог", "пог"], "answer": 0},
    {"text": "Какая самая лучшая Oc?", "options": ["Mac Oc", "Linux", "Winda"], "answer": 0},
    {"text": "2 + 2", "options": ["5", "4", "5000", "8"], "answer": 1}
]

score = 0

for q in quiz:
    print(q["text"])
    for i, opt in enumerate(q["options"]):
        print(f"{i}) {opt}")
    
    user_answer = int(input("Ваш ответ (введите номер): "))
    if user_answer == q["answer"]:
        score += 1
    print()

percent = round(score / len(quiz) * 100, 2)
print("Результат:", percent, "%")
