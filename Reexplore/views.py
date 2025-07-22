from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import UserProfile, PlaceRecommendation
from .forms import UserProfileForm, SignUpForm, PlaceForm

def home_view(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('profile_view', username=user.username)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile_view', username=user.username)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile, created = UserProfile.objects.get_or_create(user=user)
    return render(request, 'profile.html', {'profile_user': user, 'profile': profile})

@login_required
def edit_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view', username=request.user.username)
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def my_profile_redirect(request):
    return redirect('profile_view', username=request.user.username)

@login_required
def recommended_places(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    places = PlaceRecommendation.objects.all()

    if profile.location:
        places = places.filter(location__icontains=profile.location)

    category = request.GET.get('category')
    if category:
        places = places.filter(category=category)

    return render(request, 'recommended_places.html', {
        'places': places,
        'location': profile.location,
        'categories': dict(PlaceRecommendation._meta.get_field('category').choices)
    })

@login_required
def add_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES)
        if form.is_valid():
            place = form.save(commit=False)
            place.added_by = request.user
            place.save()
            return redirect('recommended_places')
    else:
        form = PlaceForm()
    return render(request, 'add_place.html', {'form': form})
