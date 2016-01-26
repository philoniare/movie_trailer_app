import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.image = poster_image
        self.trailer = trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.trailer)
        return self.trailer
