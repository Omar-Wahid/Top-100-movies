import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all(name="h3", class_="title")
titles_text = [f"{title.getText()}" for title in titles]
titles_text.reverse()
print(titles_text)


with open("movies.txt", mode="w", encoding="utf-8") as data:
    for title in titles_text:
        data.write(f"{title}\n")

