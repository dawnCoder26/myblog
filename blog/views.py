from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from .forms import EnquiryForm

# Create your views here.
def index(request):
    posts = Post.objects.all()[:10]
    user = User.objects.get(id=1)
    context = {
        'posts' : posts,
        'user'  : user
    }
    return render(request,'blog/index.html', context)

def about(request):
    return render(request,'blog/about.html')



def details(request,id):
    post = Post.objects.get(id=id)
    user = User.objects.get(id=1)
    context = {
        'post': post,
        'user': user
    }
    return render(request,'blog/details.html', context)

def contact(request):
    enquiryform = EnquiryForm(request.POST or None)
    if enquiryform.is_valid():
        enquiryform.save()
    context = {
        'enquiryform': enquiryform
    }
    return render(request,'blog/contact.html',context)

    