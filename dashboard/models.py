from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    THEME_CHOICES = [
        ('classic', 'Classic F1 (Red)'),
        ('team', 'Favorite Team Colors'),
        ('driver', 'Favorite Driver Accent'),
        ('custom', 'Custom Personal Theme'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    favorite_team = models.CharField(max_length=100, blank=True, default='')
    favorite_driver = models.CharField(max_length=10, blank=True, default='')
    
    # Advanced Theme Engine Fields
    theme_mode = models.CharField(max_length=20, choices=THEME_CHOICES, default='classic')
    custom_primary = models.CharField(max_length=7, default='#e10600')
    custom_secondary = models.CharField(max_length=7, default='#c40500')
    custom_text = models.CharField(max_length=7, default='#ffffff')
    
    # Feature Toggles
    show_watermark = models.BooleanField(default=True)
    use_team_theme = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s F1 Profile"