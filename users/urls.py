from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('sign_in/',views.SignIn.as_view(),name='sign_in'),
    path('sign_up/',views.SignUp.as_view(),name='sign_up'),
]