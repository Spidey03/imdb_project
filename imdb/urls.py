from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'index'),
    path('home/', views.home, name = 'Home'),
    path('movie/<int:movie_id>/', views.movie_page, name = 'Movie'),
    path('actor/<int:actor_id>/',views.actor, name = 'Actor'),
    path('director/<int:director_id>/', views.director, name = 'Director'),
    path('analytics/',views.analytics, name = 'Analytics Page'),
]
