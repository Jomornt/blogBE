from rest_framework import serializers
from django.contrib.auth import get_user_model
import re
from bloggl.settings import REGEX_EMAIL
from datetime import datetime, timedelta
from .models import VerifyCode
from rest_framework.validators import UniqueValidator
from rest_framework.response import Response

User = get_user_model()


class EmailVerifySerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100)

    def validate_email(self, email):
        if User.objects.filter(email = email).count():
            raise serializers.ValidationError("用户已经存在")

        if not re.match(REGEX_EMAIL, email):
            raise serializers.ValidationError("邮箱格式非法")

        # 验证码发送频率
        one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(created_time__gt=one_mintes_ago, email=email).count():
            raise serializers.ValidationError("距离上一次发送未超过60s")

        return email


class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """
    class Meta:
        model = User
        fields = ("id", "username", "first_name")


class AvatarSerializer(serializers.ModelSerializer):
    """
    用户头像
    """
    class Meta:
        model = User
        fields = ("id", "avatar", "username")


class UserRegisterSerializer(serializers.ModelSerializer):
    code = serializers.CharField(required=True, write_only=True, max_length=4, min_length=4,label="验证码",
                                 error_messages={
                                     "blank": "请输入验证码",
                                     "required": "请输入验证码",
                                     "max_length": "验证码格式错误",
                                     "min_length": "验证码格式错误"
                                 },
                                 help_text="验证码")
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])
    password = serializers.CharField(
        style={'input_type': 'password'}, help_text="密码", label="密码", write_only=True,
    )

    def validate_code(self, code):
        verify_records = VerifyCode.objects.filter(email=self.initial_data["username"]).order_by("-created_time")
        if verify_records:
            last_record = verify_records[0]

            five_mintes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
            if five_mintes_ago > last_record.created_time:
                raise serializers.ValidationError("验证码过期")

            if last_record.code != code:
                raise serializers.ValidationError("验证码错误")

        else:
            raise serializers.ValidationError("验证码错误")

    def validate(self, attrs):
        attrs["email"] = attrs["username"]
        attrs["first_name"] = attrs["username"]
        del attrs["code"]
        return attrs

    class Meta:
        model = User
        fields = ['username', "code", "email", "password", "last_login"]