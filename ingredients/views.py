from cheffies_api.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions, filters
from .models import Ingredient
from .serializers import IngredientSerializer
from django_filters.rest_framework import DjangoFilterBackend


class IngredientList(generics.ListCreateAPIView):
    """
    List or create ingredient(s) when you are logged in
    """
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Ingredient.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'recipe',
    ]

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
