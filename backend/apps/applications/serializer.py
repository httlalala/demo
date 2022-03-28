from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.response import Response
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta
from rest_framework_jwt.settings import api_settings

from applications.models import Application
from courses.models import Course
from courses.serializer import CoursesSerializer

class MyBaseSerializer(serializers.ModelSerializer):
    applicant_course_name = SerializerMethodField('applicant_course_name', read_only=True)
    applicant_course_grade = SerializerMethodField('applicant_course_grade', read_only=True)
    applicant_course_class_number = SerializerMethodField('applicant_course_class_number', read_only=True)
    applicant_course_week = SerializerMethodField('applicant_course_week', read_only=True)
    applicant_course_weekday = SerializerMethodField('applicant_course_weekday', read_only=True)
    applicant_course_order = SerializerMethodField('applicant_course_order', read_only=True)
    applicant_teacher_name = SerializerMethodField('applicant_teacher_name', read_only=True)
    applicant_teacher_phone = SerializerMethodField('applicant_teacher_phone', read_only=True)

    target_course_name = SerializerMethodField('target_course_name', read_only=True)
    target_course_grade = SerializerMethodField('target_course_grade', read_only=True)
    target_course_class_number = SerializerMethodField('target_course_class_number', read_only=True)
    target_course_week = SerializerMethodField('target_course_week', read_only=True)
    target_course_weekday = SerializerMethodField('target_course_weekday', read_only=True)
    target_course_order = SerializerMethodField('target_course_order', read_only=True)
    target_teacher_name = SerializerMethodField('target_teacher_name', read_only=True)
    target_teacher_phone = SerializerMethodField('target_teacher_phone', read_only=True)

    def applicant_course_name(self, obj):
        return obj.applicant_course_id.name

    def applicant_course_grade(self, obj):
        return obj.applicant_course_id.grade

    def applicant_course_class_number(self, obj):
        return obj.applicant_course_id.class_number

    def applicant_course_week(self, obj):
        return obj.applicant_course_id.week

    def applicant_course_weekday(self, obj):
        return obj.applicant_course_id.weekday

    def applicant_course_order(self, obj):
        return obj.applicant_course_id.order

    def applicant_teacher_name(self, obj):
        return obj.applicant_course_id.teacher_id.username

    def applicant_teacher_phone(self, obj):
        return obj.applicant_course_id.teacher_id.phone

    def target_course_name(self, obj):
        return obj.target_course_id.name

    def target_course_grade(self, obj):
        return obj.target_course_id.grade

    def target_course_class_number(self, obj):
        return obj.target_course_id.class_number

    def target_course_week(self, obj):
        return obj.target_course_id.week

    def target_course_weekday(self, obj):
        return obj.target_course_id.weekday

    def target_course_order(self, obj):
        return obj.target_course_id.order

    def target_teacher_name(self, obj):
        return obj.target_course_id.teacher_id.username

    def target_teacher_phone(self, obj):
        return obj.target_course_id.teacher_id.phone


class ApplicationsSerializer(serializers.ModelSerializer):
    applicant_info = SerializerMethodField(read_only=True)
    target_info = SerializerMethodField(read_only=True,allow_null=True)

    def get_applicant_info(self,obj):
        dict = {
            'name':obj.applicant_course_id.name,
            'week':obj.applicant_course_id.week,
            'weekday':obj.applicant_course_id.weekday,
            'order':obj.applicant_course_id.order,
            'grade':obj.applicant_course_id.class_id.grade,
            'class_number':obj.applicant_course_id.class_id.class_number,
            'teacher_name':obj.applicant_course_id.teacher_id.username,
            'teacher_phone':obj.applicant_course_id.teacher_id.phone
        }
        return dict
    def get_target_info(self,obj):
        if obj.target_course_id:
            dict = {
                'name': obj.target_course_id.name,
                'week': obj.target_course_id.week,
                'weekday': obj.target_course_id.weekday,
                'order': obj.target_course_id.order,
                'grade': obj.target_course_id.class_id.grade,
                'class_number': obj.target_course_id.class_id.class_number,
                'teacher_name':obj.target_course_id.teacher_id.username,
                'teacher_phone':obj.target_course_id.teacher_id.phone
            }
            return dict
        return None

    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ('id',)
        extra_kwargs = {'fail_time':{'required':False}}

    # def validate(self, attrs):
    #
    #     applicant_course_id = attrs.get('applicant_course_id',None)
    #     if applicant_course_id:
    #         try:
    #             applicant_course_start_time = applicant_course_id.start_time
    #         except Exception:
    #             raise serializers.ValidationError('设置fail_time出错')
    #         attrs['fail_time'] = applicant_course_start_time
    #     return attrs







