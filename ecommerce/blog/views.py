from django.shortcuts import render,redirect
from .models import Post,Commet
from django.shortcuts import get_object_or_404
from .models import *
from .forms import *
from django.views.generic.detail import DetailView
def index(request):
    post = Post.objects.all()
    context = {
        'post': post
    }
    return render(request, 'index.html',context)


def commet(request,id):
    commet = Commet.objects.get(id=id)
    context = {
        'commet': commet
    }
    return render(request, 'index.html',context)


def delete(request, id):
    
   
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect("index")

def commet_detail(request,id):
    commet_detail = Post.objects.get(id=id)
    context = {
        'commet_detail': commet_detail
    }
    return render(request, 'commet_detail.html',context)

def create(request):
    form = IndexForm()
    if request.method == 'POST':
        form = IndexForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    context = {
        'form' : form
    }
    return render (request,'create.html',context)


def update(request,id):
    index = Post.objects.get(id=id)
    form = IndexForm(instance=index)
    if request.method == 'POST':
        form = IndexForm(request.POST,instance=index)
        if form.is_valid():
            form.save()
        return redirect('index')
    context = {
        'form' : form
    }
    return render (request,'create.html',context)



