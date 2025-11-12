from django.urls import path,include
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter
from magazines.views import MagazineViewSet,ArticleViewSet,ReviewViewSet
from events.views import EventViewSet
from users.views import ClubMembersViewSet




router = SimpleRouter()
router.register('magazines',MagazineViewSet,basename= 'magazine')
router.register('events', EventViewSet, basename='event')

article_router = NestedSimpleRouter(router,'magazines',lookup = 'magazine')
article_router.register('articles',ArticleViewSet,basename='magazine-article')

review_router = NestedSimpleRouter(article_router,'articles',lookup ='article')
review_router.register('reviews',ReviewViewSet,basename='article-review')


urlpatterns = [
    path('',include(router.urls)),
    path('',include(article_router.urls)),
    path('',include(review_router.urls)),
    path('members/',ClubMembersViewSet.as_view(), name= 'club-members')
]
