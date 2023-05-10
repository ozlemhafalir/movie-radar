# Movie Radar

[Movie Radar](https://movie-radar.herokuapp.com/) is a Python console application that suggests users list of movies based on genres of their likings among the random top 250 IMDB movies.

## Program Flow
![Program Flow](https://raw.githubusercontent.com/ozlemhafalir/movie-radar/main/assets/movie-radar-program-flow.jpg)

## Sample program output

```shell
python run.py

----------------------------------------------------------------------
Welcome! You will be asked with 30 random top 250 IMDB movies.
Answer with y if like the movie, answer with n otherwise.
When you have 5 likes, we'll calculate your movie taste and suggest movies.
Press enter a username/nickname to continue (optional).
----------------------------------------------------------------------
Ozlem
> [1953] Tokyo Story 
y
> [1989] Dead Poets Society 
n
> [1988] Die Hard 
y
> [2015] Mad Max: Fury Road 
n
> [1958] Vertigo 
y
> [2016] Dangal 
y
> [1942] Casablanca 
y
Please wait while we are fetching the genres of your favorite movies
> Fetching genres of Tokyo Story...: ['Drama']
> Fetching genres of Die Hard...: ['Action', 'Thriller']
> Fetching genres of Vertigo...: ['Mystery', 'Romance', 'Thriller']
> Fetching genres of Dangal...: ['Action', 'Biography', 'Drama', 'Sport']
> Fetching genres of Casablanca...: ['Drama', 'Romance', 'War']

----------------------------------------------------------------------
Your favorite genres are: Drama, Action, Thriller
Here are some suggestions for you:
----------------------------------------------------------------------
[2023] The Hunger Games: The Ballad of Songbirds and Snakes
[2023] 65
[2021] Nobody
[2022] The Batman
[2017] Blade Runner 2049
[2008] The Dark Knight
[2023] To Catch a Killer
[2022] The Northman
[1994] Léon: The Professional
[1982] Blade Runner

Creating your certificate
You can download your certificate from: https://docs.google.com/document/d/1wfjQJS9TjTkGkeZ085mNsvO7TT3HRdxuwasIUq9j2fU/edit?usp=drivesdk

Do you want to try again? (y/n): y
> [1941] Citizen Kane 
n
> [2010] Toy Story 3 
n
> [1975] Barry Lyndon 
n
> [1927] Metropolis 
n
> [1973] The Sting 
n
> [1997] Children of Heaven 
n
> [1953] The Wages of Fear 
n
> [1957] Wild Strawberries 
n
> [2007] No Country for Old Men 
u
Please answer with y or n. Do you like: [2007] No Country for Old Men 
n
> [2014] Wild Tales 
n
> [1967] Cool Hand Luke 
n
> [1972] The Godfather 
n
> [2009] Up 
n
> [1998] The Truman Show 
n
> [2016] The Handmaiden 
n
> [1954] Rear Window 
n
> [1984] Once Upon a Time in America 
n
> [2019] Ford v Ferrari 
n
> [2019] Parasite 
n
> [1928] The Passion of Joan of Arc 
n
> [1980] Raging Bull 
n
> [2005] My Father and My Son 
n
> [2007] Ratatouille 
n
> [2008] Gran Torino 
n
> [2009] Hachi: A Dog's Tale 
n
> [2004] Million Dollar Baby 
n
> [1976] Network 
n
> [1985] Back to the Future 
n
> [1949] The Third Man 
n
> [2009] The Secret in Their Eyes 
n
You didn't have enough likes for your movie taste to be calculated

Do you want to try again? (y/n): n

```


## Deployment
This application is deployed to Heroku, under: https://movie-radar.herokuapp.com/

Heroku app is created using heroku/python and heroku/nodejs build packs.

Heroku app is connected to the GitHub repository, listening to main branch, whenever a commit is pushed to the branch, Heroku triggers the pipeline and deploys the new version of the application.

Since the project is using this template: https://github.com/Code-Institute-Org/python-essentials-template, everything needed for the application to run in Heroku is already implemented.

Config vars for CREDS and DRIVE_PARENT_DIRECTORY are configured in Heroku


## Testing

### Running the application locally.
You need to have a creds.json file for a service account that has access to drive and docs APIs.

You should install the dependencies:

```shell
$ pip install -r requirements.txt
```

You can then run:

```shell
$ python run.py
```

### Pep8

✅ Using flake8 and pylint for run.py no issue was detected:

```shell
% flake8 run.py
% pylint run.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```


Only with the usage of `googleapiclient` I needed to ignore `# pylint: disable=maybe-no-member`
This is how they handled in their official documentation as well: https://developers.google.com/drive/api/guides/manage-uploads

✅ Program validates the user input and responds with useful message.


## Known issues

Getting genre takes some time. It is a slow function from Cinemagoer library.

## References

### Cinemagoer

I searched for python libraries to get movies, there were other alternatives but this was the most up-to-date library.

* [Cinemagoer Homepage](https://cinemagoer.github.io/)
* [Cinemagoer GitHub Repository](https://github.com/cinemagoer/cinemagoer)

The documentation was not great but was enough to make it work. It is still easy to use.

### Google API Python Client

The program creates a document (certificate) as output.

In order to interact with Google Docs API and Google Drive API, I used this official library, following the official documentation: https://developers.google.com/docs/api/quickstart/python

The Certificate files are created under a directory on my Google Drive, using a GCP service account that was given write access.

Since the directory has read access to everyone with link, the url printed in the application is accessible to end users.
