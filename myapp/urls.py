from django.conf.urls import patterns, url

from myapp import views

urlpatterns = patterns('',
    url(r'^$', views.startpage, name='startpage'),
    
    url(r'^film/$', views.films, name='films'),
    url(r'^film/(?P<film_id>\d+)/$', views.film, name='film'),
    
    url(r'^cinema/$', views.cinemas, name='cinemas'),
    url(r'^cinema/(?P<cinema_id>\d+)/$', views.cinema, name='cinema'),
    
    url(r'^session/$', views.sessions, name='sessions'),
    url(r'^session/(?P<session_id>\d+)/$', views.session, name='session'),
    
    url(r'^search-film/$', views.searchFilm),
    url(r'^search-cinema/$', views.searchCinema),
    url(r'^search-session/$', views.searchSession),
    url(r'^search-film/search/$', views.searchFilmRes),
    url(r'^search-cinema/search/$', views.searchCinemaRes),
    url(r'^search-session/search/$', views.searchSessionRes)
    
)
