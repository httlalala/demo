from django.db.models import Q, F
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from utils.pagination import StandardResultsSetPagination
from .serializer import CoursesSerializer
from courses.models import Course
from classes.models import Class



class CourseView(ListAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = CoursesSerializer
    queryset = Course.objects.all()

    def get_queryset(self):
        # todo 根据 school_id grade class_number 等班级条件过滤
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
        course_qs = course_qs.filter(**course_filters)
        return course_qs



class ChoicesApplicationsView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CoursesSerializer
    pagination_class = StandardResultsSetPagination

    queryset = Course.objects.all()

    def get_queryset(self):
        # todo 数据获取并校验
        type = int(self.request.parser_context['kwargs'].get('type'))
        if type not in [0, 1]:
            return Response({'msg': "type参数无效或未指定"}, status=status.HTTP_404_NOT_FOUND)
        course_id = self.request.data.get('applicant_course_id', None)
        if course_id is None:
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
            class_id = Class.objects.get(grade=grade, class_number=class_number,
                                         school_id=applicant_course.class_id.school_id).id
            qs = Course.objects.filter(class_id=class_id)
            # todo 时间不冲突 对方在这个时间没课
            qs = qs.exclude(
                Q(week=applicant_course.week, weekday=applicant_course.weekday, order=applicant_course.order))
            # todo 时间不冲突 自己在对方时间没课
            mine = qs.filter(teacher_id=applicant_course.teacher_id).values('week', 'weekday', 'order')
            for timedict in mine:
                qs = qs.exclude(week=timedict['week'], weekday=timedict['weekday'], order=timedict['order'])
            # course_time_id_list = qs.filter(teacher_id=self.request.user.id).values_list('course_time_id')
            # qs = qs.exclude(course_time_id__in=course_time_id_list)
            # todo 未来的课程
            qs = qs.filter(
                Q(week=applicant_course.week, weekday__gt=applicant_course.weekday) | Q(week__gt=applicant_course.week))
        elif type == 1:
            # todo 同年级
            class_id = Class.objects.filter(grade=applicant_course.class_id.grade).values('id')
            qs = Course.objects.filter(class_id__in=class_id)
            # todo 时间不冲突 对方在这个时间没课
            qs = qs.exclude(Q(week=applicant_course.week, weekday=applicant_course.weekday, order=applicant_course.order))
            # todo 未来的课程
            qs = qs.filter(Q(week=applicant_course.week, weekday__gt=applicant_course.weekday) | Q(week__gt=applicant_course.week))
        qs = qs.order_by('week')
        return qs

