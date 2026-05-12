temperature = int(input("Какая температура на улице? "))

if temperature < 0:
    print("Очень золодно!")
elif temperature <= 15:
    print("Прохладно!")
elif temperature >= 15:
    print("Тепло")