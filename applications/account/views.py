from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.response import Response
from applications.account.serializers import RegisterSerializer, LoginSerializer


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
