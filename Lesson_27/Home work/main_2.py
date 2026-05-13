from sklearn.linear_model import LinearRegression

# x = [[1], [2], [3], [4], [5], [1]]
# y = [2, 4, 6, 8, 10, 100]

# model = LinearRegression()
# model.fit(x, y)
# print("3 ->", model.predict([[3]]))

x = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

model = LinearRegression()
model.fit(x, y)
print("3 ->", model.predict([[3]]))