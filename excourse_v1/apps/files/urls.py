from django.urls import path
from . import views
urlpatterns = [
    path('files/upload/courses/',views.UploadCourseView.as_view()),



]
