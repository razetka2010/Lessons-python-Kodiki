from sklearn.tree import DecisionTreeClassifier

data = [
    [1, 1],  
    [2, 2],  
    [3, 5],  
    [4, 6],  
    [6, 8],  
    [8, 9],  
]

types = [
    "Новичок",
    "Новичок",
    "Любитель", 
    "Любитель",
    "Профи",
    "Профи"
]


model = DecisionTreeClassifier()

model.fit(data, types)

hours = int(input("Сколько часов играешь в день? ( 1 - 8 ): "))

level = int(input("Какой у тебя уровень? ( 1 - 10 ): "))


result = model.predict([[hours, level]])

print(f"Ты: {result[0]}")