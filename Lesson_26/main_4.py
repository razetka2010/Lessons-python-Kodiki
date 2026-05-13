from sklearn.linear_model import LinearRegression

hours = [
    [1, 0],
    [2, 0],
    [3, 1],
    [4, 1],
    [5, 1]
]

grades = [2, 3, 4, 5]

model = LinearRegression()
model.fit(hours, grades)

hours = int(input("Сколько часов ты учился? "))
hw = int(input("Ты сделал домашнее задание? ( 1 - да, 2 - нет ): "))

result = model.predict([[hours, hw]])
print("Прогноз:", round(result[0], 1))