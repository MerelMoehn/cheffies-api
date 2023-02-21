from rest_framework import serializers
from .models import Ingredient
from django.utils.translation import gettext_lazy as _


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = [
            'id', 'name', 'recipe', 'measure_unit', 'amount_required',
            'created_at', 'owner',
        ]

        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('name', 'recipe'),
                message=_("Duplicate ingredient detected.")
            )
        ]

