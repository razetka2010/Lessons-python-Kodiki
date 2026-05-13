from sklearn.linear_model import LinearRegression

hours = [[0], [1], [2], [3], [4], [5], [10]]
grades = [20, 35, 50, 65, 80, 90, 100]

model = LinearRegression()
model.fit(hours, grades)

print("ИИ обучен")
print("Предсказание для 3 часов учёбы:", model.predict([[3]]))
