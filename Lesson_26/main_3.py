from sklearn.linear_model import LinearRegression

hours = [[-3], [0], [1], [2], [3], [4], [5], [6], [20]]
scores = [150, 200, 20, 40, 55, 70, 85, 95, 1000]
model = LinearRegression()
model.fit(hours, scores)

print("ИИ обучен")
print("Предсказание для 4 часов учёбы:", model.predict([[4]]))