from .models import *



# Genre objects
action = Genre.objects.create(name = 'Action')
comedy = Genre.objects.create(name = 'Comedy')
romance = Genre.objects.create(name = 'Romance')


# Director objects
karunakarn = Director.objects.create(name = 'Karunakaran')
hs = Director.objects.create(name = 'Harish Shankar')
ts = Director.objects.create(name = 'Trivikram Srinivas')

#Producer objects
prasad = Producer.objects.create(name = 'B.V.S.N.Prasad')
bganesh = Producer.objects.create(name = 'Bandla Ganesh')
raju = Producer.objects.create(name = 'G.V.G.Raju')

# Actor objects
pawan = Actor.objects.create(
    full_name = 'Konidela Pawan Kalyan Babu',
    name = 'Pawan Kalyan',
    dob = '1971-09-02',
    age = 48,
    gender = 'M'
)
sh = Actor.objects.create(
    name = 'Shruthi Haasan',
    age = 34,
    dob = '1986-02-28',
    gender = 'F'
)
samantha = Actor.objects.create(
    full_name = 'Samantha Akkineni',
    name = 'Samantha',
    age = 32,
    dob = '1987-04-28',
    gender = 'F',
)



# Movie objects
tp = Movie.objects.create(
    name = 'Tholi Prema', 
    director = karunakarn, 
    date_of_release = '2000-02-03',
    collections = 90.9
)
tp.producer.add(raju)
tp.genre.add(romance)
gs = Movie.objects.create(
    name = 'Gabber Singh',
    director = hs, 
    date_of_release = '2002-05-03',
    collections = 100.8
)
gs.genre.add(action,comedy)
gs.producer.add(bganesh)
ad = Movie.objects.create(
    name = 'Attarintiki Dharedhi', 
    director = ts, 
    date_of_release = '2005-02-03',
    collections = 80.9,
)
ad.genre.add(romance)
ad.producer.add(prasad)

# Cast objects
Cast.objects.create(actor = pawan, movie = tp, role = 'Balu')
Cast.objects.create(actor = pawan, movie = gs, role = 'Gabber Sing')
Cast.objects.create(actor = sh, movie = gs, role = 'Bala')
Cast.objects.create(actor = pawan, movie = ad, role = 'Gautham Nanda')
Cast.objects.create(actor = samantha, movie = ad, role = 'Sashi')

#rating objects

Rating.objects.create(movie = gs, rating1 = 10,rating2 = 10, rating3 = 50, rating4 = 100, rating5 = 120)
Rating.objects.create(movie = ad, rating1 = 10,rating2 = 5, rating3 = 50, rating4 = 100, rating5 = 100)
Rating.objects.create(movie = tp, rating1 = 10,rating2 = 10, rating3 = 100, rating4 = 40, rating5 = 50)