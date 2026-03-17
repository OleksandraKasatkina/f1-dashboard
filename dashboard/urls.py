# pathes of the app

from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule_view, name='schedule'), 
]