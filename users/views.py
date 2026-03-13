from rest_framework.generics import ListAPIView , DestroyAPIView
from users.serializers import CustomUserSerializer
from users.models import CustomUser
from rest_framework.permissions import AllowAny, IsAdminUser




class ClubMembersViewSet(ListAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]


class DeleteClubMemberViewSet(DestroyAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAdminUser]



