from rest_framework import serializers
from .models import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    recipe_rel = serializers.ReadOnlyField()

    class Meta:
        model = Ingredient
        fields = [
            'id', 'ingredient', 'recipe', 'measure_unit', 'amount_required',
            'created_at', 'recipe_rel',
        ]
