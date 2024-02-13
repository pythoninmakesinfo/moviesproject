from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import MovieForm
from. models import movies
# Create your views here.
def index(request):
    moviess=movies.objects.all()
    context={'movies_list':moviess
            }

    return render(request,'index.html',context)
def detail(request,movie_id):
    moviess = movies.objects.get(id=movie_id)
    return render(request,"detail.html", {'movies': moviess})
    return HttpResponse("this is movies no %s"% movie_id)
def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc= request.POST.get('desc',)
        year = request.POST.get('year',)
        img =request.FILES["img"]
        movie=movies(name=name,desc=desc,year=year,img=img)
        movie.save()

    return render(request, "add.html")

def update(request,id):
    movie=movies.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movies})
def delete(request,id):
    if request.method=='POST':

       movie=movies.objects.get(id=id)
       movie.delete()
       return redirect('/')
    return render(request,'delete.html')