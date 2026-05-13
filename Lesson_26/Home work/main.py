from sklearn.linear_model import LinearRegression

hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
scores = [20, 40, 50, 65, 80, 90, 95, 100]

model = LinearRegression()
model.fit(hours, scores)

time = int(input("Сколько часов ты занимался? "))

result = model.predict([[time]])

print("Результат:", round(result[0]))
