from sklearn.linear_model import LinearRegression

data = [
    [1, 0],
    [2, 1],
    [3, 1],
    [4, 2],
    [5, 3],
    [6, 4]
]

level = [10, 25, 40, 60, 80, 100]

model = LinearRegression()
model.fit(data, level)

game = int(input("Игры: "))
wins = int(input("Победы: "))

result = model.predict([[game, wins]])
print("Уровень:", round(result[0], 1))