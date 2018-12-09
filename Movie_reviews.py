import webbrowser
class Movie():
    """Crappy Description goes here"""
    VALID_RATINGS = ["G","PG", "PG-13", "R"]
    def __init__(self, movie_title, movie_storyline, poster_image, movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class TV():
    def __init__(self, series_title, series_description, series_poster, imdb_link):
        self.title = series_title
        self.description = series_description
        self.poster_image = series_poster
        self.imdb = imdb_link
