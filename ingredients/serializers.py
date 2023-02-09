from rest_framework import serializers
from django.db import IntegrityError
from .models import Ingredient


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = [
            'id', 'name', 'recipe', 'measure_unit', 'amount_required',
            'created_at', 'owner',
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
