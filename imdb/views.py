from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# from .utils import *
# Create your views here.

def index(request):
    return HttpResponse('Hello_World')

def home(request):
    res = request.GET
    #print(res)
    if res == {}:
        movies = Movie.objects.all()
    movies = {'movies':movies}
    return render(request, 'imdb_home.html', movies)

def movie_page(request,movie_id):
    res = request.GET
    if res == {}:
        movie = Movie.objects.get(id = movie_id)
        cast = Cast.objects.filter(movie = movie)
        act = []
        for actor in cast:
            act.append(actor)
    return render(request, 'imdb_movie.html',{'movie' : movie, 'cast':act})

def actor(request, actor_id):
    res = request.GET
    if res == {}:
        actor = Actor.objects.get(id = actor_id)
    return render(request, 'imdb_actor.html',{'actor':actor})

def director(request, director_id):
    res = request.GET
    if res == {}:
        director_obj = Director.objects.get(id = director_id)
    return render(request, 'imdb_director.html',{'director' : director_obj})

def analytics(request):
    #from .utils import get_Movie_collections_one_bar_plot_data, get_Movie_collections_chart_data, get_two_bar_plot_data_director_hits, get_area_plot_data_movie_year


    from .analytics import get_two_bar_plot_data_director_hits, get_area_plot_data_movie_year,get_pie_chart_data_gender, get_doughnut_chart_data_genre, get_multi_line_plot_data_gender, get_polar_chart_data_genre, get_one_bar_plot_data_subscribers, get_one_bar_plot_data_award_nominees

    

    data = get_two_bar_plot_data_director_hits()
    data.update(get_area_plot_data_movie_year())
    data.update(get_pie_chart_data_gender())
    data.update(get_doughnut_chart_data_genre())
    data.update(get_multi_line_plot_data_gender())
    data.update(get_polar_chart_data_genre())
    data.update(get_one_bar_plot_data_subscribers())
    data.update(get_one_bar_plot_data_award_nominees())
    return render(request, 'analytics.html',context = data)
