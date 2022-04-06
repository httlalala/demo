import logging
import os

from django.http import FileResponse
from django.shortcuts import render

# Create your views here.
from django.utils.encoding import escape_uri_path
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings

from files.models import UploadRecord
from schools.models import School
from utils.generateCourseFile import saveFile
from utils.permission import GradeManagerPermission,SuperManagerPermission
from utils.insertdata import generateData
from utils.timediff import week2date

class UploadCourseView(APIView):
    permission_classes = [IsAuthenticated,SuperManagerPermission]
    def post(self,request):
        myFile = request.FILES.get("file", None)
        week_start = request.POST.get("week_start", 1)
        week_start = int(week_start)
        logger = logging.getLogger('django')
        logger.info(request.POST.get("week_start", None))
        try:
            school = self.request.user.school_id
            if not school.first_week_date:
                return Response({"msg": "请先设置第一周开始日期"}, status=status.HTTP_403_FORBIDDEN)
        except Exception:
            return Response({"msg":"当前用户所属学校信息错误"},status=status.HTTP_403_FORBIDDEN)

        if not myFile:
            return Response({"msg":"no files for upload!"},status=status.HTTP_403_FORBIDDEN)

        filename = os.path.join(settings.BASE_DIR,'media/upload/courses',myFile.name)
        if os.path.exists(filename):
            filename
        destination = open(filename,'wb+')
        for chunk in myFile.chunks():
            destination.write(chunk)
        destination.close()

        if generateData(filename=filename,school_id=school.id,week_start=week_start):
            # todo 写数据库
            UploadRecord.objects.create(path=filename,uploader_id=self.request.user,start_time=week2date(school_id=school.id,week=week_start))
            return Response({"msg":"上传成功"},status=status.HTTP_200_OK)
        else:
            return Response({"msg": "上传失败，请重试!"}, status=status.HTTP_403_FORBIDDEN)




class DownloadCourseView(APIView):
    permission_classes = [IsAuthenticated,SuperManagerPermission]
    def post(self, request):
        is_application = request.data.get('is_application',False)
        path = os.path.join(settings.BASE_DIR,'media','download')
        week_start = request.data.get('week_start',1)
        week_end = request.data.get('week_end',self.request.user.school_id.week_num)
        # week_end = 5
        week_start = int(week_start)
        week_end = int(week_end)

        filename,fname = saveFile(week_start, week_end, path=path, is_application=is_application)
        if filename is None:
            return Response({"msg":"服务器导出出错，请联系管理员"},status=status.HTTP_403_FORBIDDEN)
        # local_filename = os.path.join(settings.BASE_DIR,'media/upload/courses')
        # filename = os.listdir(local_filename)
        # filename.sort(key=lambda fn: os.path.getatime(local_filename + fn) if not os.path.isdir(local_filename + fn) else 0)
        file = open(filename, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Access-Control-Expose-Headers'] = "Content-Disposition, Content-Type"
        response['Content-Disposition'] = "attachment; filename={}".format(fname)
        return response




class DownloadtemplateView(APIView):
    # permission_classes = [IsAuthenticated,SuperManagerPermission]
    def get(self, request):
        path = os.path.join(settings.BASE_DIR,'media','download')
        fname = 'template.xls'
        filename = os.path.join(path,fname)
        file = open(filename, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Access-Control-Expose-Headers'] = "Content-Disposition, Content-Type"
        response['Content-Disposition'] = "attachment; filename={}".format(fname)
        return response









