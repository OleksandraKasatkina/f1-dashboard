from .models import UserProfile
from . import data

def f1_theme_processor(request):
    """
    Globally injects a comprehensive theme dictionary (primary, secondary, text, and background).
    """
    # Default Classic F1 Theme Settings
    theme = {
        'primary': '#e10600',
        'secondary': '#c40500',
        'text': '#ffffff',
        'bg_gradient': 'linear-gradient(135deg, #0f0f14 0%, #15151e 100%)'
    }
    
    if request.user.is_authenticated:
        try:
            profile = request.user.profile
            if profile.use_team_theme and profile.favorite_team:
                team_data = next((t for t in data.CONSTRUCTORS_2026 if t['name'] == profile.favorite_team), None)
                if team_data:
                    theme['primary'] = team_data['color']
                    theme['secondary'] = team_data['color2']
                    theme['text'] = team_data['text_color']
                    
                    # Create a subtle glowing background gradient using 15% opacity (hex '15') of the primary color
                    tint = team_data['color'] + "15" 
                    theme['bg_gradient'] = f"linear-gradient(135deg, #0f0f14 0%, {tint} 100%)"
        except UserProfile.DoesNotExist:
            pass
            
    return {'theme': theme}