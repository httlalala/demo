from django.urls import path
from . import views


urlpatterns = [
    path('vertifications/', views.SMSCodeView.as_view()),
]



