import urllib.parse, json, urllib.request
import media

class MovieGetter():
    """ MovieGetter fetches the information about movie from OMDb API
        Loads file with top movie listing and fetches movie information

        Args:
            max_movies_count

        Attributes:
            max_movies_count (int): maximum number of movies to return
    """
    def __init__(self, max_movies_count):
        self.movie_titles = []
        self.max_movies = max_movies_count

    def load_movie_titles(self):
        """ Loads external file with movie titles """
        movie_list_file = open('movies_list.txt', 'r')
        for line in movie_list_file:
            self.movie_titles.append(line)

    def load_movies(self):
        """ Creates Movie object for each movie after fetching info from the API"""
        API_URL = "http://www.omdbapi.com/?t="
        additional_params = "&plot=short&r=json"
        movies_to_add = []
        for movie in self.movie_titles:
            if self.max_movies == 0:
                break
            response = urllib.request.urlopen(API_URL + urllib.parse.quote(movie) +
                additional_params)
            data = json.loads(response.read().
                decode(response.info().get_param('charset') or 'utf-8'))
            movie_title = data['Title']
            movie_desc = data['Plot']
            movie_rating = data['imdbRating']
            movie_poster = data['Poster']
            movie_to_add = media.Movie(movie_title, movie_desc, movie_poster,
                '', movie_rating)
            movies_to_add.append(movie_to_add)
            self.max_movies -= 1
        return movies_to_add
