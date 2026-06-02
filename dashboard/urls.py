from django.urls import path
from .views import (
    HomeView, ScheduleView, StandingsView, ResultsView, CompareView,
    DriversView, DriverDetailView, ConstructorsView, HistoryView,
    QuizView, QuizCheckView, CircuitDetailView,
    RegisterView, CustomLoginView, CustomLogoutView, ProfileView,
    SettingsView, CustomPasswordChangeView, DeleteAccountView 
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('schedule/', ScheduleView.as_view(), name='schedule'),
    path('standings/', StandingsView.as_view(), name='standings'),
    path('results/', ResultsView.as_view(), name='results'),
    path('compare/', CompareView.as_view(), name='compare'),
    path('drivers/', DriversView.as_view(), name='drivers'),
    path('drivers/<str:code>/', DriverDetailView.as_view(), name='driver_detail'),
    path('constructors/', ConstructorsView.as_view(), name='constructors'),
    path('history/', HistoryView.as_view(), name='history'),
    path('quiz/', QuizView.as_view(), name='quiz'),
    path('quiz/check/', QuizCheckView.as_view(), name='quiz_check'),
    path('circuit/<str:location>/', CircuitDetailView.as_view(), name='circuit_detail'),
    
    # Auth & Profile paths
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    
    # Settings paths
    path('settings/', SettingsView.as_view(), name='settings'),
    path('settings/password/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('settings/delete/', DeleteAccountView.as_view(), name='delete_account'),
]