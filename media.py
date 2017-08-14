# Movie trailer website for Udacity Full Stack Web Developer project 1
# fresh_tomatoes.py from https://github.com/udacity/ud036_StarterCode

# import webbrowser module to open system browser
import webbrowser

# defines the Movie class


class Movie():

    # constructor defines properties about movie and sets instance variables
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # define instance method to open browser and play the movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
