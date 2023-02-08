from django.db import models
from recipes.models import Recipe


class Ingredient(models.Model):
    """
    Ingredient model, which is linked via a through table to
    the Recipe model
    """
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.name}'


class Ingredient_needed(models.Model):
    """
    Through table to relate Ingredient to Recipe and add
    amount required and measurement dropdown
    """
    measurement_units = [
        ('cup', 'cup(s)'), ('g', 'gram'),
        ('tablespoon', 'tablespoon(s)'), ('item', 'item'),
        ('ml', 'ml'), ('l', 'L'), ('kg', 'kg'), ('ounce', 'ounce')
    ]

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name="ingredients_needed")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE,
                                   related_name="ingredients_needed")
    amount_required = models.IntegerField(blank=True)
    measure_unit = models.CharField(max_length=25, choices=measurement_units,
                                    default='g')

    def __str__(self):
        return f'{self.amount_required} {self.name} {self.measure_unit}'
