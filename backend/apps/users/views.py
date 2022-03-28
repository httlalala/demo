from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializer import CreateUserSerializer,UpdateUserSerializer



# Create your views here.




class RegisterView(CreateAPIView):
    serializer_class = CreateUserSerializer

class UserInfoView(UpdateAPIView,RetrieveAPIView):
    serializer_class = UpdateUserSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def put(self, request,pk):
        if (not self.request.user.is_grade) and pk != self.request.user.id:
            return Response({"msg":"您只能修改自己的信息!"},status=403)
        return self.update(request,pk, partial=True)






