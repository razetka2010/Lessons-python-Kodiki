import requests

response = requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=ru")
data = response.json()
print(data)