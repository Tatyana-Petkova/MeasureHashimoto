from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_user, name='login_user'),
    path('register/', views.register, name='register'),
    path('profile_page/<str:pk>/', views.profile_page, name='profile_page'),
    path('logout/', views.logout_user, name='logout'),

]
