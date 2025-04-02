from django.db import models

# Create your models here.

class Articles(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=70)
    author = models.CharField(max_length=70)
    description = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)