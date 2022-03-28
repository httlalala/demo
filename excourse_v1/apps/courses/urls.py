from django.urls import path
from . import views


urlpatterns = [
    path('courses/choices/<type>/', views.ChoicesApplicationsView.as_view()),
    path('courses/', views.CourseView.as_view()),


]



