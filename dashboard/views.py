# dashboard/views.py
import json
import random
import base64
from django.shortcuts import render, redirect

# Import our custom architecture
from . import data
from . import services

# ── Home ──────────────────────────────────────────────────────────────────────
def home_view(request):
    return render(request, 'dashboard/home.html')

# ── Schedule ──────────────────────────────────────────────────────────────────
def schedule_view(request):
    try:
        year = int(request.GET.get('year', data.CURRENT_YEAR))
    except ValueError:
        year = data.CURRENT_YEAR

    events, error_message = services.get_schedule_events(year)

    return render(request, 'dashboard/schedule.html', {
        'events': events, 
        'year': year,
        'available_years': data.AVAILABLE_YEARS,
        'error_message': error_message,
    })

# ── Standings ─────────────────────────────────────────────────────────────────
def standings_view(request):
    try:
        year = int(request.GET.get('year', data.CURRENT_YEAR))
    except ValueError:
        year = data.CURRENT_YEAR

    drivers, constructors, error_message = services.fetch_standings(year)
    
    return render(request, 'dashboard/standings.html', {
        'drivers': drivers, 
        'constructors': constructors,
        'year': year, 
        'available_years': data.AVAILABLE_YEARS,
        'error_message': error_message,
    })

# ── Results ───────────────────────────────────────────────────────────────────
def results_view(request):
    try:
        year = int(request.GET.get('year', data.CURRENT_YEAR))
    except ValueError:
        year = data.CURRENT_YEAR

    race_results, quali_results, event_name, error = services.fetch_latest_results(year)

    return render(request, 'dashboard/results.html', {
        'race_results': race_results, 
        'quali_results': quali_results,
        'event_name': event_name, 
        'year': year,
        'available_years': data.AVAILABLE_YEARS,
        'error_message': error,
    })

# ── Lap Comparison ────────────────────────────────────────────────────────────
def compare_view(request):
    try:
        year = int(request.GET.get('year', data.CURRENT_YEAR))
    except ValueError:
        year = data.CURRENT_YEAR

    round_num = request.GET.get('round')
    driver1 = request.GET.get('driver1', '').strip().upper()
    driver2 = request.GET.get('driver2', '').strip().upper()

    race_options = services.get_completed_races_list(year)
    driver_options = sorted([{'code': d['code'], 'name': d['name']} for d in data.DRIVERS_2026], key=lambda x: x['name'])
    
    chart_data, error_message = services.fetch_lap_comparison(year, round_num, driver1, driver2)

    return render(request, 'dashboard/compare.html', {
        'race_options': race_options, 
        'driver_options': driver_options,
        'chart_data': chart_data,
        'selected_round': round_num, 
        'driver1': driver1, 
        'driver2': driver2,
        'year': year, 
        'available_years': data.AVAILABLE_YEARS,
        'error_message': error_message,
    })

# ── Circuit detail ────────────────────────────────────────────────────────────
def circuit_detail_view(request, location):
    info = data.CIRCUITS.get(location, {
        'wiki': location.replace(' ', '_'), 'country': '—', 'city': location,
        'length_km': '—', 'turns': '—', 'lap_record': '—', 'first_gp': '—',
        'desc': 'Detailed information for this circuit is not yet available.',
    })
    return render(request, 'dashboard/circuit_detail.html', {
        'location': location, 
        'info': info,
        'wiki_url': f"https://en.wikipedia.org/wiki/{info['wiki']}",
    })

# ── Drivers ───────────────────────────────────────────────────────────────────
def drivers_view(request):
    team_filter = request.GET.get('team', '')
    teams = sorted(set(d['team'] for d in data.DRIVERS_2026))
    drivers = [d for d in data.DRIVERS_2026 if not team_filter or d['team'] == team_filter]
    
    return render(request, 'dashboard/drivers.html', {
        'drivers': drivers, 
        'teams': teams, 
        'selected_team': team_filter,
    })

def driver_detail_view(request, code):
    driver = data.DRIVER_MAP.get(code.upper())
    if not driver:
        return redirect('drivers')
    
    return render(request, 'dashboard/driver_detail.html', {
        'driver': driver,
        'wiki_url': f"https://en.wikipedia.org/wiki/{driver['wiki']}",
    })

# ── Constructors ──────────────────────────────────────────────────────────────
def constructors_view(request):
    return render(request, 'dashboard/constructors.html', {
        'constructors': data.CONSTRUCTORS_2026
    })

# ── History & Legends ─────────────────────────────────────────────────────────
def history_view(request):
    return render(request, 'dashboard/history.html', {
        'legends': data.LEGENDS, 
        'eras': data.HISTORY_ERAS, 
        'glossary': data.GLOSSARY,
    })

# ── Quiz ──────────────────────────────────────────────────────────────────────
def quiz_view(request):
    questions = random.sample(data.QUIZ_QUESTIONS, min(5, len(data.QUIZ_QUESTIONS)))
    answer_map = {q['q']: q['answer'] for q in questions}
    encoded = base64.b64encode(json.dumps(answer_map).encode()).decode()
    
    return render(request, 'dashboard/quiz.html', {
        'questions': questions, 
        'encoded_answers': encoded,
    })

def quiz_check_view(request):
    if request.method != 'POST':
        return redirect('quiz')
        
    try:
        answer_map = json.loads(base64.b64decode(request.POST.get('encoded_answers', '').encode()).decode())
    except Exception:
        return redirect('quiz')

    fact_map = {q['q']: q['fact'] for q in data.QUIZ_QUESTIONS}
    score, results = 0, []
    
    for q_text, correct_answer in answer_map.items():
        user_answer = request.POST.get(q_text, '')
        correct = user_answer == correct_answer
        if correct:
            score += 1
        results.append({
            'question': q_text, 
            'user_answer': user_answer or '(no answer)',
            'correct_answer': correct_answer, 
            'correct': correct,
            'fact': fact_map.get(q_text, ''),
        })

    return render(request, 'dashboard/quiz_results.html', {
        'score': score, 
        'total': len(results), 
        'results': results,
    })