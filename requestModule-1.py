import requests

# url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
#
# r = requests.get(url)
# print(r.text)

url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=API_KEY"

r = requests.get(url)
print(r.text)