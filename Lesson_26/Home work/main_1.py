from sklearn.tree import DecisionTreeClassifier

train_data = [
    [8, 2],  
    [4, 0],  
    [6, 1],  
    [2, 2],  
    [10, 0], 
    [5, 1],  
    [3, 1],  
    [7, 2],  
]

train_labels = [
    "Сонный",
    "Голодный",
    "Игривый",
    "Голодный",
    "Сонный",
    "Игривый",
    "Активный",
    "Сытый"
]

model = DecisionTreeClassifier()
model.fit(train_data, train_labels)

sleep = int(input("Сколько часов спал? "))

food = int(input("Сколько порций съел? "))

result = model.predict([[sleep, food]])

print(f"Питомец сейчас: {result[0]}")