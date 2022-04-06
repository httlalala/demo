from django.shortcuts import render
import datetime
from time import strftime

from django.db.models import Q
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from schedule.models import Schedule
from utils.permission import GradeManagerPermission
from applications.models import Application
from courses.models import Course
from schools.models import School

# Create your views here.

class ScheduleView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        # 获取week，weekday，order
        week = int(request.data.get('week',1))
        weekday = int(request.data.get('weekday',1))
        order = int(request.data.get('order',1))
        date = Schedule.objects.get(week=week,weekday=weekday,order=order)
        return Response({"msg":"获取成功","datetime":date},status=200)




# time = '8:40'
# week = 1
# weekday = 1
# time2datetime = datetime.datetime.strptime(time, '%H:%M')
#
# datetime.timedelta(weeks=1,hours=time2datetime.hour,minutes=time2datetime.minute)
