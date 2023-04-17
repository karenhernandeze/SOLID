import requests
from bs4 import BeautifulSoup

class Fetcher():
    #Constructor
    def __init__(self, url: str):
        self._url = url
        self._parser = 'lxml'
    
    #Fetch Data
    def fetch(self):
        return requests.get(self._url)

    #Convert Response To 'lxml' 
    def parse(self, response: str):
        return BeautifulSoup(response.text, self._parser)

    # Retrieve the data from the response and assing it to the respective
    # Data column. 

    # Getter And Setter for Movies
    def get_movies(self, soup: BeautifulSoup):
        return soup.select('td.titleColumn')
    def set_movies(self):
        response = self.fetch()
        soup = self.parse(response)
        movies = self.get_movies(soup)
        return movies

    # Getter And Setter for Links
    def get_links(self, soup: BeautifulSoup):
        return [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
    def set_links(self):
        response = self.fetch()
        soup = self.parse(response)
        links = self.get_links(soup)
        return links

    # Getter And Setter for Crew
    def get_crew(self, soup: BeautifulSoup):
        return [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
    def set_crew(self):
        response = self.fetch()
        soup = self.parse(response)
        crew = self.get_crew(soup)
        return crew

    # Getter And Setter for Ratings
    def get_ratings(self, soup: BeautifulSoup):
        return [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
    def set_ratings(self):
        response = self.fetch()
        soup = self.parse(response)
        ratings = self.get_ratings(soup)
        return ratings

    # Getter And Setter for Votes
    def get_votes(self, soup: BeautifulSoup):
        return [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]
    def set_votes(self):
        response = self.fetch()
        soup = self.parse(response)
        votes = self.get_votes(soup)
        return votes
    