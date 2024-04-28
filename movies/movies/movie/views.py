from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect,reverse
from .models import *
# Create your views here.
from .forms import *
from director.models import  Director
from django.shortcuts import render, reverse, get_object_or_404
from .models import Movie

def movie_list(request):
    context={}
    movies=Movie.objects.all()
    context['movies']=movies
    # return HttpResponse('<h1>Hello movie_list 9month</h1>')
    return render(request,'movie/list_movies.html',context)
def add_movie(request):
    context={'form':NewMovieForm}
    if(request.method=='POST'):
        if(len(request.POST)>0 and request.POST['movie_name']!=None and request.POST['part']!=None ):

            Movie.objects.create(movie_name=request.POST['movie_name'],part=request.POST['part'],director=Director.getDirector(request.POST['director']),movie_image=request.FILES['movie_image'])
        else:
            context['message']="please enter movie data"
    return render(request,'movie/add_movie.html',context)
    # return HttpResponseRedirect(reverse('movie_list'))


def update_movie(request, id):
    movie = get_object_or_404(Movie, id=id)  # Get the movie object or raise a 404 error if not found

    if request.method == 'POST':
        form = NewMovieFormModel(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('movie_list'))
    else:
        form = NewMovieFormModel(instance=movie)

    context = {
        'form': form,
        'msg': ''  # Placeholder for error message
    }
    return render(request, 'movie/update_movie.html', context)
def delete_movie(request,id):
    Movie.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('movie_list'))

def display_movie(request,id):
    movie = Movie.objects.get(id=id)
    context = {'movie': movie}
    return render(request,'movie/single_movie.html',context)
