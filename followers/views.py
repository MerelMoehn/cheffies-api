from cheffies_api.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from .serializers import FollowerSerializer
from .models import Follower


class FollowerList(generics.ListCreateAPIView):
    """
    Get a list of all followers
    Being able to create a follow instance
    When creating a follow instance, the owner is related to the user
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a follower
    To unfollow, the destroy option is used
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
