from bs4 import BeautifulSoup
import requests

URL = 'https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(URL)

website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

spans = soup.find_all("span", class_ = "content_content__i0P3p")
all_movies = []

for span in spans:
    h2 = span.find('h2')
    if h2:
        all_movies.append(h2.getText())

        # print(h2.getText())
# print(all_movies)

all_movies = all_movies[2:]
all_movies = all_movies[::-1]

for movie in all_movies:
    print(movie)