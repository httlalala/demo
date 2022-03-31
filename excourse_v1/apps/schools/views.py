import datetime
from time import strftime

from django.db.models import Q
from django.shortcuts import render
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.filters import UserViewFilter
from utils.permission import GradeManagerPermission
from applications.models import Application
from courses.models import Course
from schools.models import School
from .serializer import SchoolSerializer


class FirstWeekSetView(APIView):
    permission_classes = [IsAuthenticated,GradeManagerPermission]
    serializer_class = SchoolSerializer
    def put(self,request,pk):
        date = request.data.get('date')
        try:
            date = datetime.datetime.strptime(date, '%Y-%m-%d')
            school = School.objects.get(id=pk)
            # self.request.user.school_id.first_week_date = date
            # self.request.user.school_id.save()
            school.first_week_date = date
            school.save()
        except Exception as e:
            return Response({'msg':"修改失败，请检查date参数"},status=status.HTTP_403_FORBIDDEN)
        ser = SchoolSerializer(school)
        return Response(ser.data,status=status.HTTP_200_OK)


class SchoolListView(ListAPIView,CreateAPIView):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()
    # filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    # filterset_fields = ["id", "name", 'province','city','region']
    # ordering_fields = ['id', 'name', 'province','city','region']
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'




class SchoolRetrieveView(RetrieveAPIView,UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SchoolSerializer
    queryset = School.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request,partial=True)



