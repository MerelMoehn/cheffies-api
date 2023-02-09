from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Comment Serializer
    There are three additional instances added when returning
    a comment instance: is_owner, profile_id, profile_image
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'recipe', 'created_at', 'updated_at', 'content'
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    CommentDetail Serializer
    This serializer inherits from the Comment Serializer
    It is related to Recipe, which is set as ReadOnly
    """
    recipe = serializers.ReadOnlyField(source='recipe.id')
