import urllib.request
from bs4 import BeautifulSoup

f = open('movies_list.txt', 'w')

def fetch_movie_list():
    page_url = "http://www.imdb.com/chart/top/"
    page = urllib.request.urlopen(page_url).read()
    soup = BeautifulSoup(page, "html.parser")
    movies = soup.find_all("td", class_="titleColumn")
    for movie in movies:
        f.write(movie.a.get_text() + "\n")

fetch_movie_list()
f.close()
