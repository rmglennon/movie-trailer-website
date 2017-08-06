# Rhonda Glennon - Movie trailer website for Udacity Full Stack Web Developer project 1
# fresh_tomatoes.py from https://github.com/udacity/ud036_StarterCode

# Import media.py file that defines the classes and fresh_tomatoes.py that creates the movies webpage
import fresh_tomatoes
import media

# Movie is a class inside media.py
# create instance of movies with name, storyline, poster image, YouTube URL

all_the_presidents_men = media.Movie("All the President's Men", "Two reporters investigate the Watergate scandal.",
                       "https://upload.wikimedia.org/wikipedia/en/9/92/All_the_president%27s_men.jpg",
                       "https://www.youtube.com/watch?v=vLt6djxhNe8")

gone_with_the_wind = media.Movie("Gone With the Wind", "Romance and reconstruction in Civil War-era Georgia.",
                                 "https://upload.wikimedia.org/wikipedia/commons/2/27/Poster_-_Gone_With_the_Wind_01.jpg",
                                 "https://www.youtube.com/watch?v=Q8iIbO9uBkc")

muppet_movie = media.Movie("The Muppet Movie", "The Muppets travel across the country to make a movie",
                           "https://upload.wikimedia.org/wikipedia/en/a/a8/The_Muppet_Movie.jpg",
                           "https://www.youtube.com/watch?v=N31JLdKmHIE")

national_lampoons_vacation = media.Movie("National Lampoon's Vacation", "Everything goes wrong on a family's roadtrip.",
                                         "https://upload.wikimedia.org/wikipedia/en/a/a8/Vacation1983.jpg",
                                         "https://www.youtube.com/watch?v=rYcz5MsDgE4")

skyfall = media.Movie("Skyfall", "James Bond tracks a former agent-turned cyberterrorist.",
                      "http://www.007.com/wp-content/uploads/2012/09/SKYFALL-UK-POSTER_650.jpg",
                      "https://www.youtube.com/watch?v=6kw1UVovByw")

star_wars = media.Movie("Star Wars", "An epic battle a long time ago in another galaxy.",
                        "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                        "https://www.youtube.com/watch?v=vZ734NWnAHA")

# Add the movies to a list
movies = [all_the_presidents_men, gone_with_the_wind, muppet_movie, national_lampoons_vacation, skyfall, star_wars]

# Pass the list of movies to the function and build the webpage
fresh_tomatoes.open_movies_page(movies)
