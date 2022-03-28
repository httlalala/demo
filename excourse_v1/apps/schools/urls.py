from django.urls import path
from schools import views
urlpatterns = [
    path('schools/', views.SchoolListView.as_view()),
    path('schools/<pk>/', views.SchoolRetrieveView.as_view()),


    path('schools/firstweek/', views.FirstWeekSetView.as_view()),


]
