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

from utils.permission import GradeManagerPermission
from applications.models import Application
from courses.models import Course
from schools.models import School
from .serializer import SchoolSerializer


class FirstWeekSetView(APIView):
    permission_classes = [IsAuthenticated,GradeManagerPermission]
    def get(self,request):
        date = request.data.get('date')
        try:
            date = datetime.datetime.strptime(date, '%Y-%m-%d')
            self.request.user.school_id.first_week_date = date
            self.request.user.school_id.save()
        except Exception as e:
            return Response({'msg':"修改失败，请检查date参数"},status=status.HTTP_403_FORBIDDEN)
        return Response({'msg':"修改成功！"},status=status.HTTP_200_OK)


class SchoolListView(ListAPIView,CreateAPIView):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()


class SchoolRetrieveView(RetrieveAPIView,UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SchoolSerializer
    queryset = School.objects.all()
    def put(self, request, *args, **kwargs):
        return self.update(request,partial=True)



