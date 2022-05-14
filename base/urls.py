from django.urls import path
from . import views
app_name = 'base'
urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('', views.home, name="home"),
    path('movie/<int:movie_id>/', views.getMovie, name="getMovie"),
    path('<int:movie_id>/review/', views.userReviews, name="userReviews"),
    path('<int:movie_id>/user-review/',
         views.reviewSubmission, name="user-review"),
    path('watch-list/', views.getWatchList, name="watch-list"),
    path("<int:item_id>/delete-item-watchlist",
         views.removeItemWatchList, name="delete-watch-list-item")

]
