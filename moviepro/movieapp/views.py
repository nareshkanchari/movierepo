from django.shortcuts import render,redirect
from .models import Telugu_Movies,Book_Movie_Data,Hindi_Movies,English_Movies
from .forms import Book_Movie
from django.http.response import HttpResponse
def home(request):
    return render(request,'movie_home.html')
def telugu_movies(request):
    if request.method=='POST':
        return redirect('/book/')
    else:
        tdata=Telugu_Movies.objects.all()
        return render(request,'teludu_movie.html',{'tdata':tdata})


def hindi_movies(request):
    if request.method=='POST':
        return redirect('/book/')
    else:
        hdata=Hindi_Movies.objects.all()
        return render(request,'hindi_movies.html',{'hdata':hdata})

def english_movies(request):
    if request.method=='POST':
        return  redirect('/book/')
    else:
        edata=English_Movies.objects.all()
        return render(request,'english_movies.html',{'edata':edata})

def book_movie(request):
    if request.method=='POST':
        bform=Book_Movie(request.POST)
        if bform.is_valid():
            movie_name=request.POST.get('movie_name','')
            theater_name=request.POST.get('theater_name','')
            show_time=request.POST.get('show_time','')
            select_seats=request.POST.get('select_seats','')
            select_date=request.POST.get('select_date','')

            data=Book_Movie_Data(
                movie_name=movie_name,
                theater_name=theater_name,
                show_time=show_time,
                select_seats=select_seats,
                select_date=select_date
            )
            data.save()
            x="<h1>you have successfull booked {} in {}  {}  Show</h1>".format(movie_name,theater_name,show_time)
            return HttpResponse(x)

    else:
        bform=Book_Movie()
        return render(request,'book_movie.html',{'bform':bform})


