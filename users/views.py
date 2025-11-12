from rest_framework.generics import ListAPIView
from users.serializers import CustomUserSerializer
from users.models import CustomUser
from rest_framework.permissions import AllowAny




class ClubMembersViewSet(ListAPIView) :
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]



