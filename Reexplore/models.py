from django.contrib.auth.models import User
from django.db import models

# Categories for place types
CATEGORY_CHOICES = [
    ('nature', 'Nature'),
    ('historical', 'Historical'),
    ('food', 'Food'),
    ('shopping', 'Shopping'),
    ('entertainment', 'Entertainment'),
]

# User profile with location info
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', default='profile_images/default.jpg')
    location = models.CharField(max_length=100, blank=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.user.username

# Places users can recommend
class PlaceRecommendation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='places/', blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
