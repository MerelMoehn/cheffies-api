from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers

# This code is based on the Code Institute Walkthrough and
# the Django Rest Framework documentation


class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )
