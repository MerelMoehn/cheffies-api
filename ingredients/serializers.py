from rest_framework import serializers
from .models import Ingredient, Ingredient_needed


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = [
            'id', 'name', 'created_at'
        ]


class Ingredient_neededSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient_needed()
        fields = [
            'id', 'ingredient', 'recipe', 'amount_required', 'measure_unit'
        ]
