from cheffies_api.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from .models import Ingredient
from .serializers import IngredientSerializer


class IngredientList(generics.ListCreateAPIView):
    """
    List or create ingredient(s) when you are logged in
    """
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Ingredient.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    If you are the owner you can retreive, update and delete
    a ingredient
    """
    serializer_class = IngredientSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Ingredient.objects.all()
