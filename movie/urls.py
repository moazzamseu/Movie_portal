"""Imdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import MovieList, MovieDetail, MovieCategory, MovieLanguage, MovieSearch, MovieYear

app_name = 'movie'

urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('category/<str:category>', MovieCategory.as_view(), name='movie_category'),
    path('language/<str:lang>', MovieLanguage.as_view(), name='movie_language'),
    path('search/', MovieSearch.as_view(), name='movie_search'),
    path('<slug:slug>', MovieDetail.as_view(), name='movie_detail'),
    path('year/<int:year>', MovieYear.as_view(), name='movie_year'),
]