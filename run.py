import random

from imdb import IMDbError, Cinemagoer

NUMBER_OF_MOVIES = 30
cinemagoer = Cinemagoer()


def get_randomized_top_250_movies():
    """
    Returns a random list of movies from top 250 IMDB movies.
    """
    try:
        movies = cinemagoer.get_top250_movies()
        random_indexes = random.sample(range(0, len(movies)), NUMBER_OF_MOVIES)
        return [movies[index] for index in random_indexes]
    except IMDbError:
        print("Error during getting movies from Cinemagoer")
        return []


def main():
    """Starts the game."""
    random_movies = get_randomized_top_250_movies()
    print(random_movies)


main()
