from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # Link each profile to exactly one User account
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    favorite_team = models.CharField(max_length=100, blank=True, default='')
    favorite_driver = models.CharField(max_length=10, blank=True, default='')
    use_team_theme = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s F1 Profile"