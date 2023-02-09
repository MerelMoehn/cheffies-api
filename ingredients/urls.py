from django.urls import path
from ingredients import views

urlpatterns = [
    path('ingredients/', views.IngredientList.as_view()),
]