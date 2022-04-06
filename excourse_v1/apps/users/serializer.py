from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta
from rest_framework_jwt.settings import api_settings
import datetime

from schools.models import School
from users.models import User
from verifications.models import SMSCode
from utils.timediff import utc2local
from django.conf import settings

class UpdateUserSerializer(serializers.ModelSerializer):
    sms_code = serializers.CharField(write_only=True, required=False)
    school_name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id',)

    def update(self, instance, validated_data):
        phone = validated_data.pop('phone',None)
        password = validated_data.pop('password',None)
        if phone or password:  # 如果想要修改手机号
            if settings.MESSAGE_CAN_USE:
                # todo 校验验证码
                sms_code = validated_data.pop('sms_code',None)
                try:
                    real_code = SMSCode.objects.get(phone=phone)
                except SMSCode.DoesNotExist:
                    raise serializers.ValidationError('验证码错误')
                timediff = (datetime.datetime.now() - utc2local(real_code.update_time)).seconds
                if timediff > 300:
                    raise serializers.ValidationError('验证码已经失效')
                elif real_code.code != sms_code:
                    raise serializers.ValidationError('验证码错误')

            if password:  # 如果想要密码
                # todo 加密
                instance.set_password(password)
            if phone:  # 如果想要密码
                # todo 加密
                instance.phone=phone


        instance.school_name = School.objects.get(id = instance.school_id)


        raise_errors_on_nested_writes('update', self, validated_data)
        info = model_meta.get_field_info(instance)

        # Simply set each attribute on the instance, and then save it.
        # Note that unlike `.create()` we don't need to treat many-to-many
        # relationships as being a special case. During updates we already
        # have an instance pk for the relationships to be associated with.
        m2m_fields = []
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                m2m_fields.append((attr, value))
            else:
                setattr(instance, attr, value)

        instance.save()
        for attr, value in m2m_fields:
            field = getattr(instance, attr)
            field.set(value)

        return instance


    def get_school_name(self,obj):
        return obj.school_id.name






class CreateUserSerializer(serializers.ModelSerializer):
    school_name = serializers.SerializerMethodField()
    sms_code = serializers.CharField(write_only=True,required=True)
    token = serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id',)


    def validate(self, attrs):
        if settings.MESSAGE_CAN_USE:
            # todo 校验验证码
            phone = attrs['phone']
            sms_code = attrs['sms_code']
            try:
                real_code = SMSCode.objects.get(phone=phone)
            except SMSCode.DoesNotExist:
                raise serializers.ValidationError('验证码错误')
            timediff = (datetime.datetime.now() -utc2local(real_code.update_time)).seconds
            if timediff > 300:
                raise serializers.ValidationError('验证码已经失效')
            elif real_code.code != sms_code:
                raise serializers.ValidationError('验证码错误')
        # todo 检查 年级管理员
        if attrs.get('is_grade') is not None:
            try:
                users = User.objects.filter(is_grade=attrs.get('is_grade'))
            except User.DoesNotExist:
                pass
            if users:
                raise serializers.ValidationError('已有该年级的管理员')
        return attrs

    def create(self, validated_data):
        '''
        validated_data:反序列化后经过校验的大字典数据
        调用save的时候，如果没有传递instance那么执行create
        '''
        # todo 把不需要的先剔除

        password = validated_data.pop('password')
        validated_data.pop('sms_code')

        user = User.objects.create(**validated_data)
        user.set_password(password)  # 把密码加密后再赋值给user的password属性
        user.save()

        # todo 写入token  用于序列化返回
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER  # 引用jwt中的叫jwt_payload_handler函数(生成payload)
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER  # 函数引用 生成jwt
        payload = jwt_payload_handler(user)  # 根据user生成用户相关的载荷
        user.token = jwt_encode_handler(payload)  # 传入载荷生成完整的jwt

        return user

    def get_school_name(self,obj):
        return obj.school_id.name

