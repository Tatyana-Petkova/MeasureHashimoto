from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_user, name='login_user'),
    path('register/', views.register, name='register'),
    path('profile_page/<str:pk>/', views.profile_page, name='profile_page'),
    path('add_results/', views.add_results, name='add_results'),
    path('edit_results/<str:pk>/', views.edit_results, name='edit_results'),
    path('delete_results/<str:pk>/', views.delete_results, name='delete_results'),
    path('logout/', views.logout_user, name='logout'),

]
