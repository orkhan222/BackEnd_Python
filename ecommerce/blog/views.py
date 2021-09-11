from django.shortcuts import render,redirect
from .models import Post,Commet
from django.shortcuts import get_object_or_404


def index(request):
    post = Post.objects.all()
    context = {
        'post': post
    }
    return render(request, 'index.html',context)


def post_detail(request,id):
    commet = Commet.objects.get(id=id)
    context = {
        'commet': commet
    }
    return render(request, 'post_detail.html',context)


def delete(request, id):
    
   
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect("index")