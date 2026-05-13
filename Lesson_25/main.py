from sklearn.linear_model import LinearRegression

hours = [[1], [2], [3], [4], [5], [6]]
scores = [20, 40, 50, 65, 80 , 90]

model = LinearRegression()
model.fit(hours, scores)

time = int(input("Сколько часов ты учился? "))

result = model.predict([[time]])

print("Результат:", round(result[0]))