from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm



# Create your views here.
def index(request):
    if request.method == 'POST':
        form=PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    
    posts= Post.objects.all()[:20]
    return render(request,'post.html',{'posts':posts})


def edit(request, post_id):
    post = Post.objects.get(id = post_id)
    if request.method == 'POST':
        form=PostForm(request.POST, request.FILES, instance = post )

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    
    posts= Post.objects.all()[:20]
    return render(request,'edit.html',{'post':post})



def delete(request, post_id):
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect("/")



def like_count(request, post_id):
    post = Post.objects.get(id= post_id)
    post.like +=1
    post.save()
    return HttpResponseRedirect('/')