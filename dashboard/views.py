from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, CreateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
import json
import random
import base64

from .models import UserProfile
from .forms import CustomRegisterForm, UserProfileForm, UserSettingsForm 
from . import data
from . import services

# ── Main Pages ────────────────────────────────────────────────────────────────
class HomeView(TemplateView):
    template_name = 'dashboard/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject the next race data into the home page for the countdown
        context['next_race'] = services.get_next_race()
        return context


class ScheduleView(TemplateView):
    template_name = 'dashboard/schedule.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            year = int(self.request.GET.get('year', data.CURRENT_YEAR))
        except ValueError:
            year = data.CURRENT_YEAR

        events, error_message = services.get_schedule_events(year)
        context.update({
            'events': events,
            'year': year,
            'available_years': data.AVAILABLE_YEARS,
            'error_message': error_message,
        })
        return context


class StandingsView(TemplateView):
    template_name = 'dashboard/standings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            year = int(self.request.GET.get('year', data.CURRENT_YEAR))
        except ValueError:
            year = data.CURRENT_YEAR

        drivers, constructors, error_message = services.fetch_standings(year)
        context.update({
            'drivers': drivers,
            'constructors': constructors,
            'year': year,
            'available_years': data.AVAILABLE_YEARS,
            'error_message': error_message,
        })
        return context


class ResultsView(TemplateView):
    template_name = 'dashboard/results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            year = int(self.request.GET.get('year', data.CURRENT_YEAR))
        except ValueError:
            year = data.CURRENT_YEAR
            
        round_num = self.request.GET.get('round')
        race_results, quali_results, event_name, error = services.fetch_latest_results(year, round_num)
        race_options = services.get_completed_races_list(year)

        context.update({
            'race_results': race_results,
            'quali_results': quali_results,
            'event_name': event_name,
            'year': year,
            'available_years': data.AVAILABLE_YEARS,
            'race_options': race_options,
            'selected_round': round_num,
            'error_message': error,
        })
        return context


class CompareView(TemplateView):
    template_name = 'dashboard/compare.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            year = int(self.request.GET.get('year', data.CURRENT_YEAR))
        except ValueError:
            year = data.CURRENT_YEAR

        round_num = self.request.GET.get('round')
        driver1 = self.request.GET.get('driver1', '').strip().upper()
        driver2 = self.request.GET.get('driver2', '').strip().upper()

        race_options = services.get_completed_races_list(year)
        driver_options = sorted([{'code': d['code'], 'name': d['name']} for d in data.DRIVERS_2026], key=lambda x: x['name'])
        
        chart_data, error_message = services.fetch_lap_comparison(year, round_num, driver1, driver2)

        context.update({
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
        return context


class CircuitDetailView(TemplateView):
    template_name = 'dashboard/circuit_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        location = kwargs.get('location')
        info = data.CIRCUITS.get(location, {
            'wiki': location.replace(' ', '_'), 'country': '—', 'city': location,
            'length_km': '—', 'turns': '—', 'lap_record': '—', 'first_gp': '—',
            'desc': 'Detailed information for this circuit is not yet available.',
        })
        context.update({
            'location': location,
            'info': info,
            'wiki_url': f"https://en.wikipedia.org/wiki/{info['wiki']}",
        })
        return context


class DriversView(TemplateView):
    template_name = 'dashboard/drivers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team_filter = self.request.GET.get('team', '')
        teams = sorted(set(d['team'] for d in data.DRIVERS_2026))
        drivers = [d for d in data.DRIVERS_2026 if not team_filter or d['team'] == team_filter]
        
        context.update({
            'drivers': drivers,
            'teams': teams,
            'selected_team': team_filter,
        })
        return context


class DriverDetailView(TemplateView):
    template_name = 'dashboard/driver_detail.html'

    def get(self, request, *args, **kwargs):
        code = kwargs.get('code', '')
        driver = data.DRIVER_MAP.get(code.upper())
        if not driver:
            return redirect('drivers')
        
        context = self.get_context_data(**kwargs)
        context.update({
            'driver': driver,
            'wiki_url': f"https://en.wikipedia.org/wiki/{driver['wiki']}",
        })
        return self.render_to_response(context)


class ConstructorsView(TemplateView):
    template_name = 'dashboard/constructors.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['constructors'] = data.CONSTRUCTORS_2026
        return context


class HistoryView(TemplateView):
    template_name = 'dashboard/history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'legends': data.LEGENDS,
            'eras': data.HISTORY_ERAS,
            'glossary': data.GLOSSARY,
        })
        return context


class QuizView(TemplateView):
    template_name = 'dashboard/quiz.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        questions = random.sample(data.QUIZ_QUESTIONS, min(5, len(data.QUIZ_QUESTIONS)))
        answer_map = {q['q']: q['answer'] for q in questions}
        encoded = base64.b64encode(json.dumps(answer_map).encode()).decode()
        
        context.update({
            'questions': questions,
            'encoded_answers': encoded,
        })
        return context


class QuizCheckView(View):
    def post(self, request, *args, **kwargs):
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

    def get(self, request, *args, **kwargs):
        return redirect('quiz')

# ── Authentication Views ──────────────────────────────────────────────────────
class RegisterView(CreateView):
    template_name = 'dashboard/register.html'
    form_class = CustomRegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, "Account created successfully! You can now log in.")
        return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = 'dashboard/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home')


class CustomLogoutView(LogoutView):
    next_page = 'home'


# ── Profile & Customization Views ─────────────────────────────────────────────
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/profile.html'
    login_url = 'login' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        form = UserProfileForm(instance=profile)
        
        context.update({
            'form': form,
            'favorite_driver_data': data.DRIVER_MAP.get(profile.favorite_driver),
            'favorite_team_data': next((t for t in data.CONSTRUCTORS_2026 if t['name'] == profile.favorite_team), None)
        })
        return context

    def post(self, request, *args, **kwargs):
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        form = UserProfileForm(request.POST, instance=profile)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Your preferences have been updated successfully!")
            return redirect('profile')
            
        return render(request, self.template_name, {'form': form})
    
class SettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/settings.html'
    login_url = 'login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserSettingsForm(instance=self.request.user)
        return context
        
    def post(self, request, *args, **kwargs):
        form = UserSettingsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Account settings updated successfully!")
            return redirect('settings')
        return render(request, self.template_name, {'form': form})

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'dashboard/password_change.html'
    success_url = reverse_lazy('settings')
    
    def form_valid(self, form):
        messages.success(self.request, "Your password was successfully updated!")
        return super().form_valid(form)

class DeleteAccountView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, "Your account has been successfully deleted. We are sorry to see you go!")
        return redirect('home')