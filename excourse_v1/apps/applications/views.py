import datetime

from django.db.models import Q
from django.shortcuts import render
from rest_framework import status, filters
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from classes.models import Class
from utils import sendMessage
from utils.filters import UserViewFilter
from utils.permission import GradeManagerPermission
from .serializer import ApplicationsSerializer
from applications.models import Application
from courses.models import Course

# 调代课双方我




class GradeManagerRaiseApplicationsView(UpdateAPIView):
    permission_classes = [IsAuthenticated,GradeManagerPermission,]
    serializer_class = ApplicationsSerializer
    queryset = Application.objects.filter(type=1)
    '''
    管理员修改申请表：
        A发起的代课请求，分配代课目标：添加 handle_time,handler_id,target_course_id,accept|发短信|换课
    提交申请表：
        为A发起一个代课请求，分配代课目标：添加applicant_course_id,handle_time,handler_id|发短信|换课
    '''
    def put(self, request, pk):
        # todo 添加参数 handle_time,handler_id,target_course_id,(cancel_reason)
        res = self.update(request, pk, partial=True)
        if request.data.get("cancel_reason",None):
            # todo 有cancel_reason 代表拒绝代课请求，默认帮目标方处理
            application = Application.objects.get(id=pk)
            application.solver_confirm = 1
            application.save()
            # todo 给申请人发短信通知
            applicant_info = res.data.get('applicant_info')
            sendMessage.substitutionApplicant(applicant_name=applicant_info['teacher_name'],
                                              manager_name=request.user.username,
                                              mobile=applicant_info['teacher_phone'])
            return res
        else:
            # todo 代课处理完成，给双方短信
            applicant_info = res.data.get('applicant_info')
            target_info = res.data.get('applicant_info')
            sendMessage.substitutionApplicant(applicant_name=applicant_info['teacher_name'],manager_name=request.user.username,mobile=applicant_info['teacher_phone'])
            sendMessage.substitutionTarget(applicant_name=applicant_info['teacher_name'],target_name=target_info['teacher_name'],manager_name=request.user.username,mobile=target_info['teacher_phone'])
            # todo 换课
            applicant_course = Course.objects.get(id=res.data.get('applicant_course_id'))
            target_course = Course.objects.get(id=res.data.get('target_course_id'))
            applicant_course.teacher_id,target_course.teacher_id = target_course.teacher_id,applicant_course.teacher_id
            return res




class GradeManagerApplicationsView(CreateAPIView,ListAPIView):
    permission_classes = [IsAuthenticated,GradeManagerPermission,]
    serializer_class = ApplicationsSerializer
    queryset = Application.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'

    def get(self, request):
        type = self.request.query_params.get('type', None)
        if not type or type not in ['substitution', 'history']:
            return Response({'msg': 'type参数无效或未指定'}, status=status.HTTP_404_NOT_FOUND)
        return self.list(request)
    def get_queryset(self):
        qs = self.queryset
        type = self.request.query_params.get('type', None)
        if type == 'substitution':
            qs = Application.objects.filter(handle_time=None,overdue=False,type=1)
        elif type == 'history':
            qs = Application.objects.filter(Q(handler_id=self.request.user.id)|Q(overdue=True)|Q(target_course_id__teacher_id=self.request.user.id,solver_confirm__in=[1,2],cancel_reason=None)|Q(applicant_course_id__teacher_id=self.request.user.id,solver_confirm__in=[1,2],applicant_confirm=1))
        return qs

    def post(self, request):
        applicant_course_id = request.data.get('applicant_course_id', None)
        if applicant_course_id is None:
            return Response({"msg": "提交的applicant_course_id有误"})
        try:
            applicant_course_start_time = Course.objects.get(id=int(applicant_course_id)).start_time
        except Exception:
            return Response({"msg": "提交的applicant_course_id有误"})
        request.data['fail_time'] = applicant_course_start_time
        request.data['handler_id'] = self.request.user.id
        request.data['handle_time'] = datetime.datetime.now()
        res = self.create(request)
        # todo 年级管理员发起的  代课请求 无法被拒接，直接修改课程表
        applicant_course = Course.objects.get(id=res.data.get('applicant_course_id'))
        target_course = Course.objects.get(id=res.data.get('target_course_id'))
        applicant_course.teacher_id = target_course.teacher_id
        # todo 代课处理完成，给双方短信
        applicant_info = res.data.get('applicant_info')
        target_info = res.data.get('applicant_info')
        # ????????????????新模板??????????????????????
        sendMessage.substitutionApplicant(applicant_name=applicant_info['teacher_name'],
                                          manager_name=request.user.username, mobile=applicant_info['teacher_phone'])
        sendMessage.substitutionTarget(applicant_name=applicant_info['teacher_name'],
                                       target_name=target_info['teacher_name'], manager_name=request.user.username,
                                       mobile=target_info['teacher_phone'])
        return res

class ApplicationsView(UpdateAPIView,CreateAPIView,ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ApplicationsSerializer
    queryset = Application.objects.all()

    def put(self, request, pk):
        res = self.update(request, pk, partial=True)
        solver_confirm = request.data.get('solver_confirm',None)
        if not solver_confirm:
            return res
        if solver_confirm == 1 and res.data.get('type') == 0:
            applicant_course = Course.objects.get(id=res.data.get('applicant_course_id'))
            target_course = Course.objects.get(id=res.data.get('target_course_id'))
            # todo 给申请方发个短信通知
            sendMessage.exchangeApplicant(applicant_name=applicant_course.teacher_id.username, target_name=target_course.teacher_id.username, mobile=applicant_course.teacher_id.phone)
            # todo 调课被同意了，修改课程表: 把互换课程id
            applicant_course.teacher_id,target_course.teacher_id = target_course.teacher_id,applicant_course.teacher_id
            return res

        if solver_confirm == 0 and res.data.get('type') == 0:
            applicant_course = Course.objects.get(id=res.data.get('applicant_course_id'))
            target_course = Course.objects.get(id=res.data.get('target_course_id'))
            # todo 给申请方发个短信通知
            sendMessage.exchangeApplicant(applicant_name=applicant_course.teacher_id.username, target_name=target_course.teacher_id.username, mobile=applicant_course.teacher_id.phone)
            # todo 调课被拒绝了，不需要修改课程表
            return res

    def post(self, request):
        applicant_course_id = request.data.get('applicant_course_id',None)
        if applicant_course_id is None:
            return Response({"msg": "提交的applicant_course_id有误"})
        try:
            applicant_course = Course.objects.get(id=int(applicant_course_id))
        except Course.DoesNotExist:
            return Response({"msg":"提交的applicant_course_id有误"})
        if int(request.data.get('type')) == 0:
            target_course_id = request.data.get('target_course_id', None)
            if target_course_id is None:
                return Response({"msg": "提交的target_course_id有误"})
            try:
                target_course = Course.objects.get(id=int(target_course_id))
            except Course.DoesNotExist:
                return Response({"msg":"target_course_id"})
            request.data['fail_time'] = applicant_course.start_time
            # todo 调课通知目标人
            sendMessage.exchangeTarget(applicant_name=applicant_course.teacher_id.username,target_name=target_course.teacher_id.username,mobile=target_course.teacher_id.phone)
        elif int(request.data.get('type')) == 1:
            # todo 代课通知管理员
            sendMessage.substitutionManager(applicant_name=applicant_course.teacher_id.username,grade=applicant_course.class_id.grade)
        return self.create(request)


class MineApplicationsView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ApplicationsSerializer
    queryset = Application.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'

    def get_queryset(self):
        type = self.request.query_params.get('type',None)
        if not type or type not in ['target','applicant','history']:
            return Response({'msg':'type参数无效或未指定'},status=status.HTTP_404_NOT_FOUND)
        if type == 'target':
            qs = Application.objects.filter(solver_confirm=0,overdue=False,target_course_id__teacher_id=self.request.user.id,cancel_reason=None)
        elif type == 'applicant':
            qs = Application.objects.filter(Q(applicant_course_id__teacher_id=self.request.user.id,solver_confirm=0,overdue=False)|
                                            Q(applicant_course_id__teacher_id=self.request.user.id,solver_confirm__in=[1,2],applicant_confirm=0,overdue=False))
        elif type == 'history':
            qs = Application.objects.filter(Q(overdue=True)|Q(target_course_id__teacher_id=self.request.user.id,solver_confirm__in=[1,2],cancel_reason=None)|Q(applicant_course_id__teacher_id=self.request.user.id,solver_confirm__in=[1,2],applicant_confirm=1))
        return qs



# H:\Anaconda\envs\django;H:\Anaconda\envs\django\Library\mingw-w64\bin;H:\Anaconda\envs\django\Library\usr\bin;H:\Anaconda\envs\django\Library\bin;H:\Anaconda\envs\django\Scripts;H:\Anaconda\envs\django\bin;H:\Anaconda\condabin;C:\Program Files (x86)\Common Files\Intel\Shared Libraries\redist\intel64_win\compiler;H:\Anaconda;H:\Anaconda\Scripts;H:\Anaconda\Library\mingw-w64\bin;H:\Anaconda\Library\usr\bin;H:\Anaconda\Library\bin;C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\bin;C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\libnvvp;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\iCLS;C:\Program Files\Intel\Intel(R) Management Engine Components\iCLS;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\IPT;C:\Program Files\Intel\Intel(R) Management Engine Components\IPT;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0;C:\WINDOWS\System32\OpenSSH;C:\Program Files\NVIDIA Corporation\NVIDIA NvDLISR;F:\Java\jdk8u282-b08\bin;C:\Program Files (x86)\NVIDIA Corporation\PhysX\Common;C:\Program Files\dotnet;C:\Program Files (x86)\dotnet;G:\OPENCV\opencv\build\x64\vc14\bin;H:\MATLAB\runtime\win64;H:\MATLAB\bin;H:\Anaconda\envs\tf1\Lib\site-packages\pyqt5_tools;H:\Anaconda\envs\tf1\Lib\site-packages\pyqt5_tools\Qt\bin;G:\鐎涳缚绡勯惄绋垮彠\闂婂疇顫嬫０鎱亸蹇擃劅閺堢喕顕崇粙瀣カ閺?- 閸╄桨绨現Fmpeg+SDL閻ㄥ嫯顫嬫０鎴炴尡閺€鎯ф珤閻ㄥ嫬鍩楁担娣哄銉ュ徔;H:\Tools\Xmanager;\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0;C:\WINDOWS\System32\OpenSSH;H:\Tools\Microsoft VS Code\bin;G:\spark-2.4.3-bin-hadoop2.7\bin;G:\hadoop-2.7.1\bin;H:\VS2017\IDE\VC\Tools\MSVC\14.16.27023\bin\Hostx64\x64;H:\Tools\MinGW\mingw64\bin;H:\Tools\XShell;H:\Tools\Xftp;H:\Tools\Git\cmd;C:\Users\lenovo\AppData\Local\Microsoft\WindowsApps;C:\Users\lenovo\AppData\Local\atom\bin;C:\Users\lenovo\AppData\Local\Microsoft\WindowsApps;C:\ProgramData\Microsoft\Windows\Start Menu\Programs\MySQL\MySQL Server 8.0;C:\Program Files\MySQL\MySQL Server 8.0\bin;H:\Tools\Git\bin;H:\Tools\Git\mingw64\bin;H:\Tools\Git\mingw64\libexec;.