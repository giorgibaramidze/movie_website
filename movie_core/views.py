from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from . models import *
import json
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from .token_generator import account_activation_token


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                email_subject = 'Activate Your Account'
                message = render_to_string('core/activate_account.html',{
                    'user': user,
                    'domain': current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(email_subject, message, to=[to_email])
                email.send()
                messages.success(request, 'აქტივაციის ლინკი გამოგზავნილია თქვენს ემაილზე ')
                return redirect('login')
            else:
                password1 = form.data['password1']
                password2 = form.data['password2']
                email = form.data['email']
                user = form.data['username']
                for msg in form.errors.as_data():
                    if msg == 'email':
                        messages.error(request, f"ასეთი მაილი უკვე დარეგისტრირებულია")
                    if msg == 'password2' and password1 == password2:
                        messages.error(request, f"გთხოვთ შეიყვანოთ მინიმუმ 8 სიმბოლო")
                    elif msg == 'password2' and password1 != password2:
                        messages.error(request, f"პაროლები ერთმანეთს არ ემთხვევა")
                    elif msg == 'username':
                        messages.error(request, f"სახელი {user} უკვე არსებობს")
        context = {'form': form}
        return render(request, 'core/register.html', context)

def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'თქვენ წარმათებით გაიარეთ რეგისტრაცია')
        return HttpResponse('აქტივაციისთვის '  + '<a href="/login">დააჭირე აქ</a>')
    else:
        return HttpResponse('Activation link is invalid!')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'მომხმარებლის სახელი ან პაროლი არასწორია')
                # return render(request, 'core/login.html', context)

        context = {}
        return render(request, 'core/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def is_valid_queryparam(param):
    return param != '' and param is not None

class Home(TemplateView):
    template_name = "core/main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies_list'] = Movie.objects.filter(type='ფილმი').order_by('-id')[:12]
        context['series_list'] = Movie.objects.filter(type='სერიალი').order_by('-id')[:12]
        context['trailers_list'] = Movie.objects.filter(type='თრეილერი').order_by('-id')[:12]
        context['actors_list'] = Actor.objects.all().order_by('-id')[:25]
        context['directors_list'] = Director.objects.all().order_by('-id')[:18]
        context['rating_list'] = Movie.objects.all().order_by('-imdb')[:12]
        context['popular_list'] = Movie.objects.all().order_by('-views')[:12]

        return context


def MovieDetailView(request, id):
    movies = get_object_or_404(Movie, id=id)
    movies.views += 1
    movies.save()
    is_favourite = False
    is_watch_later = False
    if movies.favourite.filter(id=request.user.id).exists():
        is_favourite = True
    if movies.watch_later.filter(id=request.user.id).exists():
        is_watch_later = True
    similar_movies = movies.tag.similar_objects()[:5]
    context = {
        'movie_details':movies,
        'similar_movies':similar_movies,
        'is_favourite': is_favourite,
        'is_watch_later':is_watch_later,
    }
    return render(request, 'core/movie_details.html', context)


def favourite_movie(request):
    movie = get_object_or_404(Movie, id=request.POST.get('id'))
    is_favourite = False
    if movie.favourite.filter(id=request.user.id).exists():
        movie.favourite.remove(request.user)
        is_favourite = False
    else:
        movie.favourite.add(request.user)
        is_favourite = True
    context = {
        'is_favourite':is_favourite,
        'movie_details':movie
    }
    if request.is_ajax():
        html = render_to_string('core/accounts/add_favourite.html', context, request=request)
        return JsonResponse({'form': html})
    # return HttpResponseRedirect(movie.get_absolute_url())

def watch_later_movie(request):
    movie = get_object_or_404(Movie, id=request.POST.get('id'))
    is_watch_later = False
    if movie.watch_later.filter(id=request.user.id).exists():
        movie.watch_later.remove(request.user)
        is_watch_later = False
    else:
        movie.watch_later.add(request.user)
        is_watch_later = True
    context = {
        'is_watch_later':is_watch_later,
        'movie_details':movie
    }
    if request.is_ajax():
        html = render_to_string('core/accounts/add_watch_later.html', context, request=request)
        return JsonResponse({'watch_later': html})
    # return HttpResponseRedirect(movie.get_absolute_url())

class ActorsListView(ListView):
    template_name = 'core/actors.html'
    model = Actor
    context_object_name = 'all_actors'
    ordering = ['-id']
    paginate_by = 28


def actors_movies(request, id):
    actors = Actor.objects.filter(pk=id)
    movies = Movie.objects.filter(actors__in=list(actors)).order_by('-id')
    context = {
        'actors': actors,
        'movies': movies
    }
    return render(request, 'core/actors_movie.html', context)

def MovieListView(request):

    movie = Movie.objects.filter(type='ფილმი').order_by('-id')
    genre = Genrie.objects.all().order_by('genre')
    voice = Voice.objects.all().order_by('voice')
    country = Countrie.objects.all().order_by('country')
    director = Director.objects.all().order_by('director')
    actor = Actor.objects.all().order_by('actor')
    context={
        'movies': movie,
        'genre':genre,
        'country':country,
        'actor': actor,
        'director':director,
        'voice': voice,
        }

    return render(request, 'core/movies.html', context)

def search(request):
    movie = Movie.objects.all()
    query = request.GET.get('search')
    if query:
        movie = Movie.objects.filter(
            Q(title_eng__icontains=query)
        ).order_by('-id').distinct()
    # genre = Genrie.objects.all().order_by('genre')
    # voice = Voice.objects.all().order_by('voice')
    # country = Countrie.objects.all().order_by('country')
    # director = Director.objects.all().order_by('director')
    # imdb_min_range = request.GET.get('min-range')
    # imdb_max_range = request.GET.get('max-range')
    # genre_query = request.GET.get('genre')
    # country_query = request.GET.get('country')
    # actor_query = request.GET.get('actor')
    # voice_query = request.GET.get('voice')
    # director_query = request.GET.get('director')
    # actor = Actor.objects.all().order_by('actor')

    # if is_valid_queryparam(d):
    #     movie = movie.filter(Q(title_eng__icontains=d)).distinct()
    #
    # if is_valid_queryparam(genre_query):
    #     movie = movie.filter(genries__genre=genre_query)
    # if is_valid_queryparam(voice_query):
    #     movie = movie.filter(voices__voice=voice_query)
    #
    # if is_valid_queryparam(country_query):
    #     movie = movie.filter(countries__country=country_query)
    # if is_valid_queryparam(director_query):
    #     movie = movie.filter(directors__director=director_query)
    # if is_valid_queryparam(actor_query):
    #     movie = movie.filter(actors__actor=actor_query)
    # if is_valid_queryparam(imdb_min_range):
    #     movie = movie.filter(imdb__gte=imdb_min_range)
    # if is_valid_queryparam(imdb_max_range):
    #     movie = movie.filter(imdb__lt=imdb_max_range)

    context = {
        'movies': movie,
        # 'genre':genre,
        # 'country':country,
        # 'actor': actor,
        # 'director':director,
        # 'voice': voice,
    }
    return render(request, "core/search_result.html", context)



def filter_data(request):
    genries = request.GET.getlist('genre[]')
    voices = request.GET.getlist('voice[]')
    countries = request.GET.getlist('country[]')
    directors = request.GET.getlist('director[]')
    actors = request.GET.getlist('actor[]')
    movies = Movie.objects.filter(type='ფილმი').order_by('-id').distinct()
    if len(genries)>0:
        movies = movies.filter(genries__genre__in=genries).distinct()
    elif len(voices)>0:
        movies = movies.filter(voices__voice__in=voices).distinct()
    elif len(countries)>0:
        movies = movies.filter(countries__country__in=countries).distinct()
    elif len(directors)>0:
        movies = movies.filter(directors__director__in=directors).distinct()
    elif len(actors)>0:
        movies = movies.filter(actors__actor__in=actors).distinct()
    data=render_to_string('core/movies_list.html', {'movies':movies})
    return JsonResponse({'data':data})

def watch_later(request):
    user = request.user
    watch_later_movie = user.watch_later.all().order_by('-id')
    context = {
        'watch_later_movie': watch_later_movie,
    }
    return render(request, 'core/accounts/watch_later.html', context)

def favorites(request):
    user = request.user
    favourite_movie = user.favourite.all().order_by('-id')
    context = {
        'favourite_movie': favourite_movie,
    }
    return render(request, 'core/accounts/favorites.html', context)

def rated(request):
    return render(request, 'core/accounts/rated.html')
