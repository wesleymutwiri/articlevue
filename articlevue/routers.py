from rest_framework import routers
from article.viewsets import ArticlViewSet

router = routers.DefaultRouter()
router.register(r'article', ArticlViewSet)