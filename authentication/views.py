# Django & Rest Framework imports
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

# Models
from django.contrib.auth.models import User

# Serializers
from authentication.serializers import RegisterSerializer, AuthTokenPairSerializer, UserSerializer


class AuthTokenPairView(TokenObtainPairView):
    serializer_class = AuthTokenPairSerializer


class RegisterUserView(CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class ProfileView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_object(self):
        obj = get_object_or_404(User, username=self.kwargs["username"])

        if self.request.method != "GET" and obj != self.request.user:
            self.permission_denied(self.request)

        return obj
