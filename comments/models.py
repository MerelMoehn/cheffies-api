from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe

# This code is based on the Code Institute walkthrough video

class Comment(models.Model):
    """
    The comment model
    Related to both User, who creates the comment
    And the Recipe
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
