from django.contrib.auth.models import User
from .models import Recipe
from rest_framework import status
from rest_framework.test import APITestCase


class RecipeListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='merel', password='password')

    def test_can_list_all_recipes(self):
        merel = User.objects.get(username='merel')
        Recipe.objects.create(
            owner=merel,
            title='a recipe',
            instructions="1. cook",
            cooking_time='23',
            prep_time='23')
        response = self.client.get('/recipes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_recipe(self):
        self.client.login(username='merel', password='password')
        response = self.client.post('/recipes/', {
            'title': 'nice recipe',
            'instructions': 'cook',
            'cooking_time': '23', 
            'prep_time': '25'})
        count = Recipe.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cannot_create_recipe(self):
        response = self.client.post('/recipes/', {'title': 'nice recipe'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class RecipeDetailViewTests(APITestCase):
    def setUp(self):
        self.merel = User.objects.create_user(username='merel', password='password')
        self.laura = User.objects.create_user(username='laura', password='password')
        Recipe.objects.create(
            owner=self.merel,
            title='a recipe',
            instructions="1. cook",
            cooking_time='23',
            prep_time='23'
        )
        Recipe.objects.create(
            owner=self.laura,
            title='a good recipe',
            instructions="1. cook with grace",
            cooking_time='23',
            prep_time='23'
        )

    def test_can_retreive_recipe(self):
        response = self.client.get('/recipes/1/')
        self.assertEqual(response.data['title'], 'a recipe')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_recipe_with_invalid_id(self):
        response = self.client.get('/recipes/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_recipe(self):
        self.client.login(username='merel', password='password')
        response = self.client.put('/recipes/1/', {
            'owner': self.merel,
            'title': 'a new title',
            'instructions': "1. cook with grace",
            'cooking_time': '23',
            'prep_time': '23'})
        recipe = Recipe.objects.filter(pk=1).first()
        self.assertEqual(recipe.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_another_users_recipe(self):
        self.client.login(username='merel', password='password')
        response = self.client.put('/recipes/2/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)