from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.response import Response
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta
from rest_framework_jwt.settings import api_settings
from schools.models import School
from courses.models import Course

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
