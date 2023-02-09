from rest_framework import serializers
from .models import Recipe
from likes.models import Like


class RecipeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 3:
            raise serializers.ValidationError(
                'The image size is larger than 3MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width is larger than 4096px.'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height is larger than 4096px.'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, recipe=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Recipe
        fields = [
            'id', 'owner', 'profile_id', 'profile_image', 'created_at',
            'updated_at', 'title', 'instructions', 'category',
            'cooking_time', 'prep_time', 'image',
            'is_owner', 'like_id',
        ]
