import csv

class FileWriter():
    def __init__(self):
        self._fields = ["preference_key", "movie_title", "star_cast", "rating", "year", "place", "vote", "link"]
        
    def write_to_file(self, filename: str, movies_list: list):
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self._fields)
            writer.writeheader()
            for movie in movies_list:
                writer.writerow({**movie})