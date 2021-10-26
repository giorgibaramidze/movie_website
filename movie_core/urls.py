from django.urls import path
from movie_core import views
from . views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('movies/<int:id>', views.MovieDetailView, name='movie_details'),
    path('actors/', ActorsListView.as_view(), name='actors'),
    path('actors/<int:id>', views.actors_movies, name='actors_movies'),
    path('movies/', views.MovieListView, name='movies'),
    path('search/', views.search, name='search'),
    # path('?', views.search_results, name='search')
    path('filter-data/', views.filter_data, name='filter_data'),
    path('login', views.loginPage, name='login'),
    path('register', views.registerPage, name='register'),
    path('logout', views.logoutUser, name='logout'),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate_account, name='activate'),
    path('profile/watch_later', views.watch_later, name='watch_later'),
    path('profile/favorites', views.favorites, name='favorites'),
    path('profile/rated', views.rated, name='rated'),
    path('favourite_movie/', views.favourite_movie, name='favourite_movie'),
    path('watch_later_movie/', views.watch_later_movie, name='watch_later_movie'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='core/accounts/password_reset.html'), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='core/accounts/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='core/accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='core/accounts/password_reset_complete.html'), name='password_reset_complete'),
    ]