# dashboard/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',                        views.home_view,           name='home'),
    path('schedule/',               views.schedule_view,       name='schedule'),
    path('standings/',              views.standings_view,      name='standings'),
    path('results/',                views.results_view,        name='results'),
    path('compare/',                views.compare_view,        name='compare'),
    path('drivers/',                views.drivers_view,        name='drivers'),
    path('drivers/<str:code>/',     views.driver_detail_view,  name='driver_detail'),
    path('constructors/',           views.constructors_view,   name='constructors'),
    path('history/',                views.history_view,        name='history'),
    path('quiz/',                   views.quiz_view,           name='quiz'),
    path('quiz/check/',             views.quiz_check_view,     name='quiz_check'),
    path('circuit/<str:location>/', views.circuit_detail_view, name='circuit_detail'),
]