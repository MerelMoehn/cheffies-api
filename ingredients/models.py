from django.db import models
from recipes.models import Recipe
from django.contrib.auth.models import User


class Ingredient(models.Model):
    """
    Ingredient model, which is linked via a through table to
    the Recipe model
    """
    measurement_units = [
        ('cup', 'cup(s)'), ('g', 'gram'),
        ('tablespoon', 'tablespoon(s)'), ('item', 'item'),
        ('ml', 'ml'), ('l', 'L'), ('kg', 'kg'), ('ounce', 'ounce')
    ]
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    amount_required = models.IntegerField(blank=False)
    measure_unit = models.CharField(max_length=25, choices=measurement_units,
                                    default='g', blank=False)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['name', 'recipe']

    def __str__(self):
        return f'{self.amount_required} {self.name} {self.measure_unit} in {self.recipe}'
