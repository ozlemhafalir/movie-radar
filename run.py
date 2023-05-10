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


def get_genres_of_movie(movie):
    """
    Helper function to get genres of movie,
    by using Cinemagoer's get_movie function
    Returns a list of genre string
    """
    try:
        movie_info = cinemagoer.get_movie(movie.movieID)
        genres = movie_info["genres"]
        return genres
    except IMDbError:
        print("Error during getting movie from Cinemagoer")
        return []


def get_top_genre_movie_infos(top_genres_list):
    """
    Using the genre list, fetches top 50 movies and returns top 10 as MovieBasicInfo list
    """
    try:
        top_genre_movies = cinemagoer.get_top50_movies_by_genres(top_genres_list)[:10]
        top_genre_movie_infos = [MovieBasicInfo(movie) for movie in top_genre_movies]
        return top_genre_movie_infos
    except IMDbError:
        print("Error during getting genre movies from Cinemagoer")
        return []


def get_user_movie_liking(movie):
    """
    Helper function to ask if user likes the movie,
    parse the answer and return bool value.
    """
    movie_basic_info = MovieBasicInfo(movie)
    answer = input(f"> {movie_basic_info} \n")
    while answer not in ["y", "n"]:
        answer = input(
            "Please answer with y or n. Do you like: " f"{movie_basic_info} \n"
        )
    return answer == "y"


def get_liked_movies(movies):
    """
    For each movie, ask users if they like the move,
    if yes, add genres to genres dictionary
    :param movies: cinemagoer movies
    """
    liked_movies = []
    for movie in movies:
        if get_user_movie_liking(movie):
            liked_movies.append(movie)
            if len(liked_movies) == NUMBER_OF_REQUIRED_LIKES:
                break
    return liked_movies


def get_liked_genres_with_movies(movies):
    """
    For each movie, ask users if they like the move,
    if yes, add genres to genres dictionary
    """
    liked_genres = {}
    for movie in movies:
        print(f"> Fetching genres of {movie}...", end=": ", flush=True)
        genres = get_genres_of_movie(movie)
        print(genres)
        for genre in genres:
            liked_genres[genre] = liked_genres.get(genre, 0) + 1
    return liked_genres


def start_game(username):
    """
    Game logic
    """
    print(f"Hello, {username}")
    random_movies = get_randomized_top_250_movies()
    if len(random_movies) == 0:
        print("Please try again later.")
    else:
        liked_movies = get_liked_movies(random_movies)
        if len(liked_movies) == NUMBER_OF_REQUIRED_LIKES:
            print(
                "Please wait while we are fetching the genres of your favorite movies"
            )
            liked_genres = get_liked_genres_with_movies(liked_movies)
            suggested_movies = get_top_genre_movie_infos(
                list(set(liked_genres.keys()))[:3]
            )
            print(suggested_movies)
        else:
            print("You didn't have enough likes for your movie taste to be calculated")


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
