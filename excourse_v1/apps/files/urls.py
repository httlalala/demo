from django.conf import settings
from django.contrib.staticfiles.views import serve
from django.urls import path
from . import views
urlpatterns = [
    # 上传课表
    path('files/upload/courses/',views.UploadCourseView.as_view()),
    # 下载课表（+申请表）
    path('files/download/courses/',views.DownloadCourseView.as_view()),
    # 下载模板
    path('files/download/template/',views.DownloadtemplateView.as_view()),



]

