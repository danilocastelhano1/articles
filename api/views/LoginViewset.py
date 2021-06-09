from rest_framework_jwt.views import JSONWebTokenAPIView

from api.serializers.LoginSerializer import LoginSerializer


class LoginViewset(JSONWebTokenAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        return super(LoginViewset, self).post(request, *args, **kwargs)
