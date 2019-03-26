from random import randint

movies=["dgbz la battallita",
        "avengers",
        "bosque maldito",
        "cementerio de erros",
        "maldicion de hillhouse",
        "amytville"]

def show_movies():
    for movie in movies:
        print(movie)

def get_specific_movie(position):
    return movies[position]

def get_random_number():
    return randint(0,(len(movies)-1))

def get_random_number_concatenate():
    return randint(0,3)

def return_concatenate_token():
    switcher = {
    0: " La primer ",
    1: " Contra "   ,
    2: " y tambien ",
    3: "  en compañia de "
    }
    return switcher.get(get_random_number_concatenate())

def mix_movies():
    title=" Beliculitas presenta "
    for movie in movies:
        title=title+get_specific_movie(get_random_number())+return_concatenate_token()
    return title



print(mix_movies())
