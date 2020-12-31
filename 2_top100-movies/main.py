import requests
from bs4 import BeautifulSoup

# step 1
url = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)
web_page = response.text

# step 2
soup = BeautifulSoup(web_page, "html.parser")


movies_name = soup.find_all("h3", class_="title")
movies_name_list = []
for movie in movies_name:
    m_name = movie.getText()
    movies_name_list.append(m_name)


rev_movies = []
for n in range(len(movies_name_list)-1, -1, -1):   # ->99 ,1   minus 1 everytime
    rev_movies.append(movies_name_list[n])

with open("movie.text", mode="w", encoding='utf-8') as file:
    for movie in rev_movies:
        file.write(f"{movie}\n")



