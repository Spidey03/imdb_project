from imdb.models import *
import json

awards_list = [
    "SIIMA",
    "OSCAR",
    "Filmfare Awards",
    "Nandi Awards",
    "Zee Cine Awards",
    "cineMAA Awards",
    "Vanitha Film Awards"
]

actors_list =[
        {
            "full_name" : "Konidela Pawan Kalyan Babu",
            "name" : "Pawan Kalyan",
            "dob" : "1971-09-02",
            "age" : 48,
            "gender" : "M",
            "awards":[
                1,2,3
            ]
        },
        {
            "full_name" : "Shruthi Haasan",
            "name" : "Shruthi Haasan",
            "dob" : "1986-02-28",
            "age" :34,
            "gender" : "F",
            "awards":[
                7
            ]
        },
        {
            "full_name" : "Samantha Akkineni",
            "name" : "Samantha Akkineni",
            "dob" : "1987-04-28",
            "age" :32,
            "gender" : "F",
            "awards":[
                1,3,4
            ]
        },
        {
            "full_name" : "Uppalapati Venkata Satyanarayana Prabhas Raju",
            "name" : "Prabas",
            "dob" : "1979-10-23",
            "age" :40,
            "gender" : "M",
            "awards":[
                4,5
            ]
        },
        {
            "full_name" : "Anushka Shetty",
            "name" : "Anushka",
            "dob" : "1981-11-07",
            "age" :38,
            "gender" : "F",
            "awards":[
                1,4,3
            ]
        },
        {
            "full_name" : "Tamanna Bhatia",
            "name" : "Tamanna",
            "dob" : "1989-12-21",
            "age" :30,
            "gender" : "F",
            "awards":[
                7
            ]
        },
        {
            "full_name" : "Nandamuri Taraka Rama Rao Jr",
            "name" : "Jr. NTR",
            "dob" : "1983-05-20",
            "age" :36,
            "gender" : "M",
            "awards":[
                1,2,3
            ]
        },
        
    ]

directors_list = [
        "Karunakaran",
        "Harish Shankar",
        "Trivikram Srinivas",
        "S. S. Rajamouli",
        "Puri Jagannadh"
    ]

movies_list = [
        {
            "name": "Tholi Prema",
            "actors": [
                {
                    "actor_id": "1",
                    "role": "Balu",
                    "is_debut_movie": False
                }
            ],
            "genres" : [
                {
                    "name" : "Romance"
                }
            ],
            "languages":[
                {
                    "name" : "Telugu"
                }
            ],
            "collections": 90.9,
            "date_of_release": "2000-02-03",
            "director": "Karunakaran",
            "no_of_subscribers" : 10000,
        },
        {
            "name": "Gabber Singh",
            "actors": [
                {
                    "actor_id": "1",
                    "role": "Gabber Sing",
                    "is_debut_movie": False
                },
                {
                    "actor_id": "2",
                    "role": "Bala",
                    "is_debut_movie": False
                }
            ],
            "genres" : [
                {
                    "name" : "Action"
                }
            ],
            "languages":[
                {
                    "name" : "Telugu"
                }
            ],
            "collections": 100.9,
            "date_of_release": "2002-05-03",
            "director": "Harish Shankar",
            "no_of_subscribers" : 1000,
        },
        {
            "name": "Attarintiki Dharedhi",
            "actors": [
                {
                    "actor_id": "1",
                    "role": "Gautham",
                    "is_debut_movie": False
                },
                {
                    "actor_id": "3",
                    "role": "Shasi",
                    "is_debut_movie": False
                }
            ],
            "genres" : [
                {
                    "name" : "Romance"
                },
                {
                    "name" : "Comedy"
                }
            ],
            "languages":[
                {
                    "name" : "Telugu"
                }
            ],
            "collections": 80.9,
            "date_of_release": "2005-02-03",
            "director": "Trivikram Srinivas",
            "no_of_subscribers" : 20000,
        },
        {
            "name": "Baahubali: The Beginning",
            "actors": [
                {
                    "actor_id": "4",
                    "role": "Shivudu",
                    "is_debut_movie": False
                },
                {
                    "actor_id": "4",
                    "role": "Baahubali",
                    "is_debut_movie": False
                },
                {
                    "actor_id": "5",
                    "role": "Devasena",
                    "is_debut_movie": False
                },
                {
                    "actor_id": "6",
                    "role": "Avantika",
                    "is_debut_movie": False
                }
            ],
            "genres" : [
                {
                    "name" : "Romance"
                },
                {
                    "name" : "Action"
                },
                {
                    "name" : "Drama"
                },
                {
                    "name" : "War"
                },
                {
                    "name" : "Historical Fiction"
                }
            ],
            "languages":[
                {
                    "name" : "Telugu"
                },
                {
                    "name" : "Hindi"
                },
                {
                    "name" : "Tamil"
                },
                {
                    "name" : "English"
                }
            ],
            "collections": 80.9,
            "date_of_release": "2015-07-10",
            "director": "S. S. Rajamouli",
            "no_of_subscribers" : 30000,
        },
        {
            "name": "Baahubali: The Conclusion",
            "actors": [
                {
                    "actor_id": "4",
                    "role": "Shivudu",
                    "is_debut_movie": False
                },
                {
                    "actor_id": "4",
                    "role": "Baahubali",
                    "is_debut_movie": False
                },
                {
                    "actor_id": "5",
                    "role": "Devasena",
                    "is_debut_movie": False
                },
                {
                    "actor_id": "6",
                    "role": "Avantika",
                    "is_debut_movie": False
                }
            ],
            "genres" : [
                {
                    "name" : "Romance"
                },
                {
                    "name" : "Action"
                },
                {
                    "name" : "Drama"
                },
                {
                    "name" : "War"
                },
                {
                    "name" : "Historical Fiction"
                }
            ],
            "languages":[
                {
                    "name" : "Telugu"
                },
                {
                    "name" : "Hindi"
                },
                {
                    "name" : "Tamil"
                },
                {
                    "name" : "English"
                }
            ],
            "collections": 100.9,
            "date_of_release": "2015-07-10",
            "director": "S. S. Rajamouli",
            "no_of_subscribers" : 50000,
        },
        {
            "name": "Temper",
            "actors": [
                {
                    "actor_id": "7",
                    "role": "Daya",
                    "is_debut_movie": False
                }
            ],
            "genres" : [
                {
                    "name" : "Romance"
                },
                {
                    "name" : "Action"
                }
            ],
            "languages":[
                {
                    "name" : "Telugu"
                },
                {
                    "name" : "Hindi"
                }
            ],
            "collections": 70.9,
            "date_of_release": "2015-02-13",
            "director": "Puri Jagannadh",
            "no_of_subscribers" : 50000,
        },
    ]

genre_list = [
    {
        "name" : "Romance"
    },
    {
        "name" : "Comedy"
    },
    {
        "name" : "Action"
    },
    {
        "name" : "War"
    },
    {
        "name" : "Historical Fiction"
    },
    {
        "name" : "Drama"
    },
    {
        "name" : "Sci-Fi"
    }
]

language_list = [
    {
        "name" : "Telugu",
    },
    {
        "name" : "Kannada",
    },
    {
        "name" : "Hindi",
    },
    {
        "name" : "English",
    },
    {
        "name" : "Tamil",
    },
]

movie_rating_list = [
        {
            "id": "1",
            "rating1": 10,
            "rating2": 10,
            "rating3": 50,
            "rating4": 100,
            "rating5": 120
        },
        {
            "id": "2",
            "rating1": 10,
            "rating2": 5,
            "rating3": 100,
            "rating4": 100,
            "rating5": 100
        },
        {
            "id": "3",
            "rating1": 10,
            "rating2": 10,
            "rating3": 100,
            "rating4": 40,
            "rating5": 50
        },
        {
            "id": "4",
            "rating1":9,
            "rating2": 10,
            "rating3": 100,
            "rating4": 40,
            "rating5": 120
        },
        {
            "id": "5",
            "rating1":20,
            "rating2": 20,
            "rating3": 100,
            "rating4": 30,
            "rating5": 100
        },
        {
            "id": "6",
            "rating1":9,
            "rating2": 10,
            "rating3": 100,
            "rating4": 40,
            "rating5": 120
        },
    ]

import json
# Actors List
file = "/home/r/imdb_project/imdb/complete_data/actors_5000.json"
# file = "/home/r/imdb_project/imdb/100_movies/actors_100.json"
page = open(file,'r')
data = page.read()
actors_list = json.loads(data)

# Director List
file = "/home/r/imdb_project/imdb/complete_data/directors_5000.json"
# file = "/home/r/imdb_project/imdb/100_movies/directors_100.json"
page = open(file,'r')
data = page.read()
directors_list = json.loads(data)

# Movie List
file = "/home/r/imdb_project/imdb/complete_data/movies_5000.json"
# file = "/home/r/imdb_project/imdb/100_movies/movies_100.json"
page = open(file,'r')
data = page.read()
movies_list = json.loads(data)



from imdb.models import *
import uuid
def populate_directors(directors_list):
    for director in directors_list:
        if director['no_of_facebook_likes'] == '':
            no_of_facebook_likes = 0
        else:
            no_of_facebook_likes = director['no_of_facebook_likes']
        Director.objects.create(
            name = director['name'],
            gender = director['gender'],
            no_of_facebook_likes = no_of_facebook_likes
        )

def populate_actors(actors_list):
    for actor in actors_list:
        a = Actor.objects.create(
            full_name = actor['actor_id'],
            name = actor['name'],
            gender = actor['gender'],
            fblikes = actor['fb_likes']
        )

def populate_movies(movies_list):
    for movie in movies_list:
        if movie['year_of_release'] == '':
            release = 0
        else:
            release = int(movie['year_of_release'])

        m = Movie.objects.create(
            # id = uuid.uuid4(),
            name = movie['name'],
            director = Director.objects.get(name = movie['director_name']),
            release = release,
            collections = float(movie['box_office_collection_in_crores']),
            avg_rating = float(movie['average_rating']),
            no_of_subscribers = int(movie['no_of_users_voted']),
            language = movie['language']
        )
        for genre in movie['genres']:
            try:
                genre_obj = Genre.objects.get(name = genre)
            except Genre.DoesNotExist:
                genre_obj = Genre.objects.create(name = genre)
            finally:
                m.genre.add(genre_obj)
        for actor in movie['actors']:
            Cast.objects.create(
                actor = Actor.objects.get(full_name = actor['actor_id']),
                movie = m,
                role = actor['role'],
                is_debut_movie = actor['is_debut_movie']
            )

def populate():
    print('Populating Directors...')
    populate_directors(directors_list)
    print('Populating Actors...')
    populate_actors(actors_list)
    print('Inserting Movies...')
    populate_movies(movies_list)


# def populate_database(actors_list = [], movies_list = [], directors_list = [], movie_rating_list = [], genre_list = [], language_list = [], awards_list = []):
#     from .models import Actor


#     for award in awards_list:
#         Award.objects.create(name = award)


#     for actor in actors_list:
#         a = Actor.objects.create(
#             full_name = actor['full_name'],
#             name = actor['name'],
#             age = actor['age'],
#             dob = actor['dob'],
#             gender = actor['gender']
#         )

#         for award in actor['awards']:
#             a.awards.add(Award.objects.get(id = award))
    
#     #direcor
#     for director in directors_list:
#         Director.objects.create(name = director)
    

    # for genre in genre_list:
    #     g = Genre.objects.create(
    #         name = genre['name']
    #     )
    #     # for movie in genre["movies"]:
    #     #     mov = Movie.objects.get(id = movie['id'])
    #     #     mov.genre.add(g)
    
#     for language in language_list:
#         lang = Language.objects.create(
#             name = language['name']
#         )
#         # for movie in language["movies"]:
#         #     mov = Movie.objects.get(id = movie['id'])
#         #     mov.language.add(lang)

#     #movie
#     for movie in movies_list:
#         m = Movie.objects.create(
#             name = movie['name'],
#             director = Director.objects.get(name = movie['director']),
#             date_of_release = movie['date_of_release'],
#             collections = movie['collections'],
#             no_of_subscribers = movie['no_of_subscribers']
#         )
#         for actor in movie['actors']:
#             Cast.objects.create(
#                 actor = Actor.objects.get(
#                     id = actor['actor_id']
#                 ),
#                 movie = m,
#                 role = actor['role'],
#                 #is_debut_movie = actor['is_debut_movie']
#             )
#         for genre in movie['genres']:
#             genre_obj = Genre.objects.get(name = genre['name'])
#             m.genre.add(genre_obj)
#         for lang in movie['languages']:
#             lang_obj = Language.objects.get(name = lang['name'])
#             m.language.add(lang_obj)
    
#     #rating
#     for rating in movie_rating_list:
#         m = Movie.objects.get(id = rating['id'])
#         Rating.objects.create(
#             movie = m,
#             rating1 = rating['rating1'],
#             rating2 = rating['rating2'],
#             rating3 = rating['rating3'],
#             rating4 = rating['rating4'],
#             rating5 = rating['rating5'],
#         )

    

# populate_database(actors_list, movies_list, directors_list, movie_rating_list,genre_list,language_list,awards_list)
# src="https://cdn1.iconfinder.com/data/icons/seo-and-web-development-color/64/seo-and-web-development-05-512.png"