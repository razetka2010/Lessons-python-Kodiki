from sklearn.linear_model import LinearRegression

# ==== Модел А =====
games = [[1], [2], [3], [4], [5]]
level_a = [1, 2, 3, 4, 5]

model_a = LinearRegression()
model_a.fit(games, level_a)

print("Модел А (Только игры): ")
print("Уровонь при играх:", model_a.predict([[4]]))

# ==== Модел Б =====
train_data = [
    [1, 0],
    [2, 1],
    [3, 1],
    [4, 2],
    [5, 3],
]
level_b = [1, 3, 4, 6, 8]

model_b = LinearRegression()
model_b.fit(train_data, level_b)

print("\nМодель Б (Игры + победы):")
print("Уровень при 4 и 2 победах:", model_b.predict([[4, 2]]))
