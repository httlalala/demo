from django.urls import path
from . import views
urlpatterns = [
    path('applications/manager/<pk>/',views.GradeManagerRaiseApplicationsView.as_view()),
    path('applications/manager/',views.GradeManagerApplicationsView.as_view()),

    path('applications/mine/',views.MineApplicationsView.as_view()),

    path('applications/<pk>/',views.ApplicationsView.as_view()),
    path('applications/',views.ApplicationsView.as_view()),

]
