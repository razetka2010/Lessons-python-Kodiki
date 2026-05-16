#TODO: подключаем библиотеки для ншего проекта
import json
import tkinter as tk
from sklearn.linear_model import LinearRegression

#TODO: подключаем data.json к нашему проекту
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

#TODO: данные заполняются из json
hours = []
scores = []

#TODO: проходим по каждому значению часы и баллы
for item in data:
    hours.append([item["hours"]])
    scores.append(item["score"])

#TODO: создание и обучение ии
model = LinearRegression()
model.fit(hours, scores)

#TODO: функция для предсказания
def predict():
    try:
        h = float(entry.get())
        result = model.predict([[h]])
        label.config(text=f"Прогноз: {round(result[0])}")
    except:
        label.config(text="Введите число")

#TODO: создание окна
root = tk.Tk()
root.title("Предсказатель оценок")
root.geometry("300x200")

tk.Label(root, text="Сколько часов учился?", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 12))
entry.pack()

tk.Button(root, text="Предсказать", command=predict, bg="blue", fg="white").pack(pady=10)

label = tk.Label(root, text="", font=("Arial", 12))
label.pack()

root.mainloop()