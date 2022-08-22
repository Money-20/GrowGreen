from django.urls import path
from . import views

urlpatterns = [
    #path('', views.landing, name='home'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
   # path('home/', views.home, name="home"),
    # Dynamic
    path('',views.index, name = "index"),
    path('home/', views.home, name= "home"),
    #path('home/<int:user_id>/', views.home),
    #path('landing/', views.landing, name= "landing"),
    path('about/', views.about, name="about"),
    path('index/',views.index, name= "index"),
    path('bonsai/',views.bonsai, name="bonsai"),
    path('hf/', views.hf, name= "hf"),
    path('trc/', views.tr, name= "tr"),
  #  path('home/', views.homePage, name="home")
]