from django.contrib.auth.models import User
from .models import Ingredient
from recipes.models import Recipe
from rest_framework import status
from rest_framework.test import APITestCase


class IngredientListViewTests(APITestCase):
    def setUp(self):
        self.merel = User.objects.create_user(
            username='merel', password='password')
        self.recipe_1 = Recipe.objects.create(
            owner=self.merel,
            title='a recipe',
            instructions="1. cook",
            cooking_time='23',
            prep_time='23'
        )

    def test_can_list_all_ingredients(self):
        Ingredient.objects.create(
            recipe=self.recipe_1,
            name="butter",
            owner=self.merel,
            amount_required=23)
        response = self.client.get('/ingredients/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_not_logged_in_cannot_create_ingredient(self):
        response = self.client.post('/ingredients/', {'name': 'flower'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class IngredientDetailViewTests(APITestCase):
    def setUp(self):
        self.merel = User.objects.create_user(
            username='merel', password='password')
        self.laura = User.objects.create_user(
            username='laura', password='password')
        self.recipe = Recipe.objects.create(
            owner=self.merel,
            title='a recipe',
            instructions="1. cook",
            cooking_time='23',
            prep_time='23'
        )
        self.ingredient = Ingredient.objects.create(
            recipe=self.recipe,
            name="flower",
            owner=self.merel,
            amount_required=23)

    def test_can_retreive_ingredient(self):
        response = self.client.get('/ingredients/1/')
        self.assertEqual(response.data['name'], 'flower')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_ingredient_with_invalid_id(self):
        response = self.client.get('/ingredients/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_cannot_update_another_users_ingredient(self):
        self.client.login(username='laura', password='password')
        response = self.client.put('/ingredients/1/', {'name': 'wine'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
