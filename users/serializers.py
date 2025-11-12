from rest_framework.serializers import ModelSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from users.models import CustomUser


class CustomUserSerializer(BaseUserSerializer):
    class Meta:
        model= CustomUser
        exclude = ['groups','user_permissions']