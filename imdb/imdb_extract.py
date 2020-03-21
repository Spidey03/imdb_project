import json
import requests
import re


file = "/home/r/Downloads/100_movies/movies_100.json"
page = open(file,'r')
data = page.read()


movies_list = json.loads(data)
for movie in movies_list[:1]:

    pattern = f"""<a href="{movie['imdb_link'][19:]}"(.+?)</a>"""
    print(pattern)
    pattern = re.compile(pattern)
    print(movie['imdb_link'][19:])
    
    data = requests.get('http://www.imdb.com/title/tt0499549/?ref_=fn_tt_tt_1')
    result = pattern.findall(data.text)
    print(result)