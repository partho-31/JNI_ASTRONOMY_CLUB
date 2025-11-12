from rest_framework.viewsets import ModelViewSet
from magazines.serializers import ArticleSerializer,MagazineSerializer,ReviewSerializer
from rest_framework.permissions import  IsAuthenticatedOrReadOnly
from api.permissions import CustomReviewPermission
from magazines.models import *



class MagazineViewSet(ModelViewSet):
    serializer_class = MagazineSerializer
    queryset = Magazine.objects.prefetch_related('articles').all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)



class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.prefetch_related('reviews').all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        magazine = Magazine.objects.get(id = self.kwargs.get('magazine_pk'))
        serializer.save(author = self.request.user,magazine = magazine)



class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.select_related('user').all()
    permission_classes = [CustomReviewPermission]

    def perform_create(self, serializer):
        article = Article.objects.get(id = self.kwargs.get('article_pk'))
        user = self.request.user

        if user.is_authenticated:
            serializer.save(user=user, article=article)
        else:
            serializer.save(user=None, article=article)
