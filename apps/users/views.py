from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.mixins import CreateModelMixin
from rest_framework import mixins
from rest_framework import viewsets
from .serializers import EmailVerifySerializer, UserRegisterSerializer, AvatarSerializer
from random import choice
from .models import VerifyCode
from utils.email_verify import EmailVerify
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
User = get_user_model()

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(email=username)|Q(username=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class EmailVerifyViewset(CreateModelMixin, viewsets.GenericViewSet):
    """
    发送邮箱验证码
    """
    serializer_class = EmailVerifySerializer

    def generate_code(self):
        """
        生成四位数字的验证码
        :return:
        """
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))

        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True) # 设置为true，如果不合法就抛异常返回400，不会进入下一步
        email = serializer.validated_data["email"]
        code = self.generate_code()
        email_verify = EmailVerify()
        email_status = email_verify.check_mail(code=code, email=email)
        if email_status["status"] != 1:
            return Response({
                "email": email_status["msg"]
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = VerifyCode(code=code, email=email)
            code_record.save()
            return Response({
                "email": email
            }, status=status.HTTP_201_CREATED)


class UserViewset(CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    用户
    """
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["first_name"] = user.first_name
        re_dict["username"] = user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()


class AvatarViewset(mixins.CreateModelMixin,
     mixins.UpdateModelMixin, viewsets.GenericViewSet):
    # (mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet)
    """
    头像
    """
    queryset = User.objects.all()
    serializer_class = AvatarSerializer
    print(124)

    def put(self, request, *args, **kwargs):
        print(1111)
        return Response()


