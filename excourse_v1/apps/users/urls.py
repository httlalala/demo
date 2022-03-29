from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [
    # 检查用户名是否可用
    path('users/check/',views.CheckUsername.as_view()),
    # 注册
    path('users/register/',views.RegisterView.as_view()),
    # 登录
    path('users/login/',obtain_jwt_token),
    # 修改信息和查看信息
    path('users/<pk>/',views.UserInfoView.as_view()),





]
