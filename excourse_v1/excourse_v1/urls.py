"""excourse_v1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path,include
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from schools.models import School
from utils.permission import GradeManagerPermission
from utils.timediff import week2date, date2week


class viewtest(APIView):
    # permission_classes = [IsAuthenticated,GradeManagerPermission]
    def get(self,request):
        # print(request.data)
        # school = self.request.user.school_id
        return Response(data={'msg':"dwdwdwd"},status=status.HTTP_204_NO_CONTENT)

class viewtestmessage(APIView):
    # permission_classes = [IsAuthenticated,GradeManagerPermission]
    def get(self,request):
        # print(request.data)
        # school = self.request.user.school_id
        from utils import sendMessage
        res = sendMessage.substitutionComplete(teacher_name='郝高阳',manager_name="赵鸿序",mobile='13833916349')
        return Response(data=res,status=status.HTTP_204_NO_CONTENT)

class viewtestinsertdata(APIView):
    # permission_classes = [IsAuthenticated,GradeManagerPermission]
    def get(self,request):
        # print(request.data)
        # school = self.request.user.school_id
        from utils import insertdata
        insertdata.test()
        return Response(status=status.HTTP_204_NO_CONTENT)



class index(views.View):
    # permission_classes = [IsAuthenticated,GradeManagerPermission]
    def get(self,request):
        return HttpResponse("ok")

class week2dateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        week = request.data.get('week',None)
        if week:
            date = week2date(week=week,school_id=self.request.user.school_id_id)
            return Response(data=date,status=status.HTTP_200_OK)
        else:
            return Response({"请检查week参数"}, status=status.HTTP_400_BAD_REQUEST)

class date2weekView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        date = request.data.get('date', None)
        if date:
            date = date2week(date=date,school_id=self.request.user.school_id_id)
            if date == -1:
                return Response({"传入的日期有误"},status=status.HTTP_400_BAD_REQUEST)
            return Response(data=date,status=status.HTTP_200_OK)
        else:
            return Response({"请检查date参数"}, status=status.HTTP_400_BAD_REQUEST)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('users.urls')),
    path('', include('applications.urls')),
    path('', include('schools.urls')),
    path('', include('classes.urls')),
    path('', include('courses.urls')),
    path('', include('verifications.urls')),
    path('', include('files.urls')),

    # 测试
    path('test/', viewtest.as_view()),


    path('testmessage/',viewtestmessage.as_view()),
    path('testinsertdata/',viewtestinsertdata.as_view()),
    path('index/',index.as_view()),

    path('week2date/',week2dateView.as_view()),
    path('date2week/',date2weekView.as_view()),

]


