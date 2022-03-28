import logging
from datetime import datetime
from random import randint
from urllib import request
from urllib.parse import quote

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from utils.sendMessage import sendTemplateSMS
from .models import SMSCode
# Create your views here.
from rest_framework.views import APIView
logger = logging.getLogger('django')






class SMSCodeView(APIView):
    def post(self,request):
        # todo 获取数据 校验
        username = request.data.get('username')
        phone = request.data.get('phone')
        if not all([username,phone]):
            return Response({'msg': "缺少参数"}, status=status.HTTP_403_FORBIDDEN)
        # todo 生成验证码
        sms_code = '%06d' % randint(0, 999999)
        logger.info(sms_code)
        # todo 服务端保存验证码
        # 首先尝试获取
        try:
            lastcode = SMSCode.objects.get(phone=phone)
            last_time = lastcode.update_time.replace(tzinfo=None)
            diff = int((datetime.now()-last_time).seconds)
            if diff < 60:
                return Response({'msg':"发送过于频繁，请%d秒后再试"%(60-diff)},status=status.HTTP_403_FORBIDDEN)
            else:
                lastcode.code=sms_code
                lastcode.save()
        except SMSCode.DoesNotExist:
            SMSCode.objects.create(phone=phone,code=sms_code)
        # todo 利用XX发送短信验证码
        res = sendTemplateSMS(name=username,code=sms_code,mobile=phone)

        # todo 响应
        if res['stat'] == 100:
            return Response({'message': '发送成功'},status=status.HTTP_200_OK)
        else:
            return Response({'message': '发送失败'}, status=status.HTTP_400_BAD_REQUEST)

