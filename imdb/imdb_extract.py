import json
from imdb.models import *
file = "/home/r/imdb_project/imdb/actors_5000.json"
with open(file) as page:
    # data = page.read()
    data = json.loads()




# def populate_actors(data):
#     for actor in actors_list:
#         a = Actor.objects.create(
#             full_name = actor['actor_id'],
#             name = actor['name'],
#             # age = actor['age'],
#             # dob = actor['dob'],
#             gender = actor['gender']
#         )