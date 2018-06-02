from django.db import models

# Create your models here.
class Article(models.Model):
    article_heading = models.CharField(max_length=250)
    article_body = models.TextField()