import requests

response = requests.get("https://news.naver.com/")
print(response.text)
print(response.status_code)