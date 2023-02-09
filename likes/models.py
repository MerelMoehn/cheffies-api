from django.contrib.auth.models import User
from django.db import models
from recipes.models import Recipe

# This code is based on the Code Institute walkthrough video


class Like(models.Model):
    """
    The like model which is related to Owner(instance)
    And a Recipe(instance)
    'unique_together' is added to make sure
    a user can't like the same post twice.
    """
    recipe = models.ForeignKey(
        Recipe, related_name='likes', on_delete=models.CASCADE
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'recipe']

    def __str__(self):
        return f'{self.owner} {self.recipe}'
