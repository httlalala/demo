from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.response import Response
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta
from rest_framework_jwt.settings import api_settings

from courses.models import Course


class CoursesSerializer(serializers.ModelSerializer):
    teacher_name = serializers.SerializerMethodField(read_only=True)
    grade = serializers.SerializerMethodField(read_only=True)
    class_number = SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ('id',)

    def get_teacher_name(self, obj):
        return obj.teacher_id.username

    def get_grade(self, obj):
        return obj.class_id.grade

    def get_class_number(self, obj):
        return obj.class_id.class_number
