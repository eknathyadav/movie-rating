from email import contentmanager
from multiprocessing import context
from django.shortcuts import redirect, render
# Create your views here.
from .models import User, Director, Actor, Genre, Review, Writer, Movie
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django. db. models import Q


def home(request):
    q = request.GET.get('q') if request.GET.get('q') else " "
    movies = Movie.objects.filter(Q(director__name__icontains=q) |
                                  Q(name__icontains=q))
    context = {
        'movies': movies
    }
    return render(request, 'base/home.html', context)


def getMovie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    context = {
        "movie": movie
    }
    return render(request, 'base/movie_page.html', context)


def userReviews(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    reviews = movie.review_set.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'base/review_page.html', context)


def loginUser(request):
    page = 'login'
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.get(username=username)
        if user is None:
            messages.add_message(
                request, messages.INFO, 'Username or password is not correct')
        else:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # creates session
                return redirect('base:home')
            else:
                messages.add_message(
                    request,  'Username or password is not correct')
    return render(request, 'base/login_register.html', {'page': page})


def registerUser(request):
    page = "register"
    if request.method == "POST":
        try:
            if User.objects.get(username=request.POST["username"]):
                messages.add_message(
                    request, messages.INFO, 'Username already exist')
        except:
            user = User.objects.create(
                username=request.POST["username"],
                password=request.POST["password"]
            )
            login(request, user)
            return redirect('base:home')
    return render(request, 'base/login_register.html', {'page': page})


def logoutUser(request):
    logout(request)
    return redirect('base:home')


def reviewSubmission(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    context = {
        "movie": movie
    }
    if request.method == "POST":
        print("called")
        Review.objects.create(
            movie=movie,
            user=request.user,
            rating=request.POST["rate"],
            review=request.POST["review"]
        )
        numberOfRatings = len(movie.review_set.all())-1
        movie.movie_rating = round(((movie.movie_rating *
                                     (numberOfRatings))+int(request.POST["rate"]))/(numberOfRatings+1), 1)
        movie.save()

        return redirect("base:userReviews", movie_id)
    return render(request, 'base/review_form.html', context)
