"""
Application for receiving the liked movies from user
and suggest what to watch next.
"""
import dataclasses
import random

from imdb import IMDbError, Cinemagoer

NUMBER_OF_MOVIES = 30
NUMBER_OF_REQUIRED_LIKES = 5

cinemagoer = Cinemagoer()


@dataclasses.dataclass
class MovieBasicInfo:
    """Class definition for movie"""

    title: str
    year: str

    def __init__(self, movie):
        self.title = movie.data["title"]
        self.year = movie.data.get("year", "")

    def __str__(self):
        return f"[{self.year}] {self.title}"


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


def start_game(username):
    """
    Game logic
    """
    print(f"Hello, {username}")
    random_movies = get_randomized_top_250_movies()
    if len(random_movies) == 0:
        print("Please try again later.")
    else:
        print(random_movies)


def main():
    username = input(
        f"""
----------------------------------------------------------------------
Welcome! You will be asked with {NUMBER_OF_MOVIES} random top 250 IMDB movies.
Answer with y if like the movie, answer with n otherwise.
When you have {NUMBER_OF_REQUIRED_LIKES} likes, we'll calculate your movie taste and suggest movies.
Press enter a username/nickname to continue.
----------------------------------------------------------------------
"""
    )
    start_game(username)
    while input("\nDo you want to try again? (y/n): ") == "y":
        start_game(username)


main()
