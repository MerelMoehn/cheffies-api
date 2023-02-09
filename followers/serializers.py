from rest_framework import serializers
from django.db import IntegrityError
from .models import Follower

# This code is based on the DRF walkthrough videos of Code Institute


class FollowerSerializer(serializers.ModelSerializer):
    """
    Follower model serializer
    In the create method it is ensured you cannot follow
    another user twice.
    """
    followed_name = serializers.ReadOnlyField(source='followed.username')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Follower
        fields = [
            'id', 'owner', 'followed', 'followed_name', 'created_at'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})
