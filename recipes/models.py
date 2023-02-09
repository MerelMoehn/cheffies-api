from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    """
    Recipe model, related to 'owner', i.e. a User instance.
    And related to Ingredients via the through table Ingredients_needed
    Default image set so that we can always reference image.url.
    """

    recipe_categories = [
        ('starter', 'Starter'), ('main', 'Main'),
        ('dessert', 'Dessert'), ('snack', 'Snack')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    instructions = models.TextField(blank=False)
    category = models.CharField(max_length=30,
                                choices=recipe_categories,
                                default='main')
    cooking_time = models.IntegerField(blank=False)
    prep_time = models.IntegerField(blank=False)
    image = models.ImageField(
        upload_to='images/',
        default='../rachel-park-hrlvr2ZlUNk-unsplash_eseqep',
        blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
