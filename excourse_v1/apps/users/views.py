from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.filters import UserViewFilter
from utils.permission import GradeManagerPermission, SuperManagerPermission
from .models import User
from .serializer import CreateUserSerializer,UpdateUserSerializer
from rest_framework import filters


# Create your views here.


class CheckUsername(APIView):
    def post(self,request):
        username = request.data.get('username')
        school_id = int(request.data.get('school_id'))
        try:
            user = User.objects.get(username=username,school_id=school_id)
        except User.DoesNotExist:
            return Response({"msg":'用户名可用'},status=status.HTTP_200_OK)
        if user:
            return Response({"msg": '用户名已存在！'}, status=status.HTTP_403_FORBIDDEN)

class RegisterView(CreateAPIView):
    serializer_class = CreateUserSerializer

class UserInfoView(UpdateAPIView,RetrieveAPIView):
    serializer_class = UpdateUserSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def put(self, request,pk):
        if self.request.user.is_super == 0:
            if (not self.request.user.is_grade) and pk != self.request.user.id:
                return Response({"msg":"您只能修改自己的信息!"},status=403)
        return self.update(request,pk, partial=True)


class UserView(ListAPIView):
    serializer_class = UpdateUserSerializer
    permission_classes = [IsAuthenticated,SuperManagerPermission]
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    # 添加过滤字段 不写的话就是全部字段都可以用来过滤
    # filterset_fields = ["phone","username"]
    filterset_class = UserViewFilter
    ordering_fields = '__all__'


    def get_queryset(self):
        return User.objects.filter(school_id=self.request.user.school_id)




