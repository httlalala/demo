from django.db.models import Q, F
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from .serializer import CoursesSerializer
from courses.models import Course
from classes.models import Class



class CourseView(ListAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = CoursesSerializer
    queryset = Course.objects.all()

    def get_queryset(self):
        # todo 根据grade class_number等班级条件过滤
        # 获取过滤条件
        class_filters = {}
        for attr, value in self.request.data.items():
            if hasattr(Class, attr):
                class_filters[attr] = value
        class_list = Class.objects.filter(**class_filters).values('id')
        # 过滤
        course_qs = Course.objects.filter(class_id__in=class_list)
        # todo 根据week, weekday, order, teacher_id等课程条件过滤
        # 获取过滤条件
        course_filters = {}
        for attr, value in self.request.data.items():
            if hasattr(Course, attr):
                course_filters[attr] = value
        # 过滤
        course_qs = Course.objects.filter(**course_filters)
        return course_qs



class ChoicesApplicationsView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CoursesSerializer

    queryset = Course.objects.all()


    def get(self, request,type):
        # todo 数据获取并校验
        type = int(type)
        if type not in [0, 1]:
            return Response({'msg': "type参数无效或未指定"}, status=status.HTTP_404_NOT_FOUND)
        course_id = self.request.data.get('applicant_course_id', None)
        if not course_id:
            return Response({'msg': "applicant_course_id参数无效或未指定"}, status=status.HTTP_404_NOT_FOUND)
        # todo 获取 申请课程 对象
        try:
            applicant_course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({'msg': "对应的课程不存在"}, status=status.HTTP_404_NOT_FOUND)
        # todo 业务处理(筛选课程并序列化)
        if type == 0:
            # todo 同班课程
            grade = applicant_course.class_id.grade
            class_number = applicant_course.class_id.class_number
            class_id = Class.objects.get(grade=grade, class_number=class_number,school_id=applicant_course.class_id.school_id).id
            qs = Course.objects.filter(class_id=class_id)
            # todo 时间不冲突 对方在这个时间没课
            qs = qs.exclude(
                Q(week=applicant_course.week) & Q(weekday=applicant_course.weekday) & Q(order=applicant_course.order))
            # todo 时间不冲突 自己在对方时间没课
            mine =  qs.filter(teacher_id=self.request.user.id).values('week','weekday','order')
            for timedict in mine:
                qs = qs.exclude(week=timedict['week'],weekday=timedict['weekday'],order=timedict['order'])
            # course_time_id_list = qs.filter(teacher_id=self.request.user.id).values_list('course_time_id')
            # qs = qs.exclude(course_time_id__in=course_time_id_list)
            # todo 未来的课程
            qs = qs.filter(
                Q(week=applicant_course.week, weekday__gt=applicant_course.weekday) | Q(week__gt=applicant_course.week))
        elif type == 1:
            pass
        serializer = self.get_serializer(qs, many=True)  # 还会给序列化器传一个context ： view+request+many等其他参数
        return Response(data=serializer.data)


    # def get(self, request, type):
    #     # todo 数据获取并校验
    #     type = int(type)
    #     if type not in [0, 1]:
    #         return Response({'msg': "type参数无效或未指定"}, status=status.HTTP_404_NOT_FOUND)
    #
    #     course_id = request.data.get('applicant_course_id', None)
    #     print(request.data)
    #     if not course_id:
    #         return Response({'msg': "applicant_course_id参数无效或未指定"}, status=status.HTTP_404_NOT_FOUND)
    #     # todo 获取 申请课程 对象
    #     try:
    #         applicant_course = Course.objects.get(id=course_id)
    #     except Course.DoesNotExist:
    #         return Response({'msg': "对应的课程不存在"}, status=status.HTTP_404_NOT_FOUND)
    #     # todo 业务处理(筛选课程并序列化)
    #     if type == 0:
    #         # todo 同班课程
    #         grade = applicant_course.class_id.grade
    #         class_number = applicant_course.class_id.class_number
    #         class_id = Class.objects.get(grade=grade, class_number=class_number).id
    #         qs = Course.objects.filter(class_id=class_id)
    #         # todo 时间不冲突 对方在这个时间没课
    #         qs = qs.exclude( Q(week=applicant_course.week) & Q(weekday=applicant_course.weekday) & Q(order=applicant_course.order))
    #         # todo 时间不冲突 自己在对方时间没课
    #         course_time_id_list = qs.filter(teacher_id=self.request.user.id).values_list('course_time_id')
    #         qs = qs.exclude(course_time_id__in=course_time_id_list)
    #         # todo 未来的课程
    #         qs = qs.filter(Q(week=applicant_course.week, weekday__gt=applicant_course.weekday) | Q(week__gt=applicant_course.week))
    #     elif type == 1:
    #         pass
    #
    #     serializer = CoursesSerializer(instance=qs, many=True)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)


