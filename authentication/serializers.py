# Django & Rest Framework imports
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password

# Models
from django.contrib.auth.models import User
from authentication.models import Profile


class AuthTokenPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["username"] = user.username

        return token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("username", "password", "password2", "email")

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(username=validated_data["username"], email=validated_data["email"])
        user.set_password(validated_data["password"])
        user.save()

        # Create User's Profile
        Profile.objects.create(user=user)

        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ("user",)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, validators=[validate_password])
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "profile")

    def update(self, instance, validated_data):

        if validated_data.get("password"):
            hashed_password = make_password(validated_data["password"])
            validated_data.update({"password": hashed_password})

        if self.initial_data.get("profile"):
            profile_serializer = ProfileSerializer(instance.profile, data=self.initial_data.get("profile"))
            profile_serializer.is_valid(raise_exception=True)
            profile_serializer.save()

        return super().update(instance, validated_data)
