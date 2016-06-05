from Video import Video
import urllib
import webbrowser


class Movie(Video):
    """
    A program to display various details of a movie.
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]  # Implemented for future use

    def __init__(self, title, rating, duration, cast,
                 storyline, poster_image, trailer_url):
        Video.__init__(self, title, duration, cast)  # Parent Constructor call
        self.rating = rating  # The movie rating
        self.storyline = storyline  # What the movie is about
        self.trailer_youtube_url = trailer_url  # The YouTube URL of the movie.
        self.poster_image_url = poster_image  # An image of the movie poster

    def show_trailer(self):
        """
        opens up the web brower to the YouTube URL.
        """ 
        webbrowser.open(self.trailer_youtube_url)

