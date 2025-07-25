from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, PlaceRecommendation

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image', 'location', 'latitude', 'longitude']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class PlaceForm(forms.ModelForm):
    class Meta:
        model = PlaceRecommendation
        fields = ['name', 'description', 'location', 'category', 'image', 'latitude', 'longitude']
