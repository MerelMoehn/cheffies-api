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
