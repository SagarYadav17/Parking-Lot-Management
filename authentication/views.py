# Django & Rest Framework imports
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

# Models
from django.contrib.auth.models import User

# Serializers
from authentication.serializers import RegisterSerializer, AuthTokenPairSerializer


class AuthTokenPairView(TokenObtainPairView):
    serializer_class = AuthTokenPairSerializer


class RegisterUserView(CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
