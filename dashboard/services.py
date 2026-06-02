import os
import json
import fastf1
import requests
from datetime import date

# Configure FastF1 cache
if not os.path.exists('cache'):
    os.makedirs('cache')
fastf1.Cache.enable_cache('cache')

def get_schedule_events(year):
    """Fetches the schedule and formats it into a list of dictionaries."""
    events = []
    error_message = None
    try:
        schedule = fastf1.get_event_schedule(year)
        races = schedule[schedule['EventFormat'] != 'testing']
        for _, row in races.iterrows():
            events.append({
                'round': row['RoundNumber'],
                'event_name': row['EventName'],
                'country': row['Country'],
                'location': row['Location'],
                'date': row['EventDate'].date(),
            })
    except Exception:
        error_message = f"Schedule for {year} could not be loaded."
    return events, error_message

def fetch_standings(year):
    """Pulls standings from the Jolpica REST API."""
    base = "https://api.jolpi.ca/ergast/f1"
    drivers, constructors, error = [], [], None

    try:
        r = requests.get(f"{base}/{year}/driverStandings.json", timeout=8)
        r.raise_for_status()
        lists = r.json()['MRData']['StandingsTable']['StandingsLists']
        if lists:
            for e in lists[0]['DriverStandings']:
                drivers.append({
                    'position': int(e['position']),
                    'driver': f"{e['Driver']['givenName']} {e['Driver']['familyName']}",
                    'nationality': e['Driver']['nationality'],
                    'team': e['Constructors'][0]['name'] if e['Constructors'] else '—',
                    'points': float(e['points']),
                    'wins': int(e['wins']),
                })
    except Exception as exc:
        error = f"Driver standings could not be loaded: {exc}"

    try:
        r = requests.get(f"{base}/{year}/constructorStandings.json", timeout=8)
        r.raise_for_status()
        lists = r.json()['MRData']['StandingsTable']['StandingsLists']
        if lists:
            for e in lists[0]['ConstructorStandings']:
                constructors.append({
                    'position': int(e['position']),
                    'team': e['Constructor']['name'],
                    'nationality': e['Constructor']['nationality'],
                    'points': float(e['points']),
                    'wins': int(e['wins']),
                })
    except Exception as exc:
        error = (error or '') + f" Constructor standings could not be loaded: {exc}"

    return drivers, constructors, error

def fetch_latest_results(year):
    """Finds the most recent race and fetches its race and qualifying results."""
    race_results, quali_results = [], []
    event_name, error_message = None, None

    try:
        schedule = fastf1.get_event_schedule(year)
        races = schedule[schedule['EventFormat'] != 'testing']
        past = [r for _, r in races.iterrows() if r['EventDate'].date() <= date.today()]
        
        if not past:
            return [], [], None, "No completed races yet this season."
            
        latest = past[-1]
        event_name = latest['EventName']
        round_num = int(latest['RoundNumber'])

        race_session = fastf1.get_session(year, round_num, 'R')
        race_session.load(laps=False, telemetry=False, weather=False, messages=False)
        for _, row in race_session.results.iterrows():
            race_results.append({
                'position': row.get('Position', '—'),
                'driver': row.get('FullName', '—'),
                'team': row.get('TeamName', '—'),
                'points': row.get('Points', 0),
                'status': row.get('Status', '—'),
            })

        try:
            q = fastf1.get_session(year, round_num, 'Q')
            q.load(laps=False, telemetry=False, weather=False, messages=False)
            for _, row in q.results.iterrows():
                quali_results.append({
                    'position': row.get('Position', '—'),
                    'driver': row.get('FullName', '—'),
                    'team': row.get('TeamName', '—'),
                    'q1': str(row.get('Q1', '—')),
                    'q2': str(row.get('Q2', '—')),
                    'q3': str(row.get('Q3', '—')),
                })
        except Exception:
            pass
    except Exception as exc:
        error_message = f"Results could not be loaded: {exc}"

    return race_results, quali_results, event_name, error_message

def get_completed_races_list(year):
    """Returns a list of completed races for dropdown menus."""
    race_options = []
    try:
        schedule = fastf1.get_event_schedule(year)
        races = schedule[schedule['EventFormat'] != 'testing']
        for _, row in races.iterrows():
            if row['EventDate'].date() <= date.today():
                race_options.append({'round': int(row['RoundNumber']), 'name': row['EventName']})
    except Exception:
        pass
    return race_options

def fetch_lap_comparison(year, round_num, driver1, driver2):
    """Fetches and formats telemetry data for the Chart.js frontend."""
    if not (round_num and driver1 and driver2):
        return None, None
        
    try:
        session = fastf1.get_session(year, int(round_num), 'R')
        session.load(telemetry=False, weather=False, messages=False)

        def get_laps(code):
            laps = session.laps.pick_driver(code).pick_quicklaps()
            return {
                'label': code,
                'data': [
                    {'x': int(r['LapNumber']), 'y': round(r['LapTime'].total_seconds(), 3)}
                    for _, r in laps.iterrows() if hasattr(r['LapTime'], 'total_seconds')
                ],
            }

        d1, d2 = get_laps(driver1), get_laps(driver2)
        if not d1['data'] and not d2['data']:
            return None, "No lap data found. Ensure the selected drivers participated in this race."
            
        return json.dumps([d1, d2]), None
    except Exception as exc:
        return None, f"Could not load lap data: {exc}"

def get_next_race():
    """Finds the next upcoming race for the countdown timer."""
    try:
        year = date.today().year
        schedule = fastf1.get_event_schedule(year)
        races = schedule[schedule['EventFormat'] != 'testing']
        
        for _, row in races.iterrows():
            # Check if the race date is today or in the future
            if row['EventDate'].date() >= date.today():
                return {
                    'name': row['EventName'],
                    'round': row['RoundNumber'],
                    'location': row['Location'],
                    'timestamp': row['EventDate'].isoformat() # Convert for JS parsing
                }
    except Exception:
        pass
    return None