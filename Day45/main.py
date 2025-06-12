from bs4 import BeautifulSoup
import requests


# _________ With lesson code _________
# response = requests.get("https://news.ycombinator.com/news")
# yc_webpage = response.text

# soup = BeautifulSoup(yc_webpage, "html.parser")
# topics = soup.select("tr .titleline a")
# subtopics = soup.select("tr .subtext .subline .score")

# article_upvotes = [int(subtopic.get_text().split(" ")[0]) for subtopic in subtopics]

# bigger = max(article_upvotes)

# largest_index = article_upvotes.index(bigger)
# print(topics[largest_index].get_text())
# print(topics[largest_index].get("href"))

# ___________ My code _____________

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
empire_webpage = response.text
soup = BeautifulSoup(empire_webpage, "html.parser")

movies = soup.select("h2 strong")
movies = [movie.get_text() for movie in movies]
reversed_movies = movies[::-1]
for movie in reversed_movies:
    print(movie)