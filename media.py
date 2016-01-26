import webbrowser

class Movie():
    """ Movie Class for creating Movie objects

        Args:
            movie_title
            movie_storyline
            poster_image
            trailer_youtube_url
            movie_rating
        Attributes:
            title (str): Title of the movie
            movie_storyline (str): Brief description of the movie
            poster_image_url (str): URL for poster image of the movie
            trailer_youtube_url (str): URL for the trailer on youtube
            rating (str): imdb Rating of the movie
    """
    def __init__(self, movie_title, movie_storyline, poster_image,
        trailer_youtube_url, movie_rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url
        self.rating = movie_rating
    def show_trailer(self):
        webbrowser.open(self.trailer)
