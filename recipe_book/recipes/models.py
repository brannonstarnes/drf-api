from django.db import models
from django.contrib.auth import get_user_model

class Recipe(models.Model):
    chef = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    body = models.TextField()
    created_at =models.DateField(auto_now=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title