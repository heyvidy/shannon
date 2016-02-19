from django.http import *
from django.shortcuts import render, get_object_or_404, redirect,render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from models import Profile, Post, Notice, Document, Activity
from forms import DocumentForm
from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFill
import datetime
from django.utils import timezone

def index(request):
    user = request.user
    return render(request,'network/index.html', {'user': user})



def login_view(request):
    user = request.user
    if not user.is_authenticated():
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_authenticated():
                    print "User is_authenticated"
                    login(request, user)
                    return redirect("/")
            else:
                return HttpResponse("Your Login Credentials are incorrect.")
    else:
        return redirect("/")
    return  render(request,'network/login.html', {})




def signup(request):
    return render(request, 'network/signup.html', {})




def profile(request, user_id):
    user = request.user
    post_list = Post.objects.filter(author=user_id).order_by('-post_time')
    list = Profile.objects.get(profile_owner= user_id)
    dp = list.image.thumbnail
    dp_str = str(dp)[7:]
    return render(request, 'network/profile.html', {"posts": post_list, 'profile': list, "profile_pic": dp_str, "user_id" : user_id, "user":user})




def edit_profile(request):
    return HttpResponse("Edit Profile Page")




def delete_post(request, post_id):
    post = Post.objects.get(pk = post_id)
    if post.author == request.user:
        post.delete()
    return redirect('/home')




def home(request):
    user = request.user
    if user.is_authenticated():
        if request.method == "POST":
            post = Post()
            post.post_title = request.POST['title']
            post.post_body = request.POST['body']
            post.post_time = timezone.now()
            post.author = request.user
            post.save()
            return redirect('/home')

        user_id     = user.id
        post_list = Post.objects.all().order_by('-post_time')
        list = Profile.objects.get(profile_owner= user_id).image.thumbnail
        list_str = str(list)[7:]
        activity = Activity.objects.all().order_by('-activity_date')
        notice = Notice.objects.all()
    return render(request, 'network/home.html', {"posts": post_list, 'user': user, "profile" : list_str, "activities": activity, "notices":notice})




def logout_view(request):
    logout(request)
    return render(request,'network/login.html', {})




def upload_file(request):
    documents = Document.objects.all()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(name = request.POST['name'], label = request.POST['label'], docfile = request.FILES['docfile'])
            newdoc.save()
            return redirect('/docs')
    else:
        form = DocumentForm()

    documents = Document.objects.all()
    return render(request, 'network/docs.html', {'documents': documents, 'form': form})






