import json

def all_movies(_, info):
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        return movies['movies']

def movie_with_id(_,info,_id):
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        for movie in movies['movies']:
            if movie['id'] == _id:
                return movie

def update_movie_rate(_,info,_id,_rate):
    newmovies = {}
    newmovie = {}
    with open('{}/data/movies.json'.format("."), "r") as rfile:
        movies = json.load(rfile)
        for movie in movies['movies']:
            if movie['id'] == _id:
                movie['rating'] = _rate
                newmovie = movie
                newmovies = movies
    with open('{}/data/movies.json'.format("."), "w") as wfile:
        json.dump(newmovies, wfile)
    return newmovie

def add_movie(_, info, _id, _title, _director, _rating):
    with open('{}/data/movies.json'.format("."), "r") as rfile:
        movies = json.load(rfile)
    
    new_movie = {
        "id": _id,
        "title": _title,
        "rating": _rating,
        "director": _director
    }

    movies['movies'].append(new_movie)

    with open('./data/movies.json'.format("."), "w") as wfile:
        json.dump(movies, wfile)
    return new_movie

def delete_movie(_, info, _id):
    with open('{}/data/movies.json'.format("."), "r") as rfile:
        movies = json.load(rfile)
    
    movie_to_delete = None
    updated_movies = []
    
    for movie in movies['movies']:
        if movie['id'] == _id:
            movie_to_delete = movie  # Film à supprimer trouvé
        else:
            updated_movies.append(movie)  # Garder les autres films
    
    if movie_to_delete is None:
        return None
    
    movies['movies'] = updated_movies
    
    with open('./data/movies.json', "w") as wfile:
        json.dump(movies, wfile)
    
    return movie_to_delete