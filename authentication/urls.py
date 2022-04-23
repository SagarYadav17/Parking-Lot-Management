from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView
from authentication.views import AuthTokenPairView, RegisterUserView, ProfileView

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="auth-register"),
    path("login/", AuthTokenPairView.as_view(), name="auth-login-token"),
    path("refresh/", TokenRefreshView.as_view(), name="auth-token-refresh"),
    path("profile/<str:username>/", ProfileView.as_view(), name="auth-profile"),
]
