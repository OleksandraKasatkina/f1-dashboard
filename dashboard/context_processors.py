from .models import UserProfile
from . import data

def f1_theme_processor(request):
    """
    Globally injects a comprehensive theme dictionary (primary, secondary, text, background, watermark, quote).
    """
    theme = {
        'primary': '#e10600',
        'secondary': '#c40500',
        'text': '#ffffff',
        'bg_gradient': 'linear-gradient(135deg, #0f0f14 0%, #15151e 100%)',
        'watermark': '',
        'quote': ''
    }
    
    if request.user.is_authenticated:
        try:
            profile = request.user.profile
            mode = profile.theme_mode
            
            # Extract driver specific data
            if profile.favorite_driver:
                driver_data = data.DRIVER_MAP.get(profile.favorite_driver)
                if driver_data:
                    theme['quote'] = driver_data.get('quote', '')
                    if profile.show_watermark:
                        theme['watermark'] = str(driver_data['number'])

            # Apply Theme Mode Logic
            if mode == 'team' and profile.favorite_team:
                team_data = next((t for t in data.CONSTRUCTORS_2026 if t['name'] == profile.favorite_team), None)
                if team_data:
                    theme['primary'] = team_data.get('color', theme['primary'])
                    theme['secondary'] = team_data.get('color2', theme['secondary'])
                    theme['text'] = team_data.get('text_color', theme['text'])
                    
            elif mode == 'driver' and profile.favorite_driver:
                driver_data = data.DRIVER_MAP.get(profile.favorite_driver)
                if driver_data:
                    theme['primary'] = driver_data.get('accent', '#e10600')
                    team_data = next((t for t in data.CONSTRUCTORS_2026 if t['name'] == driver_data.get('team')), None)
                    theme['secondary'] = team_data['color'] if team_data else '#ffffff'
                    theme['text'] = '#000000' if theme['primary'] in ['#E3F700', '#FFFFFF', '#27F4D2'] else '#ffffff'
                    
            elif mode == 'custom':
                theme['primary'] = profile.custom_primary
                theme['secondary'] = profile.custom_secondary
                theme['text'] = profile.custom_text
            
            # Generate the subtle glowing background
            if theme['primary'].startswith('#') and len(theme['primary']) == 7:
                tint = theme['primary'] + "15" 
            else:
                tint = "#e1060015"
                
            theme['bg_gradient'] = f"linear-gradient(135deg, #0f0f14 0%, {tint} 100%)"

        except UserProfile.DoesNotExist:
            pass
            
    return {'theme': theme}