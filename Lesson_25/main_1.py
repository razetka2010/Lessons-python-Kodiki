from sklearn.tree import DecisionTreeClassifier

train_data = [
    [0, 0],
    [1, 0],
    [2, 1],
    [4, 1],
    [5, 1],
    [7, 1],
    [8, 1],
]

train_labels = [
    "Новичок",
    "Ученик",
    "Старательный",
    "Хорошист",
    "Отличник",
    "Супер - отличник",
    "Лентяй"
]

model = DecisionTreeClassifier()

model.fit(train_data, train_labels)

hours = int(input("Сколько часов ты учился сегодня? "))

hw = int(input("Ты делал домашнее задание? (1 - да, 0 - нет"))

result = model.predict([[hours, hw]])

print("Ии думает, что ты:", {result})