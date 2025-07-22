from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.my_profile_redirect, name='my_profile'),
    path('profile/<str:username>/', views.profile_view, name='profile_view'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('recommended/', views.recommended_places, name='recommended_places'),
    path('add-place/', views.add_place, name='add_place'),
]
