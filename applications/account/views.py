from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from applications.account.send_mail import send_hello
from applications.account.serializers import RegisterSerializer, LoginSerializer, ChangePasswordSerializer


class RegisterApiView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Вы успешно зарегистрировались.\n '
                        'Вам отправлено письмо с активацией',
                        status=201
                        )


class LoginApiView(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogoutApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('Вы успешно разлогинились!')


class ChangePasswordApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response('Пароль успешно обновлён')


@api_view(['POST'])
def send_hello_api_view(request):
    send_hello('vladislav001015@gmail.com')
    return Response('Письмо отправлено!')