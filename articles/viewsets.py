from rest_framework import viewsets 
from .models import Article 
from .serializers import ArticleSerializer 

class ArticleViewSet(viewsets.ModalViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    