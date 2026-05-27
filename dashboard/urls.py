from django.urls import path
from .views import (
    HomeView, ScheduleView, StandingsView, ResultsView, CompareView,
    DriversView, DriverDetailView, ConstructorsView, HistoryView,
    QuizView, QuizCheckView, CircuitDetailView
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
]