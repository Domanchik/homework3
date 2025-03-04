from django.db import models
from django.contrib.auth.models import User 


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Publication(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="publications")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="publications")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



