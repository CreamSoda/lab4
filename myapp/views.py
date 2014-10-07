from django.conf.urls import patterns, url
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from myapp.models import Film, Cinema, Session

def startpage(request):
    return render(request,'index.html',[])

def films(request):
    film_list = Film.objects.order_by('name')
    context = {'film_list':film_list}
    return render(request, 'films/index.html', context)
    
def cinemas(request):
    cinema_list = Cinema.objects.order_by('name')
    context = {'cinema_list':cinema_list}
    return render(request, 'cinemas/index.html', context)
    
def sessions(request):
    session_list = Session.objects.order_by('start')
    context = {'session_list':session_list}
    return render(request, 'sessions/index.html', context)
    
def film(request, film_id):
    film =  get_object_or_404(Film, pk=film_id)
    return render(request, 'films/film.html', {'film': film})    
        
def cinema(request, cinema_id):
    cinema =  get_object_or_404(Cinema, pk=cinema_id)
    return render(request, 'cinemas/cinema.html', {'cinema': cinema})  
    
def session(request, session_id):
    session =  get_object_or_404(Session, pk=session_id)
    return render(request, 'sessions/session.html' , {'session': session})

def searchFilm(request):
    return render_to_response('films/search.html')
    
def searchCinema(request):
    return render_to_response('cinemas/search.html')
    
def searchSession(request):
    return render_to_response('sessions/search.html')
    
def searchFilmRes(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        film_list = Film.objects.filter(name__icontains=q)
        return render_to_response('films/search_res.html',
            {'film_list': film_list, 'query': q})
    else:
        return HttpResponse('')  
        
def searchCinemaRes(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        cinema_list = Cinema.objects.filter(name__icontains=q)
        return render_to_response('cinemas/search_res.html',
            {'cinema_list': cinema_list, 'query': q})
    else:
        return HttpResponse('')
        
def searchSessionRes(request):
    if 'q1' in request.GET and request.GET['q1']:
        if 'q2' in request.GET and request.GET['q2']:
            q1 = request.GET['q1']
            q2 = request.GET['q2']
            session_list = Session.objects.filter(start__gte=q1)
            session_lisr = session_list.filter(end__gte=q2)
            return render_to_response('sessions/search_res.html',
                {'session_list': session_list, 'query1': q1, 'query2':q2 })
    else:
        return HttpResponse('')
        
