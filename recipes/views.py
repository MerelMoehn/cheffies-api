from cheffies_api.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from .models import Recipe
from .serializers import RecipeSerializer


class RecipeList(generics.ListCreateAPIView):
    """
    List or create recipe(s) when you are logged in 
    When a recipe is created it is related to an owner/user
    """
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Recipe.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    If you are the owner you can retreive, update and delete
    a recipe
    """
    serializer_class = RecipeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Recipe.objects.all()
