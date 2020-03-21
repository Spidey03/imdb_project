from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Views
# Homepage
def home(request):
    if request.method == 'POST':
        res = request.POST.get('movie')
        try:
            Movie.objects.get(id = res).delete()
        except Movie.DoesNotExist:
            pass
    movies = Movie.objects.all()
    movies = {'movies':movies}
    return render(request, 'imdb_home.html', movies)
# Movie Page
def movie_page(request,movie_id):
    movie = Movie.objects.get(id = movie_id)
    cast = Cast.objects.filter(movie = movie)
    act = []
    for actor in cast:
        act.append(actor)
    return render(request, 'imdb_movie.html',{'movie' : movie, 'cast':act})
# Actor Page
def actor(request, actor_id):
    actor = Actor.objects.get(id = actor_id)
    return render(request, 'imdb_actor.html',{'actor':actor})
# Director Page
def director(request, director_id):
    director_obj = Director.objects.get(id = director_id)
    return render(request, 'imdb_director.html',{'director' : director_obj})
# analytics
def analytics(request):
    from .analytics import get_two_bar_plot_data_director_hits, get_area_plot_data_movie_year,get_pie_chart_data_gender, get_doughnut_chart_data_genre, get_multi_line_plot_data_gender, get_polar_chart_data_genre, get_one_bar_plot_data_subscribers, get_one_bar_plot_data_award_nominees
    data = get_two_bar_plot_data_director_hits()
    data.update(get_area_plot_data_movie_year())
    data.update(get_pie_chart_data_gender())
    data.update(get_doughnut_chart_data_genre())
    data.update(get_multi_line_plot_data_gender())
    data.update(get_polar_chart_data_genre())
    data.update(get_one_bar_plot_data_subscribers())
    # data.update(get_one_bar_plot_data_award_nominees())
    return render(request, 'analytics.html',context = data)
