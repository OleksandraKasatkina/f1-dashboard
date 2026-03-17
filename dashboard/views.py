from django.shortcuts import render
import fastf1
import os

if not os.path.exists('cache'):
    os.makedirs('cache')
fastf1.Cache.enable_cache('cache')

def schedule_view(request):
    # Get the year from the URL query parameter (e.g., /?year=2023)
    # Default to 2026 if not provided
    try:
        year = int(request.GET.get('year', 2026))
    except ValueError:
        year = 2026 # Fallback to 2026 if the input is not a valid integer

    # FastF1 works best with seasons from 2018 onwards
    # Create a list of years for our dropdown menu
    available_years = list(range(2018, 2027)) 
    
    events = []
    error_message = None

    try:
        schedule = fastf1.get_event_schedule(year)
        races = schedule[schedule['EventFormat'] != 'testing']
        
        for index, row in races.iterrows():
            events.append({
                'round': row['RoundNumber'],
                'event_name': row['EventName'],
                'country': row['Country'],
                'location': row['Location'],
                'date': row['EventDate'].date()
            })
    except Exception as e:
        error_message = f"Unfortunately, the schedule for {year} could not be loaded."

    context = {
        'events': events,
        'year': year,
        'available_years': available_years,
        'error_message': error_message
    }
    return render(request, 'dashboard/schedule.html', context)