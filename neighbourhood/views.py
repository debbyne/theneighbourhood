from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UpdateUserProfileForm, newHoodForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from .models import Post,Neighbourhood,Profile,Business 
from pickle import FALSE
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist


from . import models
# Create your views here.
def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'django_registration/registration_form.html', {'form': form})

def loginrequest(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "register/login.html", {"loginform": form})

@login_required(login_url='/accounts/login')
def index(request):
    posts = Neighbourhood.objects.all()
    return render(request, 'index.html',{'posts':posts})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    posts = models.Post.objects.filter(hood=current_user.neighborhood)
    profileForm = UpdateUserProfileForm()
    if request.method == 'POST':
        profileForm = UpdateUserProfileForm(request.POST, request.FILES)
        if profileForm.is_valid():
            profile=profileForm.save(commit=FALSE)
            profile.save()
        else:
            profileForm = UpdateUserProfileForm()
    return render(request,'profile.html',{'current_user':current_user,'post':posts,'profileForm':profileForm})

def logoutUser(request):
 logout(request)
 return redirect(index)

@login_required(login_url='/accounts/login')
def search_results(request):

    if 'search_username' in request.GET and request.GET["search_username"]:
        search_term = request.GET.get("search_username")
        searched_username = Profile.search_profile(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message, 'profile':searched_username})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def hood(request):
    try:
            hoods = Neighbourhood.objects.all()
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, 'hood.html', {'hoods':hoods,})

def hooddetails(request):
    try:
            hoods = Neighbourhood.objects.all()
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, 'hooddets.html', {'hoods':hoods,})