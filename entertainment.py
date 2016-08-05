import media
import fresh_tomatoes


"""---------------------------Movies--------------------------------------"""

"""	Format : title, storyline,	poster_image, trailer_youtube, \
             year_release, runing_time,	movie_rating """

the_intouchables = media.Movie("The Intouchables",
                               "A quadriplegic aristocrat hires a young \
                               from the projects to be his caregiver",
                               "http://ia.media-imdb.com/images/M/MV5BMTYxNDA3MDQwNl5BMl5BanBnXkFtZTcwNTU4Mzc1Nw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # noqa
                               "https://youtu.be/34WIbmXkewU",
                               "2011",
                               "112 minutes",
                               "8.6/10"
                               )


the_green_mile = media.Movie("The green mile",
                             "The lives of guards on Death Row are affected \
                             by one of their charges",
                             "http://ia.media-imdb.com/images/M/MV5BMTUxMzQyNjA5MF5BMl5BanBnXkFtZTYwOTU2NTY3._V1_.jpg",  # noqa
                             "https://youtu.be/ctRK-4Vt7dA",
                             "1999",
                             "189 minutes",
                             "8.5/10")

into_the_wild = media.Movie("Into the wild",
                            "A student hitchhikes to Alaska to live in the \
                            wilderness.",
                            "http://ia.media-imdb.com/images/M/MV5BMTAwNDEyODU1MjheQTJeQWpwZ15BbWU2MDc3NDQwNw@@._V1_.jpg",  # noqa
                            "https://youtu.be/g7ArZ7VD-QQ",
                            "2007",
                            "148 minutes",
                            "8.2/10")

amelie = media.Movie("Amelie",
                     "Amelie decides to help those around her and, along the \
                     way, discovers love",
                     "http://ia.media-imdb.com/images/M/MV5BNDg4NjM1YjMtYmNhZC00MjM0LWFiZmYtNGY1YjA3MzZmODc5XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_CR0,0,666,1000_AL_.jpg",  # noqa
                     "https://youtu.be/2UT5xaAfxWU",
                     "2001",
                     "122 minutes",
                     "8.4")

toy_story = media.Movie("Toy Story",
                        "A movie of a boy and his toys",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # noqa
                        "https://youtu.be/4KPTXpQehio",
                        "2010",
                        "103 minutes",
                        "8.3/10")

boyhood = media.Movie("Boyhood",
                      "BOYHOOD charts the rocky terrain of childhood",
                      "https://upload.wikimedia.org/wikipedia/en/b/bb/Boyhood_film.jpg",  # noqa
                      "https://youtu.be/Y0oX0xiwOv8",
                      "2014",
                      "166 minutes",
                      "8/10")


"""---------------------TV Shows------------------------------"""

"""	Format: title, storyline, poster_image, trailer_youtube, \
            year_release,	running_time,	number_of_seasons """


breaking_bad = media.TvShow("Breaking bad",
                            "Story of a struggling high school chemistry \
                            teacher diagnosed with inoperable lung cancer",
                            "http://ia.media-imdb.com/images/M/MV5BMTQ0ODYzODc0OV5BMl5BanBnXkFtZTgwMDk3OTcyMDE@._V1_SY1000_CR0,0,678,1000_AL_.jpg",  # noqa
                            "https://youtu.be/HhesaQXLuRY",
                            "2008",
                            "43-58 minutes",
                            "9.5/10",
                            "5 seasons")

big_bang_theory = media.TvShow("The Big Bang Theory",
                               "The show is primarily centered on five characters \
                               living in Pasadena, California",
                               "http://ia.media-imdb.com/images/M/MV5BMjI1Mzc4MDUwNl5BMl5BanBnXkFtZTgwMDAzOTIxMjE@._V1_SY1000_CR0,0,799,1000_AL_.jpg",  # noqa
                               "https://youtu.be/WBb3fojgW0Q",
                               "2005",
                               "18-24 minutes",
                               "8.4/10",
                               "9 seasons")

mr_robot = media.TvShow("Mr. Robot",
                        "Story of a young programmer who works as a cyber-security \
                        engineer by day and a vigilante hacker by night.",
                        "http://ia.media-imdb.com/images/M/MV5BMTYzMDE2MzI4MF5BMl5BanBnXkFtZTgwNTkxODgxOTE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # noqa
                        "https://youtu.be/U94litUpZuc",
                        "2015",
                        "49 minutes",
                        "8.8/10",
                        "2 seasons")

the_office = media.TvShow("The office",
                          "Office live",
                          "http://ia.media-imdb.com/images/M/MV5BMTgzNjAzMDE0NF5BMl5BanBnXkFtZTcwNTEyMzM3OA@@._V1_SY1000_CR0,0,736,1000_AL_.jpg",  # noqa
                          "https://youtu.be/M_0o-qehYTU",
                          "2005",
                          "22-28 minutes",
                          "8.8/10",
                          "9 seasons")

sons_of_anarchy = media.TvShow("Sons of anarchy",
                               "A man struggles to find a balance in his \
                               life between being a dad and his involvement \
                               in a motorcycle club.",
                               "http://ia.media-imdb.com/images/M/MV5BMTEyODg2NzkwMDBeQTJeQWpwZ15BbWU4MDQwODI3MzIx._V1_.jpg",  # noqa
                               "https://youtu.be/_03DBXL3Srw",
                               "2008",
                               "45 minutes",
                               "8.6/10",
                               "7 seasons")

better_call_saul = media.TvShow("Better call Saul",
                                "The trials and tribulations of criminal \
                                lawyer",
                                "http://ia.media-imdb.com/images/M/MV5BNjk5MjYwNjg4NV5BMl5BanBnXkFtZTgwNzAzMzc5NzE@._V1_.jpg",  # noqa
                                "https://youtu.be/lK_70f7PamE",
                                "2015",
                                "46 minutes",
                                "8.8/10",
                                "3 seasons")

"""---------------------------------------------------------"""

# List of movies
movies = [the_intouchables, the_green_mile,
          into_the_wild, amelie, boyhood, toy_story]

# List of Tv Shows
tvshow = [breaking_bad, big_bang_theory, mr_robot,
          the_office, better_call_saul, sons_of_anarchy]


def video_input():
    """ Input at the begining of the programm.
    Redirect to movies or tv shows. """

    print "Movies or TV Shows?"
    output = 0

    while output != 1:
        name = raw_input().lower()

        if name == "movies":
            fresh_tomatoes.open_movies_page(movies)
            output += 1
        elif name == "tv shows":
            fresh_tomatoes.open_movies_page(tvshow)
            output += 1
        else:
            print "I don't understand. Choose between 'Movies' or 'Tv Shows'"

start = video_input()

print start
