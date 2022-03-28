from django.urls import path
from . import views
urlpatterns = [
    path('schedule/',views.ScheduleView.as_view()),



]
