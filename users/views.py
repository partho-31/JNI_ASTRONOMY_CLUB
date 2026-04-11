from rest_framework.generics import ListAPIView , DestroyAPIView
from users.serializers import CustomUserSerializer
from users.models import CustomUser
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter

class GoogleLoginView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    
    def get_response(self):
        # Call the parent method to complete the social login
        response = super().get_response()

        user = self.user  # The logged-in user
        refresh = RefreshToken.for_user(user)

        # Prepare custom response data with JWT tokens and user info
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'success' : True,
        }
        return Response(data)


class ClubMembersViewSet(ListAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]


class DeleteClubMemberViewSet(DestroyAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAdminUser]



