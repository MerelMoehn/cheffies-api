from cheffies_api.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from likes.models import Like
from likes.serializers import LikeSerializer

# This code is based on the DRF walkthrough video of Code Institute


class LikeList(generics.ListCreateAPIView):
    """
    If logged in, one can see all likes
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    If owned by you, one can get and delete a like instance
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
