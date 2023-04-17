import re
from bs4 import element

class Refactor(): 
    # Constructor
    def __init__(self, movies: list, links: list, crew: list, ratings: list, votes: list):
        self._movies = movies
        self._links = links
        self._crew = crew
        self._ratings = ratings
        self._votes = votes
        self._data = []

    def append_movie(self, movie: dict):
        self._data.append(movie)

    def get_movies(self):
        return self._data
    
    def splitter(self, movie: element.Tag, index: int):
        movie_string = movie.get_text()
        movie = (' '.join(movie_string.split()).replace('.', ''))
        movie_title = movie[len(str(index)) + 1:-7]
        year = re.search('\((.*?)\)', movie_string).group(1)
        place = movie[:len(str(index)) - (len(movie))]
        return movie_title, year, place

    def movie_information(self, movie_title: str, year: str, place: str, index: int):
        movie = {
            "preference_key": index % 4 + 1,
            "movie_title": movie_title,
            "star_cast": self._crew[index],
            "rating": self._ratings[index],
            "year": year,
            "place": place,
            "vote": self._votes[index],
            "link": self._links[index],
        }
        return movie

    def get_all(self):
        for idx, value in enumerate(self._movies):
            movie_title, year, place = self.splitter(value, idx)
            movie = self.movie_information(movie_title, year, place, idx)
            self.append_movie(movie)