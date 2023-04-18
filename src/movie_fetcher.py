from movies.fetch import Fetcher
from movies.refactor import Refactor
from movies.filewriter import FileWriter

def main():
    # Downloading imdb top 250 movie's data
    url = 'http://www.imdb.com/chart/top'
    data = Fetcher(url)

    # Set data to the movie info 
    movies = data.set_movies()
    links = data.set_links()
    crew = data.set_crew()
    ratings = data.set_ratings()
    votes = data.set_votes()

    # Refactor the retrieved data into the wanted format 
    refactor = Refactor(movies, links, crew, ratings, votes)
    refactor.get_all()
    movie_list = refactor.get_movies()

    # Write the retrieved data into a csv file
    writer = FileWriter()
    filename = "movie_results.csv"
    writer.write_to_file(filename, movie_list)
    
if __name__ == '__main__':
    main()
